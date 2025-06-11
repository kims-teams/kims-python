from pydantic import BaseModel, Field
from typing import Optional

class InputDataDTO(BaseModel):
    id: int
    scenarioId: Optional[int] = Field(alias="scenario_id")

    class Config:
        populate_by_name = True
        from_attributes = True
