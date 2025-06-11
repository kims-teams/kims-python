from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class SalesOrderDTO(BaseModel):
    id: Optional[int]
    demandId: Optional[str] = Field(alias="demand_id")
    partId: Optional[str] = Field(alias="part_id")
    partName: Optional[str] = Field(alias="part_name")
    customerId: Optional[int] = Field(alias="customer_id")
    dueDate: Optional[date] = Field(alias="due_date")
    demandQty: Optional[float] = Field(alias="demand_qty")
    uom: Optional[str]
    orderType: Optional[str] = Field(alias="order_type")
    orderTypeName: Optional[str] = Field(alias="order_type_name")
    headerCreationDate: Optional[date] = Field(alias="header_creation_date")
    siteId2: Optional[str] = Field(alias="site_id2")
    targetId: Optional[int] = Field(alias="target_id")

    class Config:
        populate_by_name = True
        from_attributes = True
