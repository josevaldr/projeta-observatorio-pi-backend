from app.config.database import get_connection

def create_professor(data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        INSERT INTO professor (id_professor, especialidade)
        VALUES (?, ?)
        """

        cursor.execute(query, (
            data.id_professor,
            data.especialidade
        ))

        conn.commit()

        return {"message": "Professor criado com sucesso"}

    finally:
        cursor.close()
        conn.close()


def get_all_professores():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = "SELECT * FROM professor"
        professores = cursor.fetchall()

        return [dict(p) for p in professores]

    finally:
        cursor.close()
        conn.close()


def get_professor_by_id(id_professor):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = "SELECT * FROM professor WHERE id_professor = ?"
        cursor.execute(query, (id_professor,))
        professor = cursor.fetchone()

        return dict(professor) if professor else None

    finally:
        cursor.close()
        conn.close()


def update_professor(id_professor, data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        UPDATE professor
        SET formacao = ?, especialidade = ?
        WHERE id_professor = ?
        """

        cursor.execute(query, (
            data.formacao,
            data.especialidade,
            id_professor
        ))

        conn.commit()

        return {"message": "Professor atualizado"}

    finally:
        cursor.close()
        conn.close()


def delete_professor(id_professor):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM professor WHERE id_professor = ?", (id_professor,))
        conn.commit()

        return {"message": "Professor deletado"}

    finally:
        cursor.close()
        conn.close()

