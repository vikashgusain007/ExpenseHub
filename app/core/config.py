import os


class Settings:
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./expensehub.db")


settings = Settings()
