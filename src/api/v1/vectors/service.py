from fastapi import HTTPException
from core.dao.image_dao import ImageDAO
from src.core.dao.vector_dao import VectorDAO
from src.api.v1.vectors.schemas import VectorCreate, VectorResponse
from sqlalchemy.exc import IntegrityError


vector_dao = VectorDAO()

class VectorService:
    @staticmethod
    async def create_vector(vector_in: VectorCreate) -> VectorResponse:
        """Create a FAISS vector after verifying that the corresponding image exists."""

        image = await ImageDAO().get(vector_in.image_id) # type: ignore
        if not image:
            raise HTTPException(
                status_code=400,
                detail=f"Image with id {vector_in.image_id} does not exist"
            )

        try:
            vector = await VectorDAO().create(vector_in.model_dump()) # type: ignore
            return VectorResponse(**vector.__dict__)
        except IntegrityError as e:
            raise ValueError("Failed to insert vector. Ensure image_id exists.") from e


    @staticmethod
    async def get_vector(vector_id: int) -> VectorResponse:
        vector = await vector_dao.get(vector_id) # type: ignore
        if not vector:
            raise HTTPException(status_code=404, detail="Vector not found")
        return vector


    @staticmethod
    async def list_vectors():
        return await vector_dao.get_all() # type: ignore


    @staticmethod
    async def delete_vector(vector_id: int):
        success = await vector_dao.delete(vector_id) # type: ignore
        if not success:
            raise HTTPException(status_code=404, detail="Vector not found")
        return {"message": "Vector deleted"}
