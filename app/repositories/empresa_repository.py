from app.config.database import get_connection


def create_empresa(data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        INSERT INTO empresa_parceira (id_empresa, telefone, cnpj)
        VALUES (?, ?, ?)
        """

        cursor.execute(query, (
            data.id_empresa,
            data.telefone,
            data.cnpj
        ))

        conn.commit()

        return {
            "id_empresa": data.id_empresa,
            "telefone": data.telefone,
            "cnpj": data.cnpj
        }

    finally:
        cursor.close()
        conn.close()


def get_all_empresas():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        SELECT e.*, u.nome_usuario, u.email 
        FROM empresa_parceira e
        JOIN usuario u ON e.id_empresa = u.id_usuario
        """
        cursor.execute(query)
        empresas = cursor.fetchall()

        return [dict(empresa) for empresa in empresas]

    finally:
        cursor.close()
        conn.close()


def get_empresa_by_id(id_empresa):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        SELECT e.*, u.nome_usuario, u.email 
        FROM empresa_parceira e
        JOIN usuario u ON e.id_empresa = u.id_usuario
        WHERE e.id_empresa = ?
        """
        cursor.execute(query, (id_empresa,))

        empresa = cursor.fetchone()

        if empresa:
            return dict(empresa)

        return None

    finally:
        cursor.close()
        conn.close()


def update_empresa(id_empresa, data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        UPDATE empresa_parceira
        SET telefone = ?, cnpj = ?
        WHERE id_empresa = ?
        """

        cursor.execute(query, (
            data.telefone,
            data.cnpj,
            id_empresa
        ))

        conn.commit()

        return {
            "message": "Empresa atualizada com sucesso"
        }

    finally:
        cursor.close()
        conn.close()


def delete_empresa(id_empresa):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "DELETE FROM empresa_parceira WHERE id_empresa = ?",
            (id_empresa,)
        )

        conn.commit()

        return {
            "message": "Empresa deletada com sucesso"
        }

    finally:
        cursor.close()
        conn.close()
