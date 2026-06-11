from pydantic import BaseModel, EmailStr
from typing import Literal

class UserCreate(BaseModel):
    nome_usuario: str
    email: EmailStr
    senha: str
    tipo_usuario: Literal["aluno", "professor", "empresa", "coordenador"]

class UserLogin(BaseModel):
    email: EmailStr
    senha: str



