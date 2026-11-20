
from datos.conexion import conectar


class RepositorioDetallesReparacion:

    def registrar(self, detalle):
        conexion = conectar()
        cursor = conexion.cursor()

        try:
            cursor.execute("""
                INSERT INTO detalles_reparacion (
                    id_detalle,
                    id_orden,
                    descripcion,
                    cantidad_horas,
                    costo_mano_obra
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                detalle.id_detalle,
                detalle.orden.id_orden,
                detalle.descripcion,
                detalle.cantidad_horas,
                detalle.costo_mano_obra
            ))

            conexion.commit()
            print("Detalle de reparación guardado en SQLite correctamente.")

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()

    def listar(self):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM detalles_reparacion")
        detalles = cursor.fetchall()

        conexion.close()
        return detalles

    def buscar_por_id(self, id_detalle):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM detalles_reparacion WHERE id_detalle = ?",
            (id_detalle,)
        )

        detalle = cursor.fetchone()
        conexion.close()
        return detalle

    def actualizar(self, detalle):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE detalles_reparacion
            SET id_orden = ?, descripcion = ?,
                cantidad_horas = ?, costo_mano_obra = ?
            WHERE id_detalle = ?
        """, (
            detalle.orden.id_orden,
            detalle.descripcion,
            detalle.cantidad_horas,
            detalle.costo_mano_obra,
            detalle.id_detalle
        ))

        conexion.commit()
        actualizado = cursor.rowcount > 0
        conexion.close()

        return actualizado

    def eliminar(self, id_detalle):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM detalles_reparacion WHERE id_detalle = ?",
            (id_detalle,)
        )

        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()

        return eliminado
