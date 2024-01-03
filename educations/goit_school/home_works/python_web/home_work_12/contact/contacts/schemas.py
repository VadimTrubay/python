import re

from datetime import datetime, date
from pydantic import BaseModel, EmailStr, Field, validator


class ContactModel(BaseModel):
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    email: EmailStr
    phone: str = Field()
    birthday: date
    information: str = Field('', max_length=250)

    @validator("phone")
    def phone_number(cls, phone):
        match = re.match(r"^\+38\(0\d{2}\)\d{3}-\d{2}-\d{2}$", phone)
        if not match or (len(phone) != 17):
            raise ValueError("Phone number must be in the format +38(0хх)ххх-х-ххх")
        return phone


class UserModel(BaseModel):
    username: str = Field(min_length=4, max_length=50)
    email: EmailStr
    password: str = Field(min_length=4, max_length=50)


class ContactResponse(ContactModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"