from fastapi import APIRouter
from app.controllers.estatisticas_controller import get_estatisticas_controller

router = APIRouter(prefix="/estatisticas", tags=["Estatísticas e Dashboard"])

@router.get("/")
def get_estatisticas():
    return get_estatisticas_controller()
