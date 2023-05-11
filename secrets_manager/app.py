from time import strftime
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

from secrets_manager.lib.secrets_manager import SecretsManagerClient
from secrets_manager.lib.logging import logger

app = FastAPI()

sm_client = SecretsManagerClient(access_key=os.environ["ACCESS-KEY"], secret_key=os.environ["SECRET-KEY"], region=os.environ["REGION"])

class PasswordRequest(BaseModel):
    secret_name: str
    username: str 
    description: str

@app.get("/test")
def test():
    return {'API Responding Correctly'}

@app.post('/create_secret')
def user_add(password_request: PasswordRequest):
    secret_name = password_request.secret_name
    username = password_request.username
    description = password_request.description
    logger.info('Create secret requrest received, secret_name: %s, username: %s, description: %s', secret_name, username, description)
    new = sm_client.generate_and_store_secret(secret_name=secret_name, username=username, description=description)
    if new:
        message = f"{secret_name} created successfuly"
    else:
        message = f"Secret named {secret_name} already exists"
    return {message}

def run():
    uvicorn.run("secrets_manager.app:app", host='0.0.0.0', port=8000, log_level="info")

if __name__ == "__main__":
    run()
