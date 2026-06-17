from app.repositories.projeto_repository import ProjetoRepository
from app.schemas.projeto_schemas import ProjetoCreate, ProjetoUpdate
from fastapi import HTTPException

class ProjetoService:
    def __init__(self):
        self.repository = ProjetoRepository()

    def create_projeto(self, projeto: ProjetoCreate):
        return self.repository.create_projeto(projeto.dict())

    def get_projetos(self):
        return self.repository.get_projetos()

    def get_projeto_by_id(self, id_projeto: int):
        projeto = self.repository.get_projeto_by_id(id_projeto)
        if not projeto:
            raise HTTPException(status_code=404, detail="Projeto não encontrado")
        return projeto

    def update_projeto(self, id_projeto: int, projeto: ProjetoUpdate):
        # Verifica se existe
        self.get_projeto_by_id(id_projeto)
        
        updated_projeto = self.repository.update_projeto(id_projeto, projeto.dict(exclude_unset=True))
        return updated_projeto

    def delete_projeto(self, id_projeto: int):
        # Verifica se existe
        self.get_projeto_by_id(id_projeto)
        
        self.repository.delete_projeto(id_projeto)
        return {"message": "Projeto deletado com sucesso"}
