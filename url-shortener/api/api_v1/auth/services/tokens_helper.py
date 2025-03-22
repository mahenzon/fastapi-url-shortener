import secrets
from abc import ABC, abstractmethod


class AbstractTokensHelper(ABC):
    """
    Что мне нужно от обертки:
    - проверять на наличие токена
    - добавлять токен в хранилище
    - сгенерировать и добавить токены
    """

    @abstractmethod
    def token_exists(
        self,
        token: str,
    ) -> bool:
        """
        Check if token exists.

        :param token:
        :return:
        """

    @abstractmethod
    def add_token(
        self,
        token: str,
    ) -> None:
        """
        Save token in storage.

        :param token:
        :return:
        """

    @abstractmethod
    def get_tokens(self) -> list[str]:
        """
        Get all tokens.

        :return:
        """

    @classmethod
    def generate_token(cls) -> str:
        return secrets.token_urlsafe(16)

    def generate_and_save_token(self) -> str:
        token = self.generate_token()
        self.add_token(token)
        return token
