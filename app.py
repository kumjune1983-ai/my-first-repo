from fastapi import FastAPI

app = FastAPI()  # This is the app Uvicorn looks for

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
