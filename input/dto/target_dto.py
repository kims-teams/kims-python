from pydantic import BaseModel
from typing import Optional

class TargetDTO(BaseModel):
    id: int
    inputDataId: Optional[int]

    class Config:
        orm_mode = True
