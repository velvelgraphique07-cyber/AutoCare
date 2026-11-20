
from datos.conexion import conectar


class RepositorioMantenimientos:

    def registrar(self, mantenimiento):
        conexion = conectar()
        cursor = conexion.cursor()

        try:
            cursor.execute("""
                INSERT INTO mantenimientos (
                    id_mantenimiento,
                    id_vehiculo,
                    fecha,
                    tipo,
                    descripcion,
                    kilometraje,
                    estado
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                mantenimiento.id_mantenimiento,
                mantenimiento.vehiculo.id_vehiculo,
                mantenimiento.fecha,
                mantenimiento.tipo,
                mantenimiento.descripcion,
                mantenimiento.kilometraje,
                mantenimiento.estado
            ))

            conexion.commit()
            print("Mantenimiento guardado en SQLite correctamente.")

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()

    def listar(self):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM mantenimientos")
        mantenimientos = cursor.fetchall()

        conexion.close()
        return mantenimientos

    def buscar_por_id(self, id_mantenimiento):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM mantenimientos WHERE id_mantenimiento = ?",
            (id_mantenimiento,)
        )

        mantenimiento = cursor.fetchone()
        conexion.close()
        return mantenimiento

    def actualizar(self, mantenimiento):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE mantenimientos
            SET id_vehiculo = ?, fecha = ?, tipo = ?,
                descripcion = ?, kilometraje = ?, estado = ?
            WHERE id_mantenimiento = ?
        """, (
            mantenimiento.vehiculo.id_vehiculo,
            mantenimiento.fecha,
            mantenimiento.tipo,
            mantenimiento.descripcion,
            mantenimiento.kilometraje,
            mantenimiento.estado,
            mantenimiento.id_mantenimiento
        ))

        conexion.commit()
        actualizado = cursor.rowcount > 0
        conexion.close()

        return actualizado

    def eliminar(self, id_mantenimiento):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM mantenimientos WHERE id_mantenimiento = ?",
            (id_mantenimiento,)
        )

        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()

        return eliminado
