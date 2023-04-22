from time import strftime
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

class PasswordRequest(BaseModel):
    secret_name: str
    username: str 

class SecretsManagerClient:
    def __init__(self, access_key, secret_key, region):
        session = boto3.session.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)
        self.client = session.client('secretsmanager')

@app.get("/my-first-api")
def hello(name = None):
    if(name is None):
        text = "Hello!"
    else:
        text="Hello " + name + "!"
    return {text}

@app.post('/create_secret')
def user_add(password_request: PasswordRequest):
    students.append(student)
    return{'student': students[-1]}

def run():
    uvicorn.run("app:app", port=5000, log_level="info")

if __name__ == "__main__":
    run()