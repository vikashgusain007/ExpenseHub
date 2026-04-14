import logging
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from database import engine
from app.api.v1 import api_router

logger = logging.getLogger("expensehub")


@asynccontextmanager
async def lifespan(_: FastAPI):
    """
    Validate database connectivity at startup and ensure clean disposal
    on shutdown.
    """
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logger.info("Database connectivity check passed.")
    except SQLAlchemyError:
        logger.exception("Database connectivity check failed.")
        raise

    yield

    engine.dispose()
    logger.info("Database engine disposed.")


def create_app() -> FastAPI:
    app = FastAPI(
        title="ExpenseHub",
        lifespan=lifespan,
    )
    app.include_router(api_router)

    @app.get("/health", tags=["health"])
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
