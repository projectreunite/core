from typing import List
from fastapi import HTTPException
from src.core.dao.person_dao import PersonDAO
from .schemas import PersonCreate, PersonResponse

person_dao = PersonDAO()

class PersonService:
    @staticmethod
    async def create_person(person_data: PersonCreate) -> PersonResponse:
        new_person = await person_dao.create(person_data.model_dump()) # type: ignore
        return new_person


    @staticmethod
    async def get_person(person_id: int) -> PersonResponse:
        person = await person_dao.get(person_id) # type: ignore
        if not person:
            raise HTTPException(status_code=404, detail="Person not found")
        return person

    @staticmethod
    async def list_persons() -> List[PersonResponse]:
        return await person_dao.get_all() # type: ignore

    @staticmethod
    async def delete_person(person_id: int):
        success = await person_dao.delete(person_id) # type: ignore
        if not success:
            raise HTTPException(status_code=404, detail="Person not found")
        return {"message": "Person deleted"}
