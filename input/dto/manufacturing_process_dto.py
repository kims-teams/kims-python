from pydantic import BaseModel, Field
from typing import Optional

class ManufacturingProcessDTO(BaseModel):
    id: Optional[int]
    routingId: str = Field(alias="routing_id")
    routingType: Optional[str] = Field(alias="routing_type")
    routingName: Optional[str] = Field(alias="routing_name")
    siteId: Optional[str] = Field(alias="site_id")
    bopId: Optional[int] = Field(alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
