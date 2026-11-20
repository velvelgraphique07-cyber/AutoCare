
from datos.conexion import conectar


class RepositorioMecanicos:

    def registrar(self, mecanico):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO mecanicos (
                id_mecanico,
                nombre,
                especialidad,
                telefono,
                disponible
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            mecanico.id_mecanico,
            mecanico.nombre,
            mecanico.especialidad,
            mecanico.telefono,
            int(mecanico.disponible)
        ))

        conexion.commit()
        conexion.close()

        print("Mecánico guardado en SQLite correctamente.")

    def listar(self):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM mecanicos")
        mecanicos = cursor.fetchall()

        conexion.close()

        return mecanicos

    def buscar_por_id(self, id_mecanico):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM mecanicos WHERE id_mecanico = ?",
            (id_mecanico,)
        )

        mecanico = cursor.fetchone()
        conexion.close()

        return mecanico

    def actualizar(self, mecanico):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE mecanicos
            SET nombre = ?, especialidad = ?,
                telefono = ?, disponible = ?
            WHERE id_mecanico = ?
        """, (
            mecanico.nombre,
            mecanico.especialidad,
            mecanico.telefono,
            int(mecanico.disponible),
            mecanico.id_mecanico
        ))

        conexion.commit()
        actualizado = cursor.rowcount > 0
        conexion.close()

        return actualizado

    def eliminar(self, id_mecanico):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM mecanicos WHERE id_mecanico = ?",
            (id_mecanico,)
        )

        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()

        return eliminado
