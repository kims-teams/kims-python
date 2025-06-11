from pydantic import BaseModel, Field
from typing import Optional

class ToolMapDTO(BaseModel):
    id: Optional[int]
    toolSize: Optional[int] = Field(alias="tool_size")
    partName: Optional[str] = Field(alias="part_name")
    toolId: Optional[str] = Field(alias="tool_id")
    siteId: Optional[str] = Field(alias="site_id")
    portId: Optional[str] = Field(alias="port_id")
    resourceId: Optional[int] = Field(alias="resource_id")

    class Config:
        populate_by_name = True
        from_attributes = True
