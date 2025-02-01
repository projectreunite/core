from sqlalchemy import String, Integer, Enum

from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from .enums import PersonStatus


class Person(Base):
    __tablename__ = "persons" # type: ignore

    full_name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=True)
    last_seen_location: Mapped[str] = mapped_column(String, nullable=True)
    last_seen_date: Mapped[str] = mapped_column(String, nullable=True)    
    status: Mapped[PersonStatus] = mapped_column(Enum(PersonStatus), nullable=False)

