from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class SalesOrderDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    demandId: Optional[str] = Field(default=None, alias="demand_id")
    partId: Optional[str] = Field(default=None, alias="part_id")
    partName: Optional[str] = Field(default=None, alias="part_name")
    customerId: Optional[int] = Field(default=None, alias="customer_id")
    dueDate: Optional[date] = Field(default=None, alias="due_date")
    demandQty: Optional[float] = Field(default=None, alias="demand_qty")
    uom: Optional[str] = Field(default=None)
    orderType: Optional[str] = Field(default=None, alias="order_type")
    orderTypeName: Optional[str] = Field(default=None, alias="order_type_name")
    headerCreationDate: Optional[date] = Field(default=None, alias="header_creation_date")
    siteId2: Optional[str] = Field(default=None, alias="site_id2")
    targetId: Optional[int] = Field(default=None, alias="target_id")

    class Config:
        populate_by_name = True
        from_attributes = True
