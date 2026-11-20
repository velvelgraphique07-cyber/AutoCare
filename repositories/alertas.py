
from datos.conexion import conectar


class RepositorioAlertas:

    def registrar(self, alerta):
        conexion = conectar()
        cursor = conexion.cursor()

        try:
            cursor.execute("""
                INSERT INTO alertas_mantenimiento (
                    id_alerta,
                    id_vehiculo,
                    fecha,
                    mensaje,
                    kilometraje_programado,
                    estado
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                alerta.id_alerta,
                alerta.vehiculo.id_vehiculo,
                alerta.fecha,
                alerta.mensaje,
                alerta.kilometraje_programado,
                alerta.estado
            ))

            conexion.commit()
            print("Alerta guardada en SQLite correctamente.")

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()

    def listar(self):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM alertas_mantenimiento")
        alertas = cursor.fetchall()

        conexion.close()
        return alertas

    def buscar_por_id(self, id_alerta):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM alertas_mantenimiento WHERE id_alerta = ?",
            (id_alerta,)
        )

        alerta = cursor.fetchone()
        conexion.close()
        return alerta

    def actualizar(self, alerta):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE alertas_mantenimiento
            SET id_vehiculo = ?, fecha = ?, mensaje = ?,
                kilometraje_programado = ?, estado = ?
            WHERE id_alerta = ?
        """, (
            alerta.vehiculo.id_vehiculo,
            alerta.fecha,
            alerta.mensaje,
            alerta.kilometraje_programado,
            alerta.estado,
            alerta.id_alerta
        ))

        conexion.commit()
        actualizado = cursor.rowcount > 0
        conexion.close()

        return actualizado

    def eliminar(self, id_alerta):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM alertas_mantenimiento WHERE id_alerta = ?",
            (id_alerta,)
        )

        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()

        return eliminado
