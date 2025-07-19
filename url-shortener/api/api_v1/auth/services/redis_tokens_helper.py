__all__ = ("redis_tokens",)

from typing import cast

from redis import Redis

from api.api_v1.auth.services.tokens_helper import AbstractTokensHelper
from core.config import settings


class RedisTokensHelper(AbstractTokensHelper):
    def __init__(
        self,
        host: str,
        port: int,
        db: int,
        tokens_set_name: str,
    ) -> None:
        self.redis = Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True,
        )
        self.tokens_set = tokens_set_name

    def token_exists(self, token: str) -> bool:
        return bool(
            self.redis.sismember(
                self.tokens_set,
                token,
            ),
        )

    def add_token(self, token: str) -> None:
        self.redis.sadd(self.tokens_set, token)

    def get_tokens(self) -> list[str]:
        return list(cast(set[str], self.redis.smembers(self.tokens_set)))

    def delete_token(self, token: str) -> None:
        self.redis.srem(self.tokens_set, token)


redis_tokens = RedisTokensHelper(
    host=settings.redis.connection.host,
    port=settings.redis.connection.port,
    db=settings.redis.db.tokens,
    tokens_set_name=settings.redis.collections_names.tokens_set,
)
