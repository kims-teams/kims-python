from pydantic import BaseModel, Field
from typing import Optional

class MaterialMasterDTO(BaseModel):
    id: Optional[int]
    partType: Optional[str] = Field(alias="part_type")
    partName: Optional[str] = Field(alias="part_name")
    uom: Optional[str]
    routingId: Optional[str] = Field(alias="routing_id")
    siteId2: Optional[str] = Field(alias="site_id2")
    partId: Optional[str] = Field(alias="part_id")
    bopId: Optional[int] = Field(alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
