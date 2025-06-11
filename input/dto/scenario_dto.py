from pydantic import BaseModel, Field
from typing import Optional

class ScenarioDTO(BaseModel):
    id: Optional[str] = Field(default=None)

    class Config:
        populate_by_name = True
        from_attributes = True
