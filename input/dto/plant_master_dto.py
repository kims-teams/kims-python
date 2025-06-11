from pydantic import BaseModel
from typing import Optional

class PlantMasterDTO(BaseModel):
    id: Optional[int]
    siteId: Optional[str]
    siteName: Optional[str]
    bopId: Optional[int] 

    class Config:
        orm_mode = True
