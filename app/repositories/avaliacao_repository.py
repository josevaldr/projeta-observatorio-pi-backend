from app.config.database import get_connection
import sqlite3

def create_avaliacao(data) -> dict:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO avaliacao (cod_id_professor, conceito, feedback)
            VALUES (?, ?, ?)
            """,
            (data.cod_id_professor, data.conceito, data.feedback)
        )
        conn.commit()
        last_id = cursor.lastrowid
        cursor.execute("SELECT * FROM avaliacao WHERE id_avaliacao = ?", (last_id,))
        return dict(cursor.fetchone())
    finally:
        cursor.close()
        conn.close()

def get_avaliacoes() -> list:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM avaliacao")
        return [dict(row) for row in cursor.fetchall()]
    finally:
        cursor.close()
        conn.close()

def get_avaliacao_by_id(id_avaliacao: int) -> dict | None:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM avaliacao WHERE id_avaliacao = ?", (id_avaliacao,))
        row = cursor.fetchone()
        return dict(row) if row else None
    finally:
        cursor.close()
        conn.close()
