from pydantic import BaseModel
from typing import Optional

class ResourceDTO(BaseModel):
    id: int
    inputDataId: Optional[int]  

    class Config:
        orm_mode = True
