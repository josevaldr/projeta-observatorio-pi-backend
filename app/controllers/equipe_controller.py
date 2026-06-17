from fastapi import APIRouter, status
from typing import List
from app.schemas.equipe_schemas import EquipeCreate, EquipeUpdate, EquipeResponse
from app.services.equipe_service import EquipeService

class EquipeController:
    def __init__(self):
        self.service = EquipeService()

    def create_equipe(self, equipe: EquipeCreate):
        return self.service.create_equipe(equipe)

    def get_equipes(self):
        return self.service.get_equipes()

    def get_equipe_by_id(self, id_equipe: int):
        return self.service.get_equipe_by_id(id_equipe)

    def update_equipe(self, id_equipe: int, equipe: EquipeUpdate):
        return self.service.update_equipe(id_equipe, equipe)

    def delete_equipe(self, id_equipe: int):
        return self.service.delete_equipe(id_equipe)

    def add_aluno_to_equipe(self, id_equipe: int, id_aluno: int, semestre: str):
        return self.service.add_aluno_to_equipe(id_equipe, id_aluno, semestre)

