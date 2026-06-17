from app.config.database import get_connection

def get_dashboard_stats():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Total Alunos
        cursor.execute("SELECT COUNT(*) FROM aluno")
        total_alunos = cursor.fetchone()[0]

        # Total Projetos
        cursor.execute("SELECT COUNT(*) FROM projeto")
        total_projetos = cursor.fetchone()[0]

        # Total Empresas Parceiras
        cursor.execute("SELECT COUNT(*) FROM empresa_parceira")
        total_empresas = cursor.fetchone()[0]

        # Total Avaliações
        cursor.execute("SELECT COUNT(*) FROM avaliacao")
        total_avaliacoes = cursor.fetchone()[0]

        return {
            "total_alunos": total_alunos,
            "total_projetos": total_projetos,
            "total_empresas": total_empresas,
            "total_avaliacoes": total_avaliacoes
        }

    finally:
        cursor.close()
        conn.close()
