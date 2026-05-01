from fastapi import FastAPI 

myapp = FastAPI()

@myapp.get("/")
def greet():
    return {"message" : "Hello!!"}