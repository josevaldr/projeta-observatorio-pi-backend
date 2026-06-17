from pydantic import BaseModel


class AlunoCreate(BaseModel):
    id_aluno: int
    matricula: int
    curso: str
    turma: str

class AlunoCompletoCreate(BaseModel):
    nome_usuario: str
    email: str
    senha: str
    matricula: int
    curso: str
    turma: str

from typing import Optional

class PerfilAlunoCreate(BaseModel):
    bio: Optional[str] = None
    habilidades: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    tema: Optional[str] = "blue"
