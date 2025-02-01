from collections.abc import Sequence
from typing import Any

from annotated_types import T
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import inject_session


class BaseDAO[T]:
    def __init__(self, model: type[T]):
        self.model = model
  

    @inject_session
    async def create(self, obj_in: dict[str, Any], session: AsyncSession) -> T:
        db_obj = self.model(**obj_in)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    @inject_session
    async def get(self, unique_id: int, session: AsyncSession, user_id: int | None = None) -> T | None:
        statement = select(self.model).where(self.model.id == unique_id)  # type: ignore
        if user_id is not None:
            statement = statement.where(self.model.user_id == user_id)  # type: ignore

        result = await session.execute(statement)
        return result.scalars().first()

    @inject_session
    async def get_all(
        self,
        session: AsyncSession,
        user_id: int | None = None,
        skip: int = 0,
        limit: int | None = None,
    ) -> Sequence[T]:
        statement = select(self.model).offset(skip)
        if limit is not None:
            statement = statement.limit(limit)
        if user_id is not None:
            statement = statement.where(self.model.user_id == user_id)  # type: ignore

        result = await session.execute(statement)
        return result.scalars().all()

    @inject_session
    async def update(self, unique_id: int, obj_in: dict[str, Any], session: AsyncSession) -> T | None:
        statement = update(self.model).where(self.model.id == unique_id).values(**obj_in).returning(self.model)  # type: ignore
        result = await session.execute(statement)
        await session.commit()
        return result.scalars().first()

    @inject_session
    async def delete(self, unique_id: int, session: AsyncSession) -> bool:
        statement = delete(self.model).where(self.model.id == unique_id)  # type: ignore
        result = await session.execute(statement)
        await session.commit()
        return result.rowcount > 0  # type: ignore