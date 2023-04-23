import boto3
import secrets
import string
import botocore.exceptions

class SecretsManagerClient:
    def __init__(self, access_key:str, secret_key:str, region:str):
        session = boto3.session.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)
        self.client = session.client('secretsmanager')

    def create_secret(self, name:str, secret_string:str, description=None):
        if description is not None:
            self.client.create_secret(
                Name=name,
                SecretString=secret_string
            )
        else:
            self.client.create_secret(
                Name=name,
                SecretString=secret_string,
                Description=description
            )

    def generate_password(self) -> string:
        alphabet = string.ascii_letters + string.digits + string.printable + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(20))
        return(password)
    
    def generate_and_store_secret(self, secret_name:str, username:str, description=None):
        new = True
        password = self.generate_password()
        secret = {
            'username': username,
            'password': password,
        }
        secret = str(secret)
        try:
            self.create_secret(name=secret_name, secret_string=secret, description=description)
        except self.client.exceptions.ResourceExistsException:
            new = False
        return new