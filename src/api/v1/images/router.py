from fastapi import APIRouter
from .service import ImageService
from .schemas import ImageCreate, ImageResponse

router = APIRouter()


@router.post("/", response_model=ImageResponse)
async def create_image(image: ImageCreate):
    return await ImageService.create_image(image)


@router.get("/", response_model=list[ImageResponse])
async def list_images():
    return await ImageService.list_images()


@router.get("/{image_id}", response_model=ImageResponse)
async def get_image(image_id: int):
    return await ImageService.get_image(image_id)


@router.delete("/{image_id}")
async def delete_image(image_id: int):
    return await ImageService.delete_image(image_id)
