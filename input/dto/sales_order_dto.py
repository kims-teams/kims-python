from pydantic import BaseModel
from typing import Optional
from datetime import date

class SalesOrderDTO(BaseModel):
    id: Optional[int]
    demandId: Optional[str]
    partId: Optional[str]
    partName: Optional[str]
    customerId: Optional[int]
    dueDate: Optional[date]
    demandQty: Optional[float]
    uom: Optional[str]
    orderType: Optional[str]
    orderTypeName: Optional[str]
    headerCreationDate: Optional[date]
    siteId2: Optional[str]
    targetId: Optional[int]

    class Config:
        orm_mode = True
