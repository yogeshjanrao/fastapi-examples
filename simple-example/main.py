from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/blog/unpublished")
def unpublished_blogs():
    return {"message": "All unpublished blogs"}

@app.get("/blog/{id}")
def blog(id: int):
    return {"message": f"Blog with id {id}"}    

@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"message": f"Comments for blog with id {id}"}