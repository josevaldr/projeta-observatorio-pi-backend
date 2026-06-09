
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
