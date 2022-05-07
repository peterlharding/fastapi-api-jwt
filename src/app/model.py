# app/model.py
# encoding: utf-8
#
# ----------------------------------------------------------------------------

from pydantic import BaseModel, Field, EmailStr

# ----------------------------------------------------------------------------

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Securing FastAPI applications with JWT.",
                "content": "In this tutorial, you'll learn how to secure your application by enabling authentication using JWT.  PyJWT will be used to sign, encode and decode JWT tokens...."
            }
        }

# ----------------------------------------------------------------------------

class UserSchema(BaseModel):
    id: int = Field(default=None)
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Smith",
                "email": "john@example.com",
                "password": "secret"
            }
        }

# ----------------------------------------------------------------------------

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "john@example.com",
                "password": "secret"
            }
        }

# ----------------------------------------------------------------------------
