from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: bool = True

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/blog/unpublished")
def unpublished_blogs():
    return {"message": "All unpublished blogs"}

@app.post("/blog")
def create_blog(blog: Blog):
    return {"message": f"Blog titled '{blog.title}' created successfully!"} 

@app.get("/blog/{id}")
def blog(id: int):
    return {"message": f"Blog with id {id}"}    

@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"message": f"Comments for blog with id {id}"}