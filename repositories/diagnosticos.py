
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
