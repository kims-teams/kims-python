from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class TimeUom(str, Enum):
    SEC = "SEC"
    MIN = "MIN"
    HOUR = "HOUR"

class WorkcenterMapDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    routingId: Optional[str] = Field(default=None, alias="routing_id")
    partId: Optional[str] = Field(default=None, alias="part_id")
    operationId: Optional[str] = Field(default=None, alias="operation_id")
    routingGroup: Optional[str] = Field(default=None, alias="routing_group")
    workcenterId: Optional[str] = Field(default=None, alias="workcenter_id")
    tactTime: Optional[float] = Field(default=None, alias="tact_time")
    tactTimeUom: Optional[TimeUom] = Field(default=None, alias="tact_time_uom")
    scenarioId: Optional[int] = Field(default=None, alias="scenario_id")
    resourceId: Optional[int] = Field(default=None, alias="resource_id")

    class Config:
        populate_by_name = True
        from_attributes = True
