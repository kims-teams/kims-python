from pydantic import BaseModel
from typing import Optional

class OperationDTO(BaseModel):
    id: Optional[int]
    runTime: Optional[int]
    runTimeUom: Optional[str]
    waitTimeUom: Optional[str]
    transferTimeUom: Optional[str]
    sourcingType: Optional[str]
    operationId: Optional[str]
    operationName: Optional[str]
    operationType: Optional[str]
    operationSeq: Optional[int]
    siteId2: Optional[str]
    bopId: Optional[int]

    class Config:
        orm_mode = True
