
from datos.conexion import conectar


class RepositorioDiagnosticos:

    def registrar(self, diagnostico):
        conexion = conectar()
        cursor = conexion.cursor()

        try:
            cursor.execute("""
                INSERT INTO diagnosticos (
                    id_diagnostico,
                    id_orden,
                    fecha,
                    descripcion,
                    observaciones
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                diagnostico.id_diagnostico,
                diagnostico.orden.id_orden,
                diagnostico.fecha,
                diagnostico.descripcion,
                diagnostico.observaciones
            ))

            conexion.commit()
            print("Diagnóstico guardado en SQLite correctamente.")

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()

    def listar(self):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM diagnosticos")
        diagnosticos = cursor.fetchall()

        conexion.close()
        return diagnosticos

    def buscar_por_id(self, id_diagnostico):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM diagnosticos WHERE id_diagnostico = ?",
            (id_diagnostico,)
        )

        diagnostico = cursor.fetchone()
        conexion.close()
        return diagnostico

    def actualizar(self, diagnostico):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE diagnosticos
            SET id_orden = ?, fecha = ?,
                descripcion = ?, observaciones = ?
            WHERE id_diagnostico = ?
        """, (
            diagnostico.orden.id_orden,
            diagnostico.fecha,
            diagnostico.descripcion,
            diagnostico.observaciones,
            diagnostico.id_diagnostico
        ))

        conexion.commit()
        actualizado = cursor.rowcount > 0
        conexion.close()

        return actualizado

    def eliminar(self, id_diagnostico):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM diagnosticos WHERE id_diagnostico = ?",
            (id_diagnostico,)
        )

        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()

        return eliminado
