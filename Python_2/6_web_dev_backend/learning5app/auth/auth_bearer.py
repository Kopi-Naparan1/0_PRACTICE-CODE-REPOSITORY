#auth/auth_bearer.py

from fastapi.security import OAuth2PasswordBearer

#  Purpose:
# (1) Acts as security guard
# (2) Look for the token in the authorization header
# (3) Make sure it exists
# (4) Hand the token off to the validator
# NOTE: It doesn't verify the token, it grabs it and pass it to verifier.


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

