from pydantic import BaseModel, Field
from typing import Optional

class ManufacturingProcessDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    routingId: Optional[str] = Field(default=None, alias="routing_id")
    routingType: Optional[str] = Field(default=None, alias="routing_type")
    routingName: Optional[str] = Field(default=None, alias="routing_name")
    scenarioId: Optional[str] = Field(default=None, alias="scenario_id")
    bopId: Optional[int] = Field(default=None, alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
