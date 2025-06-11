from pydantic import BaseModel
from typing import Optional

class OperationSequenceDTO(BaseModel):
    id: Optional[int]
    operationId: Optional[str]
    operationSeq: Optional[int]
    operationType: Optional[str]
    operationName: Optional[str]
    routingId: Optional[str]
    siteId: Optional[str]
    bopId: Optional[int]  

    class Config:
        orm_mode = True
