from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal

class BomDTO(BaseModel):
    id: Optional[int]
    toSiteId: Optional[str] = Field(alias="to_site_id")
    toPartId: Optional[str] = Field(alias="to_part_id")
    bomCategory: Optional[str] = Field(alias="bom_category")
    outQty: Optional[Decimal] = Field(alias="out_qty")
    outUom: Optional[str] = Field(alias="out_uom")
    fromSiteId: Optional[str] = Field(alias="from_site_id")
    fromPartId: Optional[str] = Field(alias="from_part_id")
    inQty: Optional[Decimal] = Field(alias="in_qty")
    inUom: Optional[str] = Field(alias="in_uom")
    createDatetime: Optional[datetime] = Field(alias="create_datetime")
    effStartDate: Optional[datetime] = Field(alias="eff_start_date")
    createBy: Optional[str] = Field(alias="create_by")
    toPartName: Optional[str] = Field(alias="to_part_name")
    fromPartName: Optional[str] = Field(alias="from_part_name")
    zseq: Optional[Decimal]
    bomVersion: Optional[Decimal] = Field(alias="bom_version")
    fromPartLevel: Optional[Decimal] = Field(alias="from_part_level")
    toPartLevel: Optional[Decimal] = Field(alias="to_part_level")
    siteId2: Optional[str] = Field(alias="site_id2")
    bopId: Optional[int] = Field(alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
