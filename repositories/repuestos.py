
from datos.conexion import conectar


class RepositorioRepuestos:

    def registrar(self, repuesto):
        conexion = conectar()
        cursor = conexion.cursor()

        try:
            cursor.execute("""
                INSERT INTO repuestos (
                    id_repuesto,
                    nombre,
                    descripcion,
                    precio,
                    cantidad_stock
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                repuesto.id_repuesto,
                repuesto.nombre,
                repuesto.descripcion,
                repuesto.precio,
                repuesto.cantidad_stock
            ))

            conexion.commit()
            print("Repuesto guardado en SQLite correctamente.")

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()

    def listar(self):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM repuestos")
        repuestos = cursor.fetchall()

        conexion.close()
        return repuestos

    def buscar_por_id(self, id_repuesto):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM repuestos WHERE id_repuesto = ?",
            (id_repuesto,)
        )

        repuesto = cursor.fetchone()
        conexion.close()
        return repuesto

    def actualizar(self, repuesto):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE repuestos
            SET nombre = ?, descripcion = ?,
                precio = ?, cantidad_stock = ?
            WHERE id_repuesto = ?
        """, (
            repuesto.nombre,
            repuesto.descripcion,
            repuesto.precio,
            repuesto.cantidad_stock,
            repuesto.id_repuesto
        ))

        conexion.commit()
        actualizado = cursor.rowcount > 0
        conexion.close()

        return actualizado

    def actualizar_stock(self, id_repuesto, nueva_cantidad):
        conexion = conectar()
        cursor = conexion.cursor()

        try:
            cursor.execute("""
                UPDATE repuestos
                SET cantidad_stock = ?
                WHERE id_repuesto = ?
            """, (nueva_cantidad, id_repuesto))

            conexion.commit()

            if cursor.rowcount > 0:
                print("Stock actualizado correctamente.")
            else:
                print("No se encontró el repuesto.")

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()

    def eliminar(self, id_repuesto):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM repuestos WHERE id_repuesto = ?",
            (id_repuesto,)
        )

        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()

        return eliminado
