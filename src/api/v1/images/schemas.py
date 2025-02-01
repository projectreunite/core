from pydantic import BaseModel, ConfigDict

class ImageBase(BaseModel):
    person_id: int | None = None

class ImageCreate(ImageBase):
    image_url: str


class ImageResponse(ImageBase):
    id: int
    image_url: str

    model_config = ConfigDict(
		from_attributes=True,
	)
