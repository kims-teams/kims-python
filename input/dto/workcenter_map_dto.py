from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TimeUom(str, Enum):
    SEC = "SEC"
    MIN = "MIN"
    HOUR = "HOUR"

class WorkcenterMapDTO(BaseModel):
    id: Optional[int]
    partId: Optional[str]
    operationId: Optional[str]
    routingGroup: Optional[str]
    routingVersion: Optional[int]
    tactTime: Optional[float]
    tactTimeUom: Optional[TimeUom]
    procTime: Optional[float]
    procTimeUom: Optional[TimeUom]
    routingId: Optional[str]
    workcenterId: Optional[str]
    siteId: Optional[str]
    resourceId: Optional[int]

    class Config:
        orm_mode = True
