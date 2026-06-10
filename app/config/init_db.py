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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS aluno (
        id_aluno INTEGER PRIMARY KEY,
        matricula TEXT NOT NULL,
        curso TEXT NOT NULL,
        turma TEXT NOT NULL,
        FOREIGN KEY (id_aluno) REFERENCES usuario (id_usuario)
    );
    """)

    conn.commit()
    conn.close()



