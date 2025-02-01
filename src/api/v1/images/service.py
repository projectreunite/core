from fastapi import HTTPException
from src.core.dao.image_dao import ImageDAO
from .schemas import ImageCreate, ImageResponse
from loguru import logger

image_dao = ImageDAO()

class ImageService():
    @staticmethod
    async def create_image(image_data: ImageCreate) -> ImageResponse:
        return await image_dao.create(image_data.model_dump()) # type: ignore

    @staticmethod
    async def get_image(image_id: int) -> ImageResponse:
        image = await image_dao.get(image_id) # type: ignore
        if not image:
            raise HTTPException(status_code=404, detail="Image not found")
        return image

    @staticmethod
    async def list_images():
        return await image_dao.get_all() # type: ignore

    @staticmethod
    async def delete_image(image_id: int):
        success = await image_dao.delete(image_id) # type: ignore
        if not success:
            raise HTTPException(status_code=404, detail="Image not found")
        return {"message": "Image deleted"}
