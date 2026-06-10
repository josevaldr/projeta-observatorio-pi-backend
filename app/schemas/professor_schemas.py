from pydantic import BaseModel

class ProfessorCreate(BaseModel):
    id_professor: int
    especialidade: str
