from pydantic import BaseModel


class AlunoCreate(BaseModel):
    id_aluno: int
    matricula: int
    curso: str
    turma: str
