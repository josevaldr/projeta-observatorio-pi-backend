from pydantic import BaseModel
from typing import Optional

class AvaliacaoBase(BaseModel):
    cod_id_professor: int
    conceito: str
    feedback: Optional[str] = None

class AvaliacaoCreate(AvaliacaoBase):
    pass

class AvaliacaoResponse(AvaliacaoBase):
    id_avaliacao: int
    data_avaliacao: str

    class Config:
        orm_mode = True
