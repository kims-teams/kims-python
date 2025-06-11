from pydantic import BaseModel, Field

class ScenarioDTO(BaseModel):
    id: str

    class Config:
        populate_by_name = True
        from_attributes = True
