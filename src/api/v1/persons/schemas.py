from pydantic import BaseModel, ConfigDict
from src.models.enums import PersonStatus

class PersonBase(BaseModel):
    full_name: str
    age: int | None = None
    last_seen_location: str | None = None
    last_seen_date: str | None = None
    status: PersonStatus

class PersonCreate(PersonBase):
    pass

class PersonResponse(PersonBase):
    id: int

    model_config = ConfigDict(
		from_attributes=True,
	)
