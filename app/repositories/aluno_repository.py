from app.config.database import get_connection


def create_aluno(data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        INSERT INTO aluno (id_aluno, matricula, curso, turma)
        VALUES (?, ?, ?, ?)
        """

        cursor.execute(query, (
            data.id_aluno,
            data.matricula,
            data.curso,
            data.turma
        ))

        conn.commit()

        return {
            "id_aluno": data.id_aluno,
            "matricula": data.matricula,
            "curso": data.curso,
            "turma": data.turma
        }

    finally:
        cursor.close()
        conn.close()


def get_all_alunos():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM aluno")
        alunos = cursor.fetchall()

        return [dict(aluno) for aluno in alunos]

    finally:
        cursor.close()
        conn.close()


def get_aluno_by_id(id_aluno):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM aluno WHERE id_aluno = ?", (id_aluno,))
        aluno = cursor.fetchone()

        if aluno:
            return dict(aluno)

        return None

    finally:
        cursor.close()
        conn.close()


def update_aluno(id_aluno, data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        UPDATE aluno
        SET matricula = ?, curso = ?, turma = ?
        WHERE id_aluno = ?
        """

        cursor.execute(query, (
            data.matricula,
            data.curso,
            data.turma,
            id_aluno
        ))

        conn.commit()

        return {
            "message": "Aluno atualizado com sucesso"
        }

    finally:
        cursor.close()
        conn.close()


def delete_aluno(id_aluno):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM aluno WHERE id_aluno = ?", (id_aluno,))
        conn.commit()

        return {
            "message": "Aluno deletado com sucesso"
        }

    finally:
        cursor.close()
        conn.close()
