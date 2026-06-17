from pydantic import BaseModel
from typing import Optional

class EquipeBase(BaseModel):
    nome_equipe: str
    cod_id_projeto: Optional[int] = None

class EquipeCreate(EquipeBase):
    pass

class EquipeUpdate(BaseModel):
    nome_equipe: Optional[str] = None
    cod_id_projeto: Optional[int] = None

class EquipeResponse(EquipeBase):
    id_equipe: int
    quantidade_membros: Optional[int] = 0

    class Config:
        orm_mode = True

class ParticipaCreate(BaseModel):
    cod_id_aluno: int
    semestre: str

class ParticipaResponse(ParticipaCreate):
    cod_id_equipe: int

