from passlib.context import CryptContext

# bcrypt is preferred over others for passwords because bcrypt is
# intentionally slow, making brute-force attacks computationally expensive. 

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# get_password_hash turns a plain password into an irreversible scrambled string. 
# verify_password doesn't unscramble it -> that's impossible by design -> it re-hashes the input the user just typed 
# and compares the two hashes. This means even the developer can never see 
# anyone's actual password, even by looking directly in the database.

from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = "dev-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])