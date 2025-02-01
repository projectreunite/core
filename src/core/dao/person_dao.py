from .base_dao import BaseDAO
from src.models.person import Person

class PersonDAO(BaseDAO[Person]):
    """DAO for managing Person records."""
    def __init__(self):
        super().__init__(Person)
