
from fastapi import APIRouter
from app.controllers.coordenador_controller import *
from app.schemas.coordenador_schemas import CoordenadorCreate

router = APIRouter(prefix="/coordenadores", tags=["Coordenadores"])

@router.post("/")
def create_coordenador(data: CoordenadorCreate):
    return create_coordenador_controller(data)

@router.get("/")
def get_coordenadores():
    return get_coordenadores_controller()

@router.get("/{id}")
def get_coordenador(id: int):
    return get_coordenador_by_id_controller(id)

@router.put("/{id}")
def update_coordenador(id: int, data: CoordenadorCreate):
    return update_coordenador_controller(id, data)

@router.delete("/{id}")
def delete_coordenador(id: int):
    return delete_coordenador_controller(id)
