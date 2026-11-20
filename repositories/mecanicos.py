
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
