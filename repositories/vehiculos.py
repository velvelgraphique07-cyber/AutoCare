
from datos.conexion import conectar


class RepositorioVehiculos:

    def registrar(self, vehiculo):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO vehiculos (
                id_vehiculo,
                marca,
                modelo,
                patente,
                anio,
                id_cliente
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            vehiculo.id_vehiculo,
            vehiculo.marca,
            vehiculo.modelo,
            vehiculo.patente,
            vehiculo.anio,
            vehiculo.cliente.id_cliente
        ))

        conexion.commit()
        conexion.close()

        print("Vehículo guardado en SQLite correctamente.")

    def listar(self):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM vehiculos")
        vehiculos = cursor.fetchall()

        conexion.close()

        return vehiculos

    def buscar_por_id(self, id_vehiculo):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM vehiculos WHERE id_vehiculo = ?",
            (id_vehiculo,)
        )

        vehiculo = cursor.fetchone()
        conexion.close()

        return vehiculo

    def actualizar(self, vehiculo):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE vehiculos
            SET marca = ?, modelo = ?, patente = ?,
                anio = ?, id_cliente = ?
            WHERE id_vehiculo = ?
        """, (
            vehiculo.marca,
            vehiculo.modelo,
            vehiculo.patente,
            vehiculo.anio,
            vehiculo.cliente.id_cliente,
            vehiculo.id_vehiculo
        ))

        conexion.commit()
        actualizado = cursor.rowcount > 0
        conexion.close()

        return actualizado

    def eliminar(self, id_vehiculo):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM vehiculos WHERE id_vehiculo = ?",
            (id_vehiculo,)
        )

        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()

        return eliminado
