from pydantic import BaseModel, ConfigDict
from typing import List

class VectorBase(BaseModel):
    image_id: int
    vector: List[float]

class VectorCreate(VectorBase):
    pass

class VectorResponse(VectorBase):
    id: int

    model_config = ConfigDict(
		from_attributes=True,
	)
