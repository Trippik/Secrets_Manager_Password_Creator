# Secrets Manager Password Creator

This program is designed to be run within/with access to a seucred or isolated AWS environment, providing an REST API to generate account credentials and save them to Secrets Manager with the requestor not knowing the password for the account.
The concept is if a developer is trying to move a system into the isolated AWS environment, they can then create any needed static credentials within the isolated environment by simply calling the API and pull them into their program/system programatically using AWS Secrets Manager, essentially allowing the developer to use/create credentials within an isolated AWS without ever having to know them.

To make a request simply call the API on a /create-secret path (e.g https://address-of-api/create-secret and specify the secret_name, username, and description using the JSON format shown below. The Secrets Manager Password Creator will then generate a random password to accompany your username as a key value within the secret, and save them to the Secrets Manager of the isolated AWS environment.
```
{
'secret_name': 'Example Secret',
'username': 'Example User',
'description': 'Example Secret JSON',
}
```

## Required Environment Variables
ACCESS-KEY = AWS Access Key ID, allowing the API to access to the isolated AWS Account
SECRET-KEY = Secret Key to allow the API access to the isolated AWS Account
REGION = AWS Region (e.g us-east-1) to create the secrets in

## Network Requirements

A port will need to be forwarded to port 8000 of the container that will be used for HTTP access to the API.
