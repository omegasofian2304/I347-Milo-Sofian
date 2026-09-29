import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# read the enviroment variable and say hi and the message
MESSAGE = os.getenv("MESSAGE", "Hello World")

@app.get("/")
def read_root():
    return {"message": "Default"}

@app.get("/message")
def read_root():
    return {"message": MESSAGE}
