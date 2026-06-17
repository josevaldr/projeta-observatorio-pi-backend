from app.config.database import get_connection
import sqlite3

class EquipeRepository:
    def create_equipe(self, equipe_data: dict) -> dict:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute(
            """
            INSERT INTO equipe (nome_equipe, cod_id_projeto)
            VALUES (?, ?)
            """,
            (
                equipe_data.get('nome_equipe'),
                equipe_data.get('cod_id_projeto')
            )
        )
        conn.commit()
        
        last_id = cursor.lastrowid
        cursor.execute("SELECT * FROM equipe WHERE id_equipe = ?", (last_id,))
        new_equipe = dict(cursor.fetchone())
        
        conn.close()
        return new_equipe

    def get_equipes(self) -> list[dict]:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        query = """
        SELECT e.*, COUNT(p.cod_id_aluno) as quantidade_membros
        FROM equipe e
        LEFT JOIN participa p ON e.id_equipe = p.cod_id_equipe
        GROUP BY e.id_equipe
        """
        cursor.execute(query)
        equipes = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return equipes

    def get_equipe_by_id(self, id_equipe: int) -> dict | None:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        query = """
        SELECT e.*, COUNT(p.cod_id_aluno) as quantidade_membros
        FROM equipe e
        LEFT JOIN participa p ON e.id_equipe = p.cod_id_equipe
        WHERE e.id_equipe = ?
        GROUP BY e.id_equipe
        """
        cursor.execute(query, (id_equipe,))
        row = cursor.fetchone()
        
        conn.close()
        return dict(row) if row else None

    def update_equipe(self, id_equipe: int, equipe_data: dict) -> dict | None:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        update_fields = []
        values = []
        for key, value in equipe_data.items():
            if value is not None:
                update_fields.append(f"{key} = ?")
                values.append(value)
                
        if not update_fields:
            return self.get_equipe_by_id(id_equipe)
            
        values.append(id_equipe)
        query = f"UPDATE equipe SET {', '.join(update_fields)} WHERE id_equipe = ?"
        
        cursor.execute(query, tuple(values))
        conn.commit()
        
        cursor.execute("SELECT * FROM equipe WHERE id_equipe = ?", (id_equipe,))
        row = cursor.fetchone()
        
        conn.close()
        return dict(row) if row else None

    def delete_equipe(self, id_equipe: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM equipe WHERE id_equipe = ?", (id_equipe,))
        deleted = cursor.rowcount > 0
        
        conn.commit()
        conn.close()
        return deleted

    def add_aluno_to_equipe(self, id_equipe: int, id_aluno: int, semestre: str) -> dict:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute(
            """
            INSERT INTO participa (cod_id_equipe, cod_id_aluno, semestre)
            VALUES (?, ?, ?)
            """,
            (id_equipe, id_aluno, semestre)
        )
        conn.commit()
        
        cursor.execute(
            "SELECT * FROM participa WHERE cod_id_equipe = ? AND cod_id_aluno = ? AND semestre = ?",
            (id_equipe, id_aluno, semestre)
        )
        participacao = dict(cursor.fetchone())
        conn.close()
        return participacao

