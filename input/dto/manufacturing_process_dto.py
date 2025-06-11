from pydantic import BaseModel
from typing import Optional

class ManufacturingProcessDTO(BaseModel):
    id: Optional[int]
    routingId: str
    routingType: Optional[str]
    routingName: Optional[str]
    siteId: Optional[str]
    bopId: Optional[int]

    class Config:
        orm_mode = True
