from app.repositories.avaliacao_repository import create_avaliacao, get_avaliacoes, get_avaliacao_by_id
from app.repositories.professor_repository import get_professor_by_id

def create_avaliacao_service(data):
    prof = get_professor_by_id(data.cod_id_professor)
    if not prof:
        raise ValueError("Professor não encontrado.")
    return create_avaliacao(data)

def get_avaliacoes_service():
    return get_avaliacoes()

def get_avaliacao_by_id_service(id_avaliacao):
    avaliacao = get_avaliacao_by_id(id_avaliacao)
    if not avaliacao:
        raise LookupError("Avaliação não encontrada.")
    return avaliacao
