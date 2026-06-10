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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS empresa_parceira (
        id_empresa INTEGER PRIMARY KEY,
        telefone TEXT,
        cnpj TEXT NOT NULL UNIQUE,
        FOREIGN KEY (id_empresa) REFERENCES usuario (id_usuario)
    );               
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS professor (
        id_professor INTEGER PRIMARY KEY,
        especialidade TEXT,
        FOREIGN KEY (id_professor) REFERENCES usuario (id_usuario)
    );               
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS coordenador (
        id_coordenador INTEGER PRIMARY KEY,
        curso TEXT,
        FOREIGN KEY (id_coordenador) REFERENCES usuario (id_usuario)
    );               
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS avaliacao (
        id_avaliacao INTEGER PRIMARY KEY AUTOINCREMENT,
        cod_id_professor INTEGER,
        conceito TEXT NOT NULL,
        feedback TEXT,
        data_avaliacao DATE DEFAULT CURRENT_DATE,
        FOREIGN KEY (cod_id_professor) REFERENCES professor (id_professor)
    );               
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projeto (
        id_projeto INTEGER PRIMARY KEY AUTOINCREMENT,
        cod_id_avaliacao INTEGER,
        titulo TEXT NOT NULL,
        descricao TEXT,
        data_upload DATE DEFAULT CURRENT_DATE,
        status_projeto TEXT,
        link_projeto TEXT,
        FOREIGN KEY (cod_id_avaliacao) REFERENCES avaliacao (id_avaliacao)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipe (
        id_equipe INTEGER PRIMARY KEY AUTOINCREMENT,
        cod_id_projeto INTEGER,
        nome_equipe TEXT,
        FOREIGN KEY (cod_id_projeto) REFERENCES projeto (id_projeto)
    );
    """)


    conn.commit()
    conn.close()



