from app.config.database import get_connection


def create_user(data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        INSERT INTO usuario (nome_usuario, email, senha, tipo_usuario)
        VALUES (?, ?, ?, ?)
        """

        cursor.execute(query, (
            data.nome_usuario,
            data.email,
            data.senha,
            data.tipo_usuario
        ))

        conn.commit()

        user_id = cursor.lastrowid

        return {
            "id_usuario": user_id,
            "nome_usuario": data.nome_usuario,
            "email": data.email,
            "tipo_usuario": data.tipo_usuario
        }

    finally:
        cursor.close()
        conn.close()


def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM usuario WHERE id_usuario = ?", (user_id,))
        user = cursor.fetchone()

        if user:
            return dict(user)
        return None

    finally:
        cursor.close()
        conn.close()


def update_user(user_id, data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        UPDATE usuario
        SET nome_usuario = ?, email = ?, tipo_usuario = ?
        WHERE id_usuario = ?
        """

        cursor.execute(query, (
            data.nome_usuario,
            data.email,
            data.tipo_usuario,
            user_id
        ))

        conn.commit()

        return {"message": "Usuário atualizado com sucesso"}

    finally:
        cursor.close()
        conn.close()


def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM usuario WHERE id_usuario = ?", (user_id,))
        conn.commit()

        return {"message": "Usuário deletado com sucesso"}

    finally:
        cursor.close()
        conn.close()


def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM usuario")
        users = cursor.fetchall()
        return [dict(user) for user in users]

    finally:
        cursor.close()
        conn.close()


def get_user_by_email_and_password(email, senha):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT * FROM usuario WHERE email = ? AND senha = ?",
            (email, senha)
        )
        user = cursor.fetchone()

        if user:
            user_data = dict(user)
            user_data.pop("senha", None)
            return user_data

        return None

    finally:
        cursor.close()
        conn.close()


        

