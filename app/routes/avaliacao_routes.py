from fastapi import APIRouter
from app.schemas.avaliacao_schemas import AvaliacaoCreate
from app.controllers.avaliacao_controller import *

router = APIRouter(prefix="/avaliacoes", tags=["Avaliações"])

@router.post("/")
def create_avaliacao(data: AvaliacaoCreate):
    return create_avaliacao_controller(data)

@router.get("/")
def get_avaliacoes():
    return get_avaliacoes_controller()

@router.get("/{id_avaliacao}")
def get_avaliacao(id_avaliacao: int):
    return get_avaliacao_by_id_controller(id_avaliacao)
