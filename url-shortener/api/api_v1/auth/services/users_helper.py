from abc import ABC, abstractmethod


class AbstractUsersHelper(ABC):
    """
    Что мне нужно от обертки:
    - получение пароля по юзернейму
    - совпадает ли пароль с переданным
    """

    @abstractmethod
    def get_user_password(
        self,
        username: str,
    ) -> str | None:
        """
        По переданному юзернейму находит пароль.

        Возвращает пароль если есть.

        :param username: - имя пользователя
        :return: пароль по пользователю, если найден
        """

    @classmethod
    def check_passwords_match(
        cls,
        password1: str,
        password2: str,
    ) -> bool:
        """
        Проверка паролей на совпадение.
        """
        return password1 == password2

    def validate_user_password(
        self,
        username: str,
        password: str,
    ) -> bool:
        """
        Проверить, валиден ли пароль.

        :param username: - чей пароль проверить
        :param password: - переданный пароль. Сверить с тем, что в БД
        :return: True если совпадают, иначе False
        """
        db_password = self.get_user_password(username)
        if db_password is None:
            return False
        return self.check_passwords_match(
            password1=db_password,
            password2=password,
        )
