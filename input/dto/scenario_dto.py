from pydantic import BaseModel

class ScenarioDTO(BaseModel):
    id: str

    class Config:
        orm_mode = True
