from pydantic import BaseModel
from typing import Optional


class EmpresaCreate(BaseModel):
    id_empresa: int
    telefone: Optional[str] = None
    cnpj: str
