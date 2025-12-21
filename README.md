# HW#44 Definition
## Login Lambda Function
1. Create lambda function processing event from HTTP Gateway<br>
1.1 Body event should contain JSON with following fields:<br>
     - username (required) <br> 
     - password (required) <br>
     - new password (optional, required only if new password required)<br>
1.2 Following flows<br>
1.2.1 Normal Flow - response with status code 200 and {"access_token":< access token >, "id_token": < id_token >, "refresh_token" : < refresh token >}<br> 
1.2.1 Alternative Flows - response with status code 400 and {"error": "invalid username or password"} <br>
## Create HTTP Gateway with POST route "/login" and integration for Login Lambda Function invocation
## Attach Cognito Authorizer to HTTP Gateway for "calculator" from HW#43
## Make sure all auth flows work properly


   




 