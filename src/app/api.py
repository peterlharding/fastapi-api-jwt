# app/api.py
# encoding: utf-8
#
# ----------------------------------------------------------------------------

@app.get("/posts", tags=["posts"])
async def get_posts() -> dict:
    return { "data": posts }

# ----------------------------------------------------------------------------

@app.get("/posts/{id}", tags=["posts"])
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

# ----------------------------------------------------------------------------
