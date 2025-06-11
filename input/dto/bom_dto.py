from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class BomDTO(BaseModel):
    id: Optional[int]
    toSiteId: Optional[str]
    toPartId: Optional[str]
    bomCategory: Optional[str]
    outQty: Optional[Decimal]
    outUom: Optional[str]
    fromSiteId: Optional[str]
    fromPartId: Optional[str]
    inQty: Optional[Decimal]
    inUom: Optional[str]
    createDatetime: Optional[datetime]
    effStartDate: Optional[datetime]
    createBy: Optional[str]
    toPartName: Optional[str]
    fromPartName: Optional[str]
    zseq: Optional[Decimal]
    bomVersion: Optional[Decimal]
    fromPartLevel: Optional[Decimal]
    toPartLevel: Optional[Decimal]
    siteId2: Optional[str]
    bopId: Optional[int]

    class Config:
        orm_mode = True
