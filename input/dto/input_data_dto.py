from pydantic import BaseModel
from typing import Optional

class InputDataDTO(BaseModel):
    id: int
    scenarioId: Optional[int] 

    class Config:
        orm_mode = True
