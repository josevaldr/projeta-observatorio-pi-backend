from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr

from app.config.database import get_connection


router = APIRouter(prefix="/alunos", tags=["Alunos"])


class AlunoCreate(BaseModel):
    nome_usuario: str
    email: EmailStr
    senha: str


@router.post("")
def cadastrar_aluno(aluno: AlunoCreate):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO usuario (nome_usuario, email, senha, tipo_usuario)
            VALUES (?, ?, ?, ?)
        """, (
            aluno.nome_usuario,
            aluno.email,
            aluno.senha,
            "aluno"
        ))

        conn.commit()

        return {
            "mensagem": "Aluno cadastrado com sucesso",
            "aluno": {
                "nome_usuario": aluno.nome_usuario,
                "email": aluno.email,
                "tipo_usuario": "aluno"
            }
        }

    except Exception as erro:
        raise HTTPException(status_code=400, detail=str(erro))

    finally:
        conn.close()


@router.get("")
def listar_alunos():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT id_usuario, nome_usuario, email, tipo_usuario, data_cadastro
            FROM usuario
            WHERE tipo_usuario = ?
        """, ("aluno",))

        alunos = cursor.fetchall()

        lista_alunos = []

        for aluno in alunos:
            lista_alunos.append({
                "id_usuario": aluno[0],
                "nome_usuario": aluno[1],
                "email": aluno[2],
                "tipo_usuario": aluno[3],
                "data_cadastro": aluno[4]
            })

        return {
            "mensagem": "Alunos listados com sucesso",
            "alunos": lista_alunos
        }

    except Exception as erro:
        raise HTTPException(status_code=400, detail=str(erro))

    finally:
        conn.close()
