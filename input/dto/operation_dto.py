from pydantic import BaseModel, Field
from typing import Optional

class OperationDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    operationId: Optional[str] = Field(default=None, alias="operation_id")
    operationName: Optional[str] = Field(default=None, alias="operation_name")
    runTime: Optional[int] = Field(default=None, alias="run_time")
    runTimeUom: Optional[str] = Field(default=None, alias="run_time_uom")
    operationSeq: Optional[int] = Field(default=None, alias="operation_seq")
    operationType: Optional[str] = Field(default=None, alias="operation_type")
    sourcingType: Optional[str] = Field(default=None, alias="sourcing_type")
    scenarioId: Optional[int] = Field(default=None, alias="scenario_id")
    bopId: Optional[int] = Field(default=None, alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
