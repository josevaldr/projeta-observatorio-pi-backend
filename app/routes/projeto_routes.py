from fastapi import APIRouter, status
from typing import List
from app.schemas.projeto_schemas import ProjetoCreate, ProjetoUpdate, ProjetoResponse
from app.controllers.projeto_controller import ProjetoController

router = APIRouter(prefix="/projetos", tags=["Projetos"])
controller = ProjetoController()

@router.post("/", response_model=ProjetoResponse, status_code=status.HTTP_201_CREATED)
def create_projeto(projeto: ProjetoCreate):
    return controller.create_projeto(projeto)

@router.get("/", response_model=List[ProjetoResponse])
def get_projetos():
    return controller.get_projetos()

@router.get("/{id_projeto}", response_model=ProjetoResponse)
def get_projeto_by_id(id_projeto: int):
    return controller.get_projeto_by_id(id_projeto)

@router.put("/{id_projeto}", response_model=ProjetoResponse)
def update_projeto(id_projeto: int, projeto: ProjetoUpdate):
    return controller.update_projeto(id_projeto, projeto)

@router.delete("/{id_projeto}", status_code=status.HTTP_204_NO_CONTENT)
def delete_projeto(id_projeto: int):
    controller.delete_projeto(id_projeto)
    return None
