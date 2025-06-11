from pydantic import BaseModel, Field
from typing import Optional

class OperationDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    runTime: Optional[int] = Field(default=None, alias="run_time")
    runTimeUom: Optional[str] = Field(default=None, alias="run_time_uom")
    waitTimeUom: Optional[str] = Field(default=None, alias="wait_time_uom")
    transferTimeUom: Optional[str] = Field(default=None, alias="transfer_time_uom")
    sourcingType: Optional[str] = Field(default=None, alias="sourcing_type")
    operationId: Optional[str] = Field(default=None, alias="operation_id")
    operationName: Optional[str] = Field(default=None, alias="operation_name")
    operationType: Optional[str] = Field(default=None, alias="operation_type")
    operationSeq: Optional[int] = Field(default=None, alias="operation_seq")
    siteId2: Optional[str] = Field(default=None, alias="site_id2")
    bopId: Optional[int] = Field(default=None, alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
