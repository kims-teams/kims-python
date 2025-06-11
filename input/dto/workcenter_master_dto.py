from pydantic import BaseModel, Field
from typing import Optional

class WorkcenterMasterDTO(BaseModel):
    id: Optional[int]
    workcenterId: Optional[str] = Field(alias="workcenter_id")
    workcenterName: Optional[str] = Field(alias="workcenter_name")
    workcenterGroup: Optional[str] = Field(alias="workcenter_group")
    workcenterType: Optional[str] = Field(alias="workcenter_type")
    dispatcherType: Optional[str] = Field(alias="dispatcher_type")
    workcenterState: Optional[str] = Field(alias="workcenter_state")
    automation: Optional[str]
    siteId: Optional[str] = Field(alias="site_id")
    factorId: Optional[str] = Field(alias="factor_id")
    resourceId: Optional[int] = Field(alias="resource_id")

    class Config:
        populate_by_name = True
        from_attributes = True
