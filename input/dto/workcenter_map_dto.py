from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class TimeUom(str, Enum):
    SEC = "SEC"
    MIN = "MIN"
    HOUR = "HOUR"

class WorkcenterMapDTO(BaseModel):
    id: Optional[int]
    partId: Optional[str] = Field(alias="part_id")
    operationId: Optional[str] = Field(alias="operation_id")
    routingGroup: Optional[str] = Field(alias="routing_group")
    routingVersion: Optional[int] = Field(alias="routing_version")
    tactTime: Optional[float] = Field(alias="tact_time")
    tactTimeUom: Optional[TimeUom] = Field(alias="tact_time_uom")
    procTime: Optional[float] = Field(alias="proc_time")
    procTimeUom: Optional[TimeUom] = Field(alias="proc_time_uom")
    routingId: Optional[str] = Field(alias="routing_id")
    workcenterId: Optional[str] = Field(alias="workcenter_id")
    siteId: Optional[str] = Field(alias="site_id")
    resourceId: Optional[int] = Field(alias="resource_id")

    class Config:
        populate_by_name = True
        from_attributes = True
