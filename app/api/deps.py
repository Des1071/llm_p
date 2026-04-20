
from typing import AsyncGenerator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import decode_token
from app.db.session import AsyncSessionLocal
from app.repositories.chat_messages import ChatMessageRepository
from app.repositories.users import UserRepository
from app.services.openrouter_client import OpenRouterClient
from app.usecases.auth import AuthUseCase
from app.usecases.chat import ChatUseCase

# настройка OAuth2 для Swagger UI
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# создание сессии
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

# получение пользовательского репозитория
async def get_user_repository(
    session: AsyncSession = Depends(get_session),
) -> UserRepository:
    return UserRepository(session)

# получения репозитория
async def get_chat_repository(
    session: AsyncSession = Depends(get_session),
) -> ChatMessageRepository:
    return ChatMessageRepository(session)

# получение клиента
def get_openrouter_client() -> OpenRouterClient:
    """Get OpenRouter client."""
    return OpenRouterClient()

#аутентификация
async def get_auth_usecase(
    user_repo: UserRepository = Depends(get_user_repository),
) -> AuthUseCase:
    """Get authentication use case."""
    return AuthUseCase(user_repo)

# Чат юсре кейс
async def get_chat_usecase(
    chat_repo: ChatMessageRepository = Depends(get_chat_repository),
    llm_client: OpenRouterClient = Depends(get_openrouter_client),
) -> ChatUseCase:
    return ChatUseCase(chat_repo, llm_client)

# текущий ИД токена
async def get_current_user_id(
    token: str = Depends(oauth2_scheme),
) -> int:
    try:
        payload = decode_token(token)
        user_id = int(payload.get("sub", ""))
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user_id
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )