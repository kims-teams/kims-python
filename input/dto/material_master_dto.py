from pydantic import BaseModel, Field
from typing import Optional

class MaterialMasterDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    partId: Optional[str] = Field(default=None, alias="part_id")
    partType: Optional[str] = Field(default=None, alias="part_type")
    routingId: Optional[str] = Field(default=None, alias="routing_id")
    partName: Optional[str] = Field(default=None, alias="part_name")
    scenarioId: Optional[int] = Field(default=None, alias="scenario_id")
    bopId: Optional[int] = Field(default=None, alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
