from pydantic import BaseModel, Field
from typing import Optional

class ToolMasterDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    toolId: Optional[str] = Field(default=None, alias="tool_id")
    toolState: Optional[bool] = Field(default=None, alias="tool_state")
    scenarioId: Optional[int] = Field(default=None, alias="scenario_id")
    toolName: Optional[str] = Field(default=None, alias="tool_name")
    resourceId: Optional[int] = Field(default=None, alias="resource_id")

    class Config:
        populate_by_name = True
        from_attributes = True
