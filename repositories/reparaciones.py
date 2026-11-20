
from datos.conexion import conectar


class RepositorioReparaciones:

    def registrar(self, orden):
        conexion = conectar()
        cursor = conexion.cursor()

        try:
            # Guardar la orden
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

            # Guardar los mecánicos asignados
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
