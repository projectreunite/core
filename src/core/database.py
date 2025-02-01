import uuid
from collections.abc import AsyncGenerator, Awaitable, Callable
from functools import wraps
from typing import Any, TypeVar, cast

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from .config.settings import settings

F = TypeVar("F", bound=Callable[..., Awaitable[Any]])

class Database:
	def __init__(self) -> None:
		self.engine = create_async_engine(
			settings.DATABASE_URL,
			future=True,
			connect_args={
				"prepared_statement_name_func": lambda: f"__asyncpg_{uuid.uuid4()}__",
				"statement_cache_size": 100,
				"prepared_statement_cache_size": 100,
			},
			pool_pre_ping=True,
		)
		self.session_factory = async_sessionmaker(
			bind=self.engine,
			expire_on_commit=False,
			autocommit=False,
			autoflush=False,
			class_=AsyncSession,
		)

	async def get_db(self) -> AsyncGenerator[AsyncSession, None]:
		async with self.session_factory() as session:
			try:
				yield session
				await session.commit()
			except Exception:
				await session.rollback()
				raise


database = Database()


def inject_session(func: F) -> F:
	@wraps(func)
	async def wrapper(*args: tuple[Any], **kwargs: dict[str, Any]) -> F:
		async with database.session_factory() as session:
			if "session" in kwargs:
				msg = "Session argument already provided"
				raise ValueError(msg)
			kwargs["session"] = session  # type: ignore
			return await func(*args, **kwargs)

	return cast(F, wrapper)


__all__ = [
    # add models here
]
