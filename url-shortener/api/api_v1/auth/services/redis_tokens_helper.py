from redis import Redis

from api.api_v1.auth.services.tokens_helper import AbstractTokensHelper
from core import config


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
            )
        )

    def add_token(self, token: str) -> None:
        self.redis.sadd(self.tokens_set, token)


redis_tokens = RedisTokensHelper(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_TOKENS,
    tokens_set_name=config.REDIS_TOKENS_SET_NAME,
)
