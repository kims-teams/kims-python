from pydantic import BaseModel
from typing import Optional

class MaterialMasterDTO(BaseModel):
    id: Optional[int]
    partType: Optional[str]
    partName: Optional[str]
    uom: Optional[str]
    routingId: Optional[str]
    siteId2: Optional[str]
    partId: Optional[str]
    bopId: Optional[int]

    class Config:
        orm_mode = True
