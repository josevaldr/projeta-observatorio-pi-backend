from app.repositories.equipe_repository import EquipeRepository
from app.schemas.equipe_schemas import EquipeCreate, EquipeUpdate
from fastapi import HTTPException

class EquipeService:
    def __init__(self):
        self.repository = EquipeRepository()

    def create_equipe(self, equipe: EquipeCreate):
        return self.repository.create_equipe(equipe.dict())

    def get_equipes(self):
        return self.repository.get_equipes()

    def get_equipe_by_id(self, id_equipe: int):
        equipe = self.repository.get_equipe_by_id(id_equipe)
        if not equipe:
            raise HTTPException(status_code=404, detail="Equipe não encontrada")
        return equipe

    def update_equipe(self, id_equipe: int, equipe: EquipeUpdate):
        self.get_equipe_by_id(id_equipe)
        updated_equipe = self.repository.update_equipe(id_equipe, equipe.dict(exclude_unset=True))
        return updated_equipe

    def delete_equipe(self, id_equipe: int):
        self.get_equipe_by_id(id_equipe)
        self.repository.delete_equipe(id_equipe)
        return {"message": "Equipe deletada com sucesso"}

    def add_aluno_to_equipe(self, id_equipe: int, id_aluno: int, semestre: str):
        # Verifica se equipe existe
        self.get_equipe_by_id(id_equipe)
        # Tenta inserir na tabela participa
        try:
            return self.repository.add_aluno_to_equipe(id_equipe, id_aluno, semestre)
        except Exception as e:
            raise HTTPException(status_code=400, detail="Erro ao adicionar aluno. Verifique se o aluno existe ou já está na equipe neste semestre.")

