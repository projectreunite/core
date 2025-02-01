from datetime import datetime

from sqlalchemy import UUID, DateTime, Integer, func
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
	__abstract__ = True

	@declared_attr  # type: ignore
	def __tablename__(cls) -> str:  # type: ignore # noqa
		return cls.__name__.lower()  # type: ignore

	id: Mapped[UUID] = mapped_column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
	created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
	updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
