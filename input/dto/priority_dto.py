from pydantic import BaseModel
from typing import Optional

class PriorityDTO(BaseModel):
    id: Optional[int]
    factorId: Optional[str]
    field: Optional[str]
    orderType: Optional[str]
    description: Optional[str]
    configId: Optional[int]  

    class Config:
        orm_mode = True
