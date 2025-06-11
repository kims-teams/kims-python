from pydantic import BaseModel, Field
from typing import Optional

class InputDataDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    scenarioId: Optional[int] = Field(default=None, alias="scenario_id")

    class Config:
        populate_by_name = True
        from_attributes = True
