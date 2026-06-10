
from pydantic import BaseModel

class CoordenadorCreate(BaseModel):
    id_coordenador: int
    curso: str
