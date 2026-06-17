
from pydantic import BaseModel

class CoordenadorCreate(BaseModel):
    id_coordenador: int
    curso: str

class CoordenadorCompletoCreate(BaseModel):
    nome_usuario: str
    email: str
    senha: str
    curso: str

