from pydantic import BaseModel
from typing import Optional

class WorkcenterMasterDTO(BaseModel):
    id: Optional[int]
    workcenterId: Optional[str]
    workcenterName: Optional[str]
    workcenterGroup: Optional[str]
    workcenterType: Optional[str]
    dispatcherType: Optional[str]
    workcenterState: Optional[str]
    automation: Optional[str]
    siteId: Optional[str]
    factorId: Optional[str]
    resourceId: Optional[int]

    class Config:
        orm_mode = True
