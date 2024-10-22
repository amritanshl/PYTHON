from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating:Optional[int] = None

my_posts = [{"title":"title of post 1", "content": "content of post ", "id": 1}, 
            {"title":"favorite food", "content": "I like Pizza", "id": 2}]

def find_post (id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
async def root():
    return {"message":"Hello amritf"}


@app.get("/posts")
def get_posts():
    return {"data":my_posts}


@app.post("/posts")
def create_posts(post: Post, status_code = status.HTTP_201_CREATED):
    # print(post.rating)
    # print(post.dict())
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return{"data": post_dict}





# @app.post("/posts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['title']} content: {payload['places']}"} 


# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"detial":post}

@app.get("/posts/{id}")
def get_posts(id:int, response : Response):
    Post = find_post(int(id))
    if not Post: 
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'messsage':f"post with {id} does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} does not exist")
    return {"post_deitails":Post}

@app.delete("/posts/{id}")
def delete_post(id:int):
    index = find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} does not exist")
    
    my_posts.pop(index)
    return {'message': 'post was successfully delted'}