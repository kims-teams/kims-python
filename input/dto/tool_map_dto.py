from pydantic import BaseModel
from typing import Optional

class ToolMapDTO(BaseModel):
    id: Optional[int]
    toolSize: Optional[int]
    partName: Optional[str]
    toolId: Optional[str]
    siteId: Optional[str]
    portId: Optional[str]
    resourceId: Optional[int]

    class Config:
        orm_mode = True
