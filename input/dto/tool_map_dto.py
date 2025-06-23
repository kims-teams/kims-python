from pydantic import BaseModel, Field
from typing import Optional

class ToolMapDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    scenarioId: Optional[int] = Field(default=None, alias="scenario_id")
    partId: Optional[str] = Field(default=None, alias="part_id")
    toolId: Optional[str] = Field(default=None, alias="tool_id")
    partName: Optional[str] = Field(default=None, alias="part_name")
    resourceId: Optional[int] = Field(default=None, alias="resource_id")

    operationId: Optional[str] = Field(default=None, alias="operation_id")

    class Config:
        populate_by_name = True
        from_attributes = True
