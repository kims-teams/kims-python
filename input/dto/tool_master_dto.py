from pydantic import BaseModel, Field
from typing import Optional

class ToolMasterDTO(BaseModel):
    id: Optional[int]
    toolId: Optional[str] = Field(alias="tool_id")
    toolType: Optional[str] = Field(alias="tool_type")
    toolName: Optional[str] = Field(alias="tool_name")
    siteId2: Optional[str] = Field(alias="site_id2")
    resourceId: Optional[int] = Field(alias="resource_id")

    class Config:
        populate_by_name = True
        from_attributes = True
