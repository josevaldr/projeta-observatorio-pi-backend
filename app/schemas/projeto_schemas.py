from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import date

class ProjetoBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    status_projeto: Optional[str] = "Pendente"
    link_projeto: Optional[str] = None
    cod_id_avaliacao: Optional[int] = None

class ProjetoCreate(ProjetoBase):
    pass

class ProjetoUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    status_projeto: Optional[str] = None
    link_projeto: Optional[str] = None
    cod_id_avaliacao: Optional[int] = None

class ProjetoResponse(ProjetoBase):
    id_projeto: int
    data_upload: Optional[date]
    equipe: Optional[Dict[str, Any]] = None

    class Config:
        orm_mode = True
