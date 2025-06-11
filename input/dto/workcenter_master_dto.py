from pydantic import BaseModel, Field
from typing import Optional

class WorkcenterMasterDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    workcenterId: Optional[str] = Field(default=None, alias="workcenter_id")
    workcenterName: Optional[str] = Field(default=None, alias="workcenter_name")
    workcenterGroup: Optional[str] = Field(default=None, alias="workcenter_group")
    workcenterType: Optional[str] = Field(default=None, alias="workcenter_type")
    dispatcherType: Optional[str] = Field(default=None, alias="dispatcher_type")
    workcenterState: Optional[str] = Field(default=None, alias="workcenter_state")
    automation: Optional[str] = Field(default=None)
    siteId: Optional[str] = Field(default=None, alias="site_id")
    factorId: Optional[str] = Field(default=None, alias="factor_id")
    resourceId: Optional[int] = Field(default=None, alias="resource_id")

    class Config:
        populate_by_name = True
        from_attributes = True
