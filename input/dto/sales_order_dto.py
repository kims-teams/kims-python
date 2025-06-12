from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class SalesOrderDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    demandId: Optional[str] = Field(default=None, alias="demand_id")
    partId: Optional[str] = Field(default=None, alias="part_id")
    partName: Optional[str] = Field(default=None, alias="part_name")
    dueDate: Optional[date] = Field(default=None, alias="due_date")
    demandQty: Optional[int] = Field(default=None, alias="demand_qty")  # ← int로 수정
    headerCreationDate: Optional[date] = Field(default=None, alias="header_creation_date")
    scenarioId: Optional[int] = Field(default=None, alias="scenario_id")
    targetId: Optional[int] = Field(default=None, alias="target_id")

    class Config:
        populate_by_name = True
        from_attributes = True
