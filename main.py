import os

from fastapi import FastAPI

app = FastAPI()

# read the enviroment variable and say hi and the message

MESSAGE = os.getenv("MESSAGE", "Hello World")


@app.get("/")
def read_root():
    return {"message": MESSAGE}
