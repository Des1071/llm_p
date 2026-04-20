# база
class AppError(Exception):

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)

# конфликт 
class ConflictError(AppError):
    pass

# авторизация
class UnauthorizedError(AppError):

    pass

# доступ
class ForbiddenError(AppError):

    pass

# не найден ресурс
class NotFoundError(AppError):

    pass

# ошибка обращения
class ExternalServiceError(AppError):

    pass