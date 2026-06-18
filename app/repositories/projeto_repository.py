from app.config.database import get_connection
import sqlite3

class ProjetoRepository:
    def create_projeto(self, projeto_data: dict) -> dict:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute(
            """
            INSERT INTO projeto (cod_id_avaliacao, titulo, descricao, status_projeto, link_projeto)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                projeto_data.get('cod_id_avaliacao'),
                projeto_data.get('titulo'),
                projeto_data.get('descricao'),
                projeto_data.get('status_projeto'),
                projeto_data.get('link_projeto')
            )
        )
        conn.commit()
        
        # Get the inserted row
        last_id = cursor.lastrowid
        cursor.execute("SELECT * FROM projeto WHERE id_projeto = ?", (last_id,))
        new_projeto = dict(cursor.fetchone())
        
        conn.close()
        return new_projeto

    def get_projetos(self) -> list[dict]:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM projeto")
        projetos_rows = cursor.fetchall()
        projetos = [dict(row) for row in projetos_rows]
        
        for proj in projetos:
            cursor.execute("SELECT id_equipe, nome_equipe FROM equipe WHERE cod_id_projeto = ?", (proj['id_projeto'],))
            equipe_row = cursor.fetchone()
            if equipe_row:
                equipe = dict(equipe_row)
                cursor.execute("""
                    SELECT u.nome_usuario 
                    FROM participa p
                    JOIN aluno a ON p.cod_id_aluno = a.id_aluno
                    JOIN usuario u ON a.id_aluno = u.id_usuario
                    WHERE p.cod_id_equipe = ?
                """, (equipe['id_equipe'],))
                alunos_rows = cursor.fetchall()
                equipe['alunos'] = [r['nome_usuario'] for r in alunos_rows]
                proj['equipe'] = equipe
            else:
                proj['equipe'] = None
        
        conn.close()
        return projetos

    def get_projeto_by_id(self, id_projeto: int) -> dict | None:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM projeto WHERE id_projeto = ?", (id_projeto,))
        row = cursor.fetchone()
        
        conn.close()
        return dict(row) if row else None

    def update_projeto(self, id_projeto: int, projeto_data: dict) -> dict | None:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Build query dynamically based on provided fields
        update_fields = []
        values = []
        for key, value in projeto_data.items():
            if value is not None:
                update_fields.append(f"{key} = ?")
                values.append(value)
                
        if not update_fields:
            return self.get_projeto_by_id(id_projeto)
            
        values.append(id_projeto)
        query = f"UPDATE projeto SET {', '.join(update_fields)} WHERE id_projeto = ?"
        
        cursor.execute(query, tuple(values))
        conn.commit()
        
        # Fetch updated row
        cursor.execute("SELECT * FROM projeto WHERE id_projeto = ?", (id_projeto,))
        row = cursor.fetchone()
        
        conn.close()
        return dict(row) if row else None

    def delete_projeto(self, id_projeto: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM projeto WHERE id_projeto = ?", (id_projeto,))
        deleted = cursor.rowcount > 0
        
        conn.commit()
        conn.close()
        return deleted
