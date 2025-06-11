from pydantic import BaseModel
from typing import Optional

class ToolMasterDTO(BaseModel):
    id: Optional[int]
    toolId: Optional[str]
    toolType: Optional[str]
    toolName: Optional[str]
    siteId2: Optional[str]
    resourceId: Optional[int]

    class Config:
        orm_mode = True
