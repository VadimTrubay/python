"""
settings for sending emails
"""

from pathlib import Path

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from fastapi_mail.errors import ConnectionErrors
from pydantic import EmailStr

from goit_web_hw13.services.auth import auth_service
from goit_web_hw13.conf.config import settings


conf = ConnectionConfig(
    MAIL_USERNAME=settings.mail_username,
    MAIL_PASSWORD=settings.mail_password,
    MAIL_FROM=EmailStr(settings.mail_from),
    MAIL_PORT=settings.mail_port,
    MAIL_SERVER=settings.mail_server,
    MAIL_FROM_NAME="Desired Name",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=Path(__file__).parent / "templates",
)
# conf = ConnectionConfig(
#     MAIL_USERNAME="vakula1301@meta.ua",
#     MAIL_PASSWORD="Gogol_1301",
#     MAIL_FROM=EmailStr("vakula1301@meta.ua"),
#     MAIL_PORT=465,
#     MAIL_SERVER="smtp.meta.ua",
#     MAIL_FROM_NAME="Desired Name",
#     MAIL_STARTTLS=False,
#     MAIL_SSL_TLS=True,
#     USE_CREDENTIALS=True,
#     VALIDATE_CERTS=True,
#     TEMPLATE_FOLDER=Path(__file__).parent / 'templates',
# )


async def send_email(email: EmailStr, username: str, host: str) -> None:
    """
    email sending function

    :param email: EmailStr: user's email
    :param username: str: user's username
    :return: None | ConnectionErrors: None or print Error message
    """
    try:
        token_verification = auth_service.create_email_token({"sub": email})
        message = MessageSchema(
            subject="Confirm your email ",
            recipients=[email],
            template_body={
                "host": host,
                "username": username,
                "token": token_verification,
            },
            subtype=MessageType.html,
        )

        fm = FastMail(conf)
        await fm.send_message(message, template_name="email_template.html")
    except ConnectionErrors as err:
        print(err)
