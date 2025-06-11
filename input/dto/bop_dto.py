from pydantic import BaseModel, Field
from typing import Optional

class BopDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    inputDataId: Optional[int] = Field(default=None, alias="input_data_id")

    class Config:
        populate_by_name = True
        from_attributes = True
