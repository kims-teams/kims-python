from pydantic import BaseModel, Field
from typing import Optional

class PlantMasterDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    siteId: Optional[int] = Field(default=None, alias="site_id")
    siteName: Optional[str] = Field(default=None, alias="site_name")
    scenarioId: Optional[int] = Field(default=None, alias="scenario_id")
    bopId: Optional[int] = Field(default=None, alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
