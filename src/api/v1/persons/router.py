from fastapi import APIRouter
from src.api.v1.persons.service import PersonService
from src.api.v1.persons.schemas import PersonCreate, PersonResponse

router = APIRouter()


@router.post("/", response_model=PersonResponse)
async def create_person(person: PersonCreate):
    return await PersonService.create_person(person)


@router.get("/", response_model=list[PersonResponse])
async def list_persons():
    return await PersonService.list_persons()


@router.get("/{person_id}", response_model=PersonResponse)
async def get_person(person_id: int):
    return await PersonService.get_person(person_id)


@router.delete("/{person_id}")
async def delete_person(person_id: int):
    return await PersonService.delete_person(person_id)

