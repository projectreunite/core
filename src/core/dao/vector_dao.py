from .base_dao import BaseDAO
from src.models.vector import FaissVector

class VectorDAO(BaseDAO[FaissVector]):
    """DAO for managing FAISS Vector records."""
    def __init__(self):
        super().__init__(FaissVector)
