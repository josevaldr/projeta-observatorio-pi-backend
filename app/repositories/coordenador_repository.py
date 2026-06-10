
from app.config.database import get_connection

def create_coordenador(data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        INSERT INTO coordenador (id_coordenador, curso)
        VALUES (?, ?)
        """

        cursor.execute(query, (
            data.id_coordenador,
            data.curso
        ))

        conn.commit()

        return {"message": "Coordenador criado com sucesso"}

    finally:
        cursor.close()
        conn.close()


def get_all_coordenadores():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM coordenador")
        coordenadores = cursor.fetchall()

        return [dict(c) for c in coordenadores]

    finally:
        cursor.close()
        conn.close()


def get_coordenador_by_id(id_coordenador):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = "SELECT * FROM coordenador WHERE id_coordenador = ?"
        cursor.execute(query, (id_coordenador,))
        coordenador = cursor.fetchone()

        return dict(coordenador) if coordenador else None

    finally:
        cursor.close()
        conn.close()

def update_coordenador(id_coordenador, data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        UPDATE coordenador
        SET curso
         = ?
        WHERE id_coordenador = ?
        """

        cursor.execute(query, (
            data.curso,
            id_coordenador
        ))

        conn.commit()

        return {"message": "Coordenador atualizado"}

    finally:
        cursor.close()
        conn.close()


def delete_coordenador(id_coordenador):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM coordenador WHERE id_coordenador = ?", (id_coordenador,))
        conn.commit()

        return {"message": "Coordenador deletado"}

    finally:
        cursor.close()
        conn.close()
