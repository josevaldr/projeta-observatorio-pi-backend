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
        SELECT a.*, p.bio, p.habilidades, p.linkedin, p.github, p.tema, u.nome_usuario, u.email 
        FROM aluno a
        LEFT JOIN portfolio p ON a.id_aluno = p.id_aluno
        JOIN usuario u ON a.id_aluno = u.id_usuario
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
        cursor.execute("SELECT * FROM portfolio WHERE id_aluno = ?", (id_aluno,))
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
        cursor.execute("SELECT id_aluno FROM portfolio WHERE id_aluno = ?", (id_aluno,))
        exists = cursor.fetchone()
        
        if exists:
            query = """
            UPDATE portfolio 
            SET bio = ?, habilidades = ?, linkedin = ?, github = ?, tema = ?
            WHERE id_aluno = ?
            """
            cursor.execute(query, (data.bio, data.habilidades, data.linkedin, data.github, data.tema, id_aluno))
        else:
            query = """
            INSERT INTO portfolio (id_aluno, bio, habilidades, linkedin, github, tema)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (id_aluno, data.bio, data.habilidades, data.linkedin, data.github, data.tema))
            
        conn.commit()
        return get_perfil_aluno(id_aluno)
    finally:
        cursor.close()
        conn.close()

def get_portfolio_by_username(username: str):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # 1. Buscar usuário
        cursor.execute("SELECT id_usuario, nome_usuario, email FROM usuario WHERE nome_usuario = ?", (username,))
        user_row = cursor.fetchone()
        if not user_row:
            return None
        user_data = dict(user_row)
        id_aluno = user_data['id_usuario']

        # 2. Buscar perfil
        cursor.execute("SELECT bio, habilidades, linkedin, github, tema FROM portfolio WHERE id_aluno = ?", (id_aluno,))
        perfil_row = cursor.fetchone()
        if perfil_row:
            perfil_data = dict(perfil_row)
        else:
            perfil_data = {
                "bio": "Estudante e desenvolvedor em evolução. Apaixonado por transformar ideias complexas em interfaces simples e intuitivas.",
                "habilidades": "",
                "linkedin": "",
                "github": "",
                "tema": "blue"
            }

        # 3. Buscar projetos do aluno
        query_projetos = """
        SELECT p.id_projeto as id, p.titulo, p.descricao as disciplina, p.data_upload as ano, p.status_projeto, p.link_projeto, e.nome_equipe
        FROM projeto p
        JOIN equipe e ON p.id_projeto = e.cod_id_projeto
        JOIN participa part ON e.id_equipe = part.cod_id_equipe
        WHERE part.cod_id_aluno = ?
        """
        cursor.execute(query_projetos, (id_aluno,))
        projetos_rows = cursor.fetchall()
        projetos_data = [dict(row) for row in projetos_rows]

        return {
            "usuario": user_data,
            "perfil": perfil_data,
            "projetos": projetos_data
        }
    finally:
        cursor.close()
        conn.close()
