
from app.core.errors import ConflictError, NotFoundError, UnauthorizedError
from app.core.security import create_access_token, get_password_hash, verify_password
from app.repositories.users import UserRepository
from app.schemas.user import UserPublic


class AuthUseCase:

    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repo = user_repository

    async def register(self, email: str, password: str) -> UserPublic:

        existing_user = await self._user_repo.get_by_email(email)
        if existing_user:
            raise ConflictError("User with this email already exists")

        password_hash = get_password_hash(password)
        user = await self._user_repo.create(email, password_hash)

        return UserPublic.model_validate(user)
# определение пользователя и возрат токена
    async def login(self, email: str, password: str) -> str:
        user = await self._user_repo.get_by_email(email)
        if not user:
            raise UnauthorizedError("Invalid email or password")

        if not verify_password(password, user.password_hash):
            raise UnauthorizedError("Invalid email or password")

        token_data = {"sub": str(user.id), "role": user.role}
        return create_access_token(token_data)

    async def get_profile(self, user_id: int) -> UserPublic:
        
        user = await self._user_repo.get_by_id(user_id)
        if not user:
            raise NotFoundError("User not found")

        return UserPublic.model_validate(user)