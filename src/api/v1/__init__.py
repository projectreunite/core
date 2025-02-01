from fastapi import APIRouter
from .persons.router import router as persons_router
from .images.router import router as images_router
from .vectors.router import router as vectors_router

api_router = APIRouter()

api_router.include_router(persons_router, prefix="/persons", tags=["Persons"])
api_router.include_router(images_router, prefix="/images", tags=["Images"])
api_router.include_router(vectors_router, prefix="/vectors", tags=["Vectors"])
