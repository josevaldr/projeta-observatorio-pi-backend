from pydantic import BaseModel

class ProfessorCreate(BaseModel):
    id_professor: int
    especialidade: str

class ProfessorCompletoCreate(BaseModel):
    nome_usuario: str
    email: str
    senha: str
    especialidade: str

