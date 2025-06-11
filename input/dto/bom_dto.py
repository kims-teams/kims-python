from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal

class BomDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    toSiteId: Optional[str] = Field(default=None, alias="to_site_id")
    toPartId: Optional[str] = Field(default=None, alias="to_part_id")
    bomCategory: Optional[str] = Field(default=None, alias="bom_category")
    outQty: Optional[Decimal] = Field(default=None, alias="out_qty")
    outUom: Optional[str] = Field(default=None, alias="out_uom")
    fromSiteId: Optional[str] = Field(default=None, alias="from_site_id")
    fromPartId: Optional[str] = Field(default=None, alias="from_part_id")
    inQty: Optional[Decimal] = Field(default=None, alias="in_qty")
    inUom: Optional[str] = Field(default=None, alias="in_uom")
    createDatetime: Optional[datetime] = Field(default=None, alias="create_datetime")
    effStartDate: Optional[datetime] = Field(default=None, alias="eff_start_date")
    createBy: Optional[str] = Field(default=None, alias="create_by")
    toPartName: Optional[str] = Field(default=None, alias="to_part_name")
    fromPartName: Optional[str] = Field(default=None, alias="from_part_name")
    zseq: Optional[Decimal] = Field(default=None)
    bomVersion: Optional[Decimal] = Field(default=None, alias="bom_version")
    fromPartLevel: Optional[Decimal] = Field(default=None, alias="from_part_level")
    toPartLevel: Optional[Decimal] = Field(default=None, alias="to_part_level")
    siteId2: Optional[str] = Field(default=None, alias="site_id2")
    bopId: Optional[int] = Field(default=None, alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
