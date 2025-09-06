from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.status import HTTP_403_FORBIDDEN
from learning6app.app_api.auth.auth_handler import verify_token

# This should verify and decode token


# JSON TOKEN Bearer. The HTTP bearer is extended in this class.
# This is the subclass
class JWTBearer(HTTPBearer):
    # auto_error tells base class to give 403 error when token are not provided.
    # calls the constructor of the parent class (HTTPBearer) use that in JWTBearer
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    # __call__ makes this class behaves like a function. Everytime this class gets called, it behaves like a function.
    async def __call__(self, request: Request):

        # HTTP.A.C. looks for the scheme, and credentials.
        # right side of = . calls the parent class (HTTPBearer)'s __call__() to extract credentials.
        # Then, that will return the HTTP.A.C : declare it to credentials
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)

        # Check if credentials were returned. If not, raise 403
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid authentication scheme.")

            if not verify_token(credentials.credentials):
                raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid or expired token.")

            # This only returns the token not the schema
            return credentials.credentials
        else:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid authorization code.")
