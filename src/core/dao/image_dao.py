from .base_dao import BaseDAO
from src.models.image import Image

class ImageDAO(BaseDAO[Image]):
    """DAO for managing Image records."""
    def __init__(self):
        super().__init__(Image)
