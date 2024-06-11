from fastapi import HTTPException, Header
import jwt

def auth_middleware(x_auth_token = Header()):
    try:
        # get the user token from the headers
        if not x_auth_token:
            raise HTTPException(401, 'No auth token, access denied!')
        # decode the token
        verified_token = jwt.decode(x_auth_token, 'password_key', ['HS256'])

        if not verified_token:
            raise HTTPException(401, 'Token verification failed, authorization denied!')
        # get the id from the token
        uid = verified_token.get('id')
        return {'uid': uid, 'token': x_auth_token}
        # postgres database get the user info
    except jwt.PyJWTError:
        raise HTTPException(401, 'Token is not valid, authorization failed.')