
from datos.conexion import conectar


class RepositorioReparaciones:

    def registrar(self, orden):
        conexion = conectar()
        cursor = conexion.cursor()

        try:
            cursor.execute("""
                INSERT INTO ordenes_reparacion (
                    id_orden,
                    id_vehiculo,
                    fecha,
                    descripcion,
                    estado
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                orden.id_orden,
                orden.vehiculo.id_vehiculo,
                orden.fecha,
                orden.descripcion,
                orden.estado
            ))

            for mecanico in orden.mecanicos:
                cursor.execute("""
                    INSERT INTO orden_mecanicos (
                        id_orden,
                        id_mecanico
                    )
                    VALUES (?, ?)
                """, (
                    orden.id_orden,
                    mecanico.id_mecanico
                ))

            conexion.commit()
            print("Orden y mecánicos guardados correctamente.")

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()

    def listar(self):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM ordenes_reparacion")
        ordenes = cursor.fetchall()

        conexion.close()
        return ordenes

    def buscar_por_id(self, id_orden):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM ordenes_reparacion WHERE id_orden = ?",
            (id_orden,)
        )

        orden = cursor.fetchone()
        conexion.close()
        return orden

    def listar_mecanicos(self, id_orden):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT mecanicos.*
            FROM mecanicos
            INNER JOIN orden_mecanicos
                ON mecanicos.id_mecanico = orden_mecanicos.id_mecanico
            WHERE orden_mecanicos.id_orden = ?
        """, (id_orden,))

        mecanicos = cursor.fetchall()
        conexion.close()
        return mecanicos

    def actualizar(self, orden):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE ordenes_reparacion
            SET id_vehiculo = ?, fecha = ?,
                descripcion = ?, estado = ?
            WHERE id_orden = ?
        """, (
            orden.vehiculo.id_vehiculo,
            orden.fecha,
            orden.descripcion,
            orden.estado,
            orden.id_orden
        ))

        conexion.commit()
        actualizado = cursor.rowcount > 0
        conexion.close()

        return actualizado

    def eliminar(self, id_orden):
        conexion = conectar()
        cursor = conexion.cursor()

        try:
            cursor.execute(
                "DELETE FROM orden_mecanicos WHERE id_orden = ?",
                (id_orden,)
            )

            cursor.execute(
                "DELETE FROM ordenes_reparacion WHERE id_orden = ?",
                (id_orden,)
            )

            conexion.commit()
            eliminado = cursor.rowcount > 0

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()

        return eliminado
