import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# read the environment variable
MESSAGE = os.getenv("MESSAGE", "Hello World")

@app.get("/")
def read_root():
    return {"message": "Default route"}

@app.get("/message")
def read_message():
    return {"message": MESSAGE}
