from time import strftime
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

from secrets_manager.lib.secrets_manager import SecretsManagerClient

app = FastAPI()

sm_client = SecretsManagerClient(access_key=os.environ["ACCESS-KEY"], secret_key=os.environ["SECRET-KEY"], region=os.environ["REGION"])

class PasswordRequest(BaseModel):
    secret_name: str
    username: str 
    description: str

@app.get("/my-first-api")
def hello(name = None):
    if(name is None):
        text = "Hello!"
    else:
        text="Hello " + name + "!"
    return {text}

@app.post('/create_secret')
def user_add(password_request: PasswordRequest):
    secret_name = password_request.secret_name
    username = password_request.username
    description = password_request.description
    sm_client.generate_and_store_secret(secret_name=secret_name, username=username, description=description)

def run():
    uvicorn.run("app", port=5000, log_level="info")

if __name__ == "__main__":
    run()