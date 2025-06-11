from pydantic import BaseModel, Field
from typing import Optional

class MaterialMasterDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    partType: Optional[str] = Field(default=None, alias="part_type")
    partName: Optional[str] = Field(default=None, alias="part_name")
    uom: Optional[str] = Field(default=None)
    routingId: Optional[str] = Field(default=None, alias="routing_id")
    siteId2: Optional[str] = Field(default=None, alias="site_id2")
    partId: Optional[str] = Field(default=None, alias="part_id")
    bopId: Optional[int] = Field(default=None, alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
