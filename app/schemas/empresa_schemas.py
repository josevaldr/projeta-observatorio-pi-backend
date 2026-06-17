from pydantic import BaseModel
from typing import Optional


class EmpresaCreate(BaseModel):
    id_empresa: int
    telefone: Optional[str] = None
    cnpj: str

class EmpresaCompletoCreate(BaseModel):
    nome_usuario: str
    email: str
    senha: str
    telefone: Optional[str] = None
    cnpj: str

