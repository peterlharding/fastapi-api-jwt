# encoding: utf-8
#
# pylint disable=xxxx
# -----------------------------------------------------------------------------

import httpx
import uvicorn

from fastapi import (
    Body,
    Depends,
    FastAPI,
    # HTTPException,
    # Request
)

# from fastapi.security import OAuth2PasswordBearer
# from starlette.config import Config

from typing import List, Dict

# from pydantic import BaseModel

# -----------------------------------------------------------------------------

from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_handler import signToken
from app.auth.auth_bearer import JWTBearer

# -----------------------------------------------------------------------------

posts = [
    {
        "id": 1,
        "title": "Some Title",
        "content": "Some junk content ..."
    }
]

users = [
    UserSchema(**{"id": 1, "fullname":"John", "email": "john@example.com", "password": "secret"}),
    UserSchema(**{"id": 2, "fullname":"Tom",  "email": "tom@example.com",  "password": "secret"})
]

# -----------------------------------------------------------------------------

app = FastAPI()


# -----------------------------------------------------------------------------
# Protected, get items route
# -----------------------------------------------------------------------------

@app.get("/", tags=["root"])
def read_root() -> Dict:
    return {"Hello": "World"}

# -----------------------------------------------------------------------------

@app.post("/users", dependencies=[Depends(JWTBearer())], tags=["user"])
async def add_user(user: UserSchema) -> dict:
    user.id = len(users) + 1
    users.append(user)
    return user.json()

# -----------------------------------------------------------------------------

@app.get("/users", dependencies=[Depends(JWTBearer())],  tags=["user"])
async def get_users() -> List:
    results = []
    for user in users:
        results.append(user)
    return results

# -----------------------------------------------------------------------------

@app.get("/posts", dependencies=[Depends(JWTBearer())], tags=["post"])
async def get_posts() -> dict:
    return { "data": posts }

# ----------------------------------------------------------------------------

@app.get("/posts/{id}", dependencies=[Depends(JWTBearer())], tags=["post"])
async def get_single_post(id: int) -> dict:
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }

# -----------------------------------------------------------------------------

@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["post"])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }

# -----------------------------------------------------------------------------

@app.post("/register", tags=["user"])
async def register(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signToken(user.email)

# -----------------------------------------------------------------------------

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

# -----------------------------------------------------------------------------

@app.post("/login", tags=["user"])
async def login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signToken(user.email)
    return {
        "error": "Wrong login details!"
    }

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)

# -----------------------------------------------------------------------------
