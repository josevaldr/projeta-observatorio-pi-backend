from fastapi import APIRouter, status
from typing import List
from app.schemas.equipe_schemas import EquipeCreate, EquipeUpdate, EquipeResponse, ParticipaCreate, ParticipaResponse
from app.controllers.equipe_controller import EquipeController

router = APIRouter(prefix="/equipes", tags=["Equipes"])
controller = EquipeController()

@router.post("/", response_model=EquipeResponse, status_code=status.HTTP_201_CREATED)
def create_equipe(equipe: EquipeCreate):
    return controller.create_equipe(equipe)

@router.get("/", response_model=List[EquipeResponse])
def get_equipes():
    return controller.get_equipes()

@router.get("/{id_equipe}", response_model=EquipeResponse)
def get_equipe_by_id(id_equipe: int):
    return controller.get_equipe_by_id(id_equipe)

@router.put("/{id_equipe}", response_model=EquipeResponse)
def update_equipe(id_equipe: int, equipe: EquipeUpdate):
    return controller.update_equipe(id_equipe, equipe)

@router.delete("/{id_equipe}", status_code=status.HTTP_204_NO_CONTENT)
def delete_equipe(id_equipe: int):
    controller.delete_equipe(id_equipe)
    return None

@router.post("/{id_equipe}/alunos", response_model=ParticipaResponse, status_code=status.HTTP_201_CREATED)
def add_aluno_to_equipe(id_equipe: int, participa: ParticipaCreate):
    return controller.add_aluno_to_equipe(id_equipe, participa.cod_id_aluno, participa.semestre)

