from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal

class BomDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    toPartId: Optional[str] = Field(default=None, alias="to_part_id")
    operationId: Optional[str] = Field(default=None, alias="operation_id")
    outQty: Optional[Decimal] = Field(default=None, alias="out_qty")
    outUom: Optional[str] = Field(default=None, alias="out_uom")
    fromPartId: Optional[str] = Field(default=None, alias="from_part_id")
    inQty: Optional[Decimal] = Field(default=None, alias="in_qty")
    inUom: Optional[str] = Field(default=None, alias="in_uom")
    toPartName: Optional[str] = Field(default=None, alias="to_part_name")
    fromPartName: Optional[str] = Field(default=None, alias="from_part_name")
    zseq: Optional[Decimal] = Field(default=None)
    scenarioId: Optional[int] = Field(default=None, alias="scenario_id")
    fromPartLevel: Optional[Decimal] = Field(default=None, alias="from_part_level")
    toPartLevel: Optional[Decimal] = Field(default=None, alias="to_part_level")
    bopId: Optional[int] = Field(default=None, alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
