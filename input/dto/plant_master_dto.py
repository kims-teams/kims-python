from pydantic import BaseModel, Field
from typing import Optional

class PlantMasterDTO(BaseModel):
    id: Optional[int]
    siteId: Optional[str] = Field(alias="site_id")
    siteName: Optional[str] = Field(alias="site_name")
    bopId: Optional[int] = Field(alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
