from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY, FLOAT
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class FaissVector(Base):
    __tablename__ = "faiss_vectors" # type: ignore

    image_id: Mapped[int] = mapped_column(ForeignKey("images.id"), nullable=False)
    vector: Mapped[list[float]] = mapped_column(ARRAY(FLOAT), nullable=False)
