# goit_web_hw13
# verification and password reset


1. poetry shell
2. start docker container with postgres SQL
   and created BD web_hw12
3. # Setting up the alembic package
   alembic init migrations
   alembic revision --autogenerate -m 'Init'
   alembic upgrade head
4. # (optional)
   py goit_web_hw13/database/seeds.py
   # - to fill the database with fake data
5. py main.py
6. uvicorn main:app --host localhost --port 8000 --reload
7. http://127.0.0.1:8000/docs

# create .env

POSTGRES_DB=
POSTGRES_DOMAIN=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_PORT=

SQLALCHEMY_DATABASE_URL=postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_DOMAIN}:${POSTGRES_PORT}/${POSTGRES_DB}

SECRET_KEY=
ALGORITHM=

MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=${MAIL_USERNAME}
MAIL_PORT=
MAIL_SERVER=

REDIS_HOST=
REDIS_PORT=

CLOUDINARY_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=