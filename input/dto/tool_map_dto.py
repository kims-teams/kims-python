from pydantic import BaseModel, Field
from typing import Optional

class ToolMapDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    toolSize: Optional[int] = Field(default=None, alias="tool_size")
    partName: Optional[str] = Field(default=None, alias="part_name")
    toolId: Optional[str] = Field(default=None, alias="tool_id")
    siteId: Optional[str] = Field(default=None, alias="site_id")
    portId: Optional[str] = Field(default=None, alias="port_id")
    resourceId: Optional[int] = Field(default=None, alias="resource_id")

    class Config:
        populate_by_name = True
        from_attributes = True
