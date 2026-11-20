
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
