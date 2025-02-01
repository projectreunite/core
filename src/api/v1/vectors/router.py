from fastapi import APIRouter
from .service import VectorService

from .schemas import VectorCreate, VectorResponse

router = APIRouter()


@router.post("/", response_model=VectorResponse)
async def create_vector(vector: VectorCreate):
    return await VectorService.create_vector(vector)


@router.get("/", response_model=list[VectorResponse])
async def list_vectors():
    return await VectorService.list_vectors()


@router.get("/{vector_id}", response_model=VectorResponse)
async def get_vector(vector_id: int):
    return await VectorService.get_vector(vector_id)


@router.delete("/{vector_id}")
async def delete_vector(vector_id: int):
    return await VectorService.delete_vector(vector_id)
