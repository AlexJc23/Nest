import os
from functools import lru_cache

class Settings:
    ENV: str = os.getenv("ENV", "development")

    @property
    def cors_origins(self) -> list[str]:
        if self.ENV == "development":
            return [
                "http://localhost:8081",
                "http://10.0.0.92:8081",
            ]
        if self.ENV == "production":
            return [
                "https://<production-domain-here.com"
            ]
@lru_cache
def get_settings() -> Settings:
    return Settings()
