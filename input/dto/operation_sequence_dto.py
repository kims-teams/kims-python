from pydantic import BaseModel, Field
from typing import Optional

class OperationSequenceDTO(BaseModel):
    id: Optional[int]
    operationId: Optional[str] = Field(alias="operation_id")
    operationSeq: Optional[int] = Field(alias="operation_seq")
    operationType: Optional[str] = Field(alias="operation_type")
    operationName: Optional[str] = Field(alias="operation_name")
    routingId: Optional[str] = Field(alias="routing_id")
    siteId: Optional[str] = Field(alias="site_id")
    bopId: Optional[int] = Field(alias="bop_id")

    class Config:
        populate_by_name = True
        from_attributes = True
