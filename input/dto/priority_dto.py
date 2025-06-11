from pydantic import BaseModel, Field
from typing import Optional

class PriorityDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    factorId: Optional[str] = Field(default=None, alias="factor_id")
    field: Optional[str] = Field(default=None)
    orderType: Optional[str] = Field(default=None, alias="order_type")
    description: Optional[str] = Field(default=None)
    configId: Optional[int] = Field(default=None, alias="config_id")

    class Config:
        populate_by_name = True
        from_attributes = True
