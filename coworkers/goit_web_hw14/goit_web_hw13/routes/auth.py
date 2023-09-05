from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    status,
    Security,
    BackgroundTasks,
    Request,
)
from fastapi.security import (
    OAuth2PasswordRequestForm,
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from sqlalchemy.orm import Session

from goit_web_hw13.database.db import get_db
from goit_web_hw13.schemas import UserModel, UserResponse, TokenModel, RequestEmail
from goit_web_hw13.repository import auth as repository_auth
from goit_web_hw13.services.auth import auth_service
from goit_web_hw13.services.email import send_email

router = APIRouter(prefix="/auth", tags=["auth"])
security = HTTPBearer()


@router.post(
    "/signup", response_model=UserResponse, 
    status_code=status.HTTP_201_CREATED
    )
async def signup(
    body: UserModel,
    background_tasks: BackgroundTasks,
    request: Request,
    db: Session = Depends(get_db),
    ) -> dict | HTTPException:
    """
    Creates the '/signup' route for user registration.
    The signup function for the '/signup' route handles the POST
    operation. It creates a new user if a user with this
    email address does not exist. There cannot be two users
    with the same email in the system. If a user with this email
    already exists in the database, the function throws an
    HTTPException with status code 409 Conflict and details
    detail="Account already exists".

    :param body: The data for the user to create.
    :type body: UserModel
    :param background_tasks: The BackgroundTasks class allows you to
        run long-running tasks, such as sending email or processing
        images, in the background
    :type background_tasks: BackgroundTasks
    :param request: Requests allows you to send HTTP/1.1 requests
        extremely easily
    :type request: Request
    :param db: The database session.
    :type db: Session | Depends(get_db)
    :return: The newly created user or HTTPException
        with message "Account already exists".
    :rtype: User | HTTPException
    """
    exist_user = await repository_auth.get_user_by_email(body.email, db)
    if exist_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Account already exists"
        )
    body.password = auth_service.get_password_hash(body.password)
    new_user = await repository_auth.create_user(body, db)
    background_tasks.add_task(
        send_email, new_user.email, new_user.username, request.base_url
    )
    return {"user": new_user, "detail": "User successfully created"}


@router.post("/login", response_model=TokenModel)
async def login(
    body: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
) -> dict:
    """
    Creates the '/login' route for user authentication.
    The function 'login' checks the presence of the user in
    the database, email verification and user password.
    If something is missing, the function returns the
    HTTP 401 Unauthorised error and a corresponding message.
    If the validation is passed, the function generates new
    refresh_token and access_token to send to the client.
    Also update the refresh token in the database for the user

    :param body: The data for the user to create.
    :type body: OAuth2PasswordRequestForm | Depends()
    :param db: The database session.
    :type db: Session | Depends(get_db)
    :return: The dict or HTTPException
    :rtype: dict | HTTPException
    """
    user = await repository_auth.get_user_by_email(body.username, db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email"
        )
    if not user.confirmed:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Email not confirmed"
        )
    if not auth_service.verify_password(body.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password"
        )
    # Generate JWT
    access_token = await auth_service.create_access_token(data={"sub": user.email})
    refresh_token = await auth_service.create_refresh_token(data={"sub": user.email})
    await repository_auth.update_token(user, refresh_token, db)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.get("/refresh_token", response_model=TokenModel)
async def refresh_token(
    credentials: HTTPAuthorizationCredentials = Security(security),
    db: Session = Depends(get_db),
) -> dict:
    """
    The refresh_token function for the '/refresh_token' route handles
    the GET operation. It decodes the refresh_token and retrieves
    the corresponding user from the database. It then creates new
    access and refresh tokens, and updates the refresh_token in
    the database for the user as well. If the refresh token is
    invalid, an HTTPException is thrown with status code 401 and
    detail="Invalid refresh token".

    :param credentials: credentials
    :type credentials: HTTPAuthorizationCredentials | Security(security)
    :param db: The database session.
    :type db: Session | Depends(get_db)
    :return: The dict or HTTPException
    :rtype: dict | HTTPException
    """
    token = credentials.credentials
    email = await auth_service.decode_refresh_token(token)
    user = await repository_auth.get_user_by_email(email, db)
    if user.refresh_token != token:
        await repository_auth.update_token(user, None, db)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token"
        )

    access_token = await auth_service.create_access_token(data={"sub": email})
    refresh_token = await auth_service.create_refresh_token(data={"sub": email})
    await repository_auth.update_token(user, refresh_token, db)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.get("/confirmed_email/{token}")
async def confirmed_email(token: str, db: Session = Depends(get_db)) -> dict:
    """
    The function sets the user's confirmed attribute to True in
    the database or generates a message in case of an error

    :param token: token from email
    :type token: str
    :param db: The database session.
    :type db: Session | Depends(get_db)
    :return: The dict or HTTPException
    :rtype: dict | HTTPException
    """
    email = await auth_service.get_email_from_token(token)
    user = await repository_auth.get_user_by_email(email, db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Verification error"
        )
    if user.confirmed:
        return {"message": "Your email is already confirmed"}
    await repository_auth.confirmed_email(email, db)
    return {"message": "Email confirmed"}


@router.post("/request_email")
async def request_email(
    body: RequestEmail,
    background_tasks: BackgroundTasks,
    request: Request,
    db: Session = Depends(get_db),
) -> dict:
    """
    Sending an email confirmation request

    :param body: the email.
    :type body: RequestEmail
    :param background_tasks: The BackgroundTasks class allows
        you to run long-running tasks, such as sending email
        or processing images, in the background
    :type background_tasks: BackgroundTasks
    :param request: Requests allows you to send HTTP/1.1 requests
        extremely easily
    :type request: Request
    :param db: The database session.
    :type db: Session | Depends(get_db)
    :return: The dict or HTTPException
    :rtype: dict | HTTPException
    """
    user = await repository_auth.get_user_by_email(body.email, db)

    if user.confirmed:
        return {"message": "Your email is already confirmed"}
    if user:
        background_tasks.add_task(
            send_email, user.email, user.username, request.base_url
        )
    return {"message": "Check your email for confirmation."}
