from pydantic import BaseModel, Field
from typing import Optional

class ToolMasterDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    toolId: Optional[str] = Field(default=None, alias="tool_id")
    toolType: Optional[str] = Field(default=None, alias="tool_type")
    toolName: Optional[str] = Field(default=None, alias="tool_name")
    siteId2: Optional[str] = Field(default=None, alias="site_id2")
    resourceId: Optional[int] = Field(default=None, alias="resource_id")

    class Config:
        populate_by_name = True
        from_attributes = True
