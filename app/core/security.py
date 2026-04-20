from datetime import UTC, datetime, timedelta
from typing import Any

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# сверка простого пароля и хеш
def verify_password(plain_password: str, hashed_password: str) -> bool:

    return pwd_context.verify(plain_password, hashed_password)

# хэширование
def get_password_hash(password: str) -> str:

    return pwd_context.hash(password)

# создание токена
def create_access_token(data: dict[str, Any]) -> str:

    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(
        minutes=settings.access_token_expire_minutes
    )
    to_encode.update({"exp": expire, "iat": datetime.now(UTC)})
    encoded_jwt = jwt.encode(
        to_encode, settings.jwt_secret, algorithm=settings.jwt_alg
    )
    return encoded_jwt


def decode_token(token: str) -> dict[str, Any]:

    try:
        payload = jwt.decode(
            token, settings.jwt_secret, algorithms=[settings.jwt_alg]
        )
        return payload
    except JWTError as e:
        raise ValueError(f"Invalid token: {e}")