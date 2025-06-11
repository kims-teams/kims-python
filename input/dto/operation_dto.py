from pydantic import BaseModel, Field
from typing import Optional

class OperationDTO(BaseModel):
    id: Optional[int]
    runTime: Optional[int] = Field(alias="run_time")
    runTimeUom: Optional[str] = Field(alias="run_time_uom")
    waitTimeUom: Optional[str] = Field(alias="wait_time_uom")
    transferTimeUom: Optional[str] = Field(alias="transfer_time_uom")
    sourcingType: Optional[str] = Field(alias="sourcing_type")
    operationId: Optional[str] = Field(alias="operation_id")
    operationName: Optional[str] = Field(alias="operation_name")
    operationType: Optional[str] = Field(alias="operation_type")
    operationSeq: Optional[int] = Field(alias="operation_seq")
    siteId2: Optional[str] = Field(alias="site_id2")
    bopId: Optional[int] = Field(alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
