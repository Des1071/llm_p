
from typing import List

from app.repositories.chat_messages import ChatMessageRepository
from app.schemas.chat import ChatMessageResponse
from app.services.openrouter_client import OpenRouterClient

# бизнес логика чата
class ChatUseCase:

    def __init__(
        self,
        chat_repository: ChatMessageRepository,
        openrouter_client: OpenRouterClient,
    ) -> None:
        self._chat_repo = chat_repository
        self._llm_client = openrouter_client

    async def ask(
        self,
        user_id: int,
        prompt: str,
        system: str | None = None,
        max_history: int = 10,
        temperature: float = 0.7,
    ) -> str:
        
        messages = []

        if system:
            messages.append({"role": "system", "content": system})

        history = \
            await self._chat_repo.get_recent_messages(user_id, max_history)
        for msg in history:
            messages.append({"role": msg.role, "content": msg.content})

        messages.append({"role": "user", "content": prompt})

        await self._chat_repo.add_message(user_id, "user", prompt)

        try:
            answer = \
                await self._llm_client.chat_completion(messages, temperature)
        except Exception:
            await self._chat_repo.add_message(
                user_id, "assistant", "[Error: Failed to get response]"
            )
            raise

        await self._chat_repo.add_message(user_id, "assistant", answer)

        return answer

    async def get_history(self, user_id: int) -> List[ChatMessageResponse]:
        messages = await self._chat_repo.get_all_messages(user_id)
        return [ChatMessageResponse.model_validate(msg) for msg in messages]

    async def clear_history(self, user_id: int) -> int:
        return await self._chat_repo.delete_all_messages(user_id)