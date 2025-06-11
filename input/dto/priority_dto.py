from pydantic import BaseModel, Field
from typing import Optional

class PriorityDTO(BaseModel):
    id: Optional[int]
    factorId: Optional[str] = Field(alias="factor_id")
    field: Optional[str]
    orderType: Optional[str] = Field(alias="order_type")
    description: Optional[str]
    configId: Optional[int] = Field(alias="config_id")

    class Config:
        populate_by_name = True
        from_attributes = True
