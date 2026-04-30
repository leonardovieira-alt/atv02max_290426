from db.database import get_connection
from model.usuario import Usuario

class UsuarioRepository:
    def salvar(self, usuario: Usuario):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
            (usuario.nome, usuario.email)
        )
        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios")
        rows = cursor.fetchall()
        conn.close()
        return [Usuario(r[1], r[2], r[0]) for r in rows]

    def buscar_por_id(self, usuario_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios WHERE id = ?", (usuario_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Usuario(row[1], row[2], row[0])
        return None