from fastapi import APIRouter, Depends, status
from typing import List
from app.schemas.projeto_schemas import ProjetoCreate, ProjetoUpdate, ProjetoResponse
from app.services.projeto_service import ProjetoService

class ProjetoController:
    def __init__(self):
        self.service = ProjetoService()

    def create_projeto(self, projeto: ProjetoCreate):
        return self.service.create_projeto(projeto)

    def get_projetos(self):
        return self.service.get_projetos()

    def get_projeto_by_id(self, id_projeto: int):
        return self.service.get_projeto_by_id(id_projeto)

    def update_projeto(self, id_projeto: int, projeto: ProjetoUpdate):
        return self.service.update_projeto(id_projeto, projeto)

    def delete_projeto(self, id_projeto: int):
        return self.service.delete_projeto(id_projeto)
