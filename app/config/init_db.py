from app.config.database import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_usuario TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        tipo_usuario TEXT NOT NULL,
        data_cadastro DATE DEFAULT CURRENT_DATE
    );
    """)

    conn.commit()
    conn.close()
