from pydantic import BaseModel, Field
from typing import Optional

class OperationSequenceDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    operationId: Optional[str] = Field(default=None, alias="operation_id")
    operationSeq: Optional[int] = Field(default=None, alias="operation_seq")
    operationType: Optional[str] = Field(default=None, alias="operation_type")
    operationName: Optional[str] = Field(default=None, alias="operation_name")
    routingId: Optional[str] = Field(default=None, alias="routing_id")
    scenarioId: Optional[int] = Field(default=None, alias="scenario_id")
    bopId: Optional[int] = Field(default=None, alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
