from pydantic import BaseModel, Field
from typing import Optional
from typing import Union

class PriorityDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    priorityId: Optional[str] = Field(default=None, alias="priority_id")
    factorId: Union[str, int] = Field(default=None, alias="factor_id")
    sequence: Optional[int] = Field(default=None)
    description: Optional[str] = Field(default=None)
    scenarioId: Optional[int] = Field(default=None, alias="scenario_id")
    configId: Optional[int] = Field(default=None, alias="config_id")

    class Config:
        populate_by_name = True
        from_attributes = True
