
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
