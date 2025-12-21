import boto3
from botocore.exceptions import ClientError
from getpass import getpass
CLIENT_ID = "6n5mvgjg3rje55ek2dtkju0tmm"
USERNAME = "yuragranovsky"
CHALLENGE_NAME = 'ChallengeName'
def initiate_auth(client, password)->dict:
    resp = client.initiate_auth(
        AuthFlow="USER_PASSWORD_AUTH",
        ClientId = CLIENT_ID,
        AuthParameters ={
            "USERNAME":USERNAME,
            "PASSWORD": password
        }
    )
    return resp
def respond_to_new_passowrd_challenge(client, password, session) -> dict:
    resp = client.respond_to_auth_challenge(
        ClientId = CLIENT_ID,
        ChallengeName = 'NEW_PASSWORD_REQUIRED',
        Session = session,
        ChallengeResponses = {
            "USERNAME":USERNAME,
            "NEW_PASSWORD": password
        }
    )
    return resp
def main():
    try:
        client = boto3.client("cognito-idp", region_name="il-central-1")
        password = getpass("Enter password: ")
        resp = initiate_auth(client, password)
        
        if CHALLENGE_NAME in resp:
            if resp[CHALLENGE_NAME] != 'NEW_PASSWORD_REQUIRED':
                print(f"Script doesn't process {resp[CHALLENGE_NAME]}")
            else:
                password = getpass("Enter new password: ")
                resp = respond_to_new_passowrd_challenge(client, password, resp['Session'])
                print(resp)
        else:
            print(resp)
    except  ClientError as ce:
        print(ce.response.get("Error", "Unknown"))   
    
    
if __name__ == "__main__":
    main()   