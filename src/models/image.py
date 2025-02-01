from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Image(Base):
    __tablename__ = "images" # type: ignore

    person_id: Mapped[int] = mapped_column(ForeignKey("persons.id"), nullable=True)
    image_url: Mapped[str] = mapped_column(String, nullable=False)
    vector_id: Mapped[int] = mapped_column(nullable=True)  # If using FAISS
