from pydantic import BaseModel, Field
from typing import Optional

class ConfigDTO(BaseModel):
    id: int
    inputDataId: Optional[int] = Field(alias="input_data_id")

    class Config:
        populate_by_name = True
        from_attributes = True
