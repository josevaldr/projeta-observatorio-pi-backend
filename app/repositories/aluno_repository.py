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
        query = """
        SELECT a.*, p.bio, p.habilidades, p.linkedin, p.github, p.tema 
        FROM aluno a
        LEFT JOIN perfil_aluno p ON a.id_aluno = p.id_aluno
        """
        cursor.execute(query)
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

def get_perfil_aluno(id_aluno: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM perfil_aluno WHERE id_aluno = ?", (id_aluno,))
        perfil = cursor.fetchone()
        if perfil:
            return dict(perfil)
        return None
    finally:
        cursor.close()
        conn.close()

def create_or_update_perfil_aluno(id_aluno: int, data):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Check if exists
        cursor.execute("SELECT id_aluno FROM perfil_aluno WHERE id_aluno = ?", (id_aluno,))
        exists = cursor.fetchone()
        
        if exists:
            query = """
            UPDATE perfil_aluno 
            SET bio = ?, habilidades = ?, linkedin = ?, github = ?, tema = ?
            WHERE id_aluno = ?
            """
            cursor.execute(query, (data.bio, data.habilidades, data.linkedin, data.github, data.tema, id_aluno))
        else:
            query = """
            INSERT INTO perfil_aluno (id_aluno, bio, habilidades, linkedin, github, tema)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (id_aluno, data.bio, data.habilidades, data.linkedin, data.github, data.tema))
            
        conn.commit()
        return get_perfil_aluno(id_aluno)
    finally:
        cursor.close()
        conn.close()

