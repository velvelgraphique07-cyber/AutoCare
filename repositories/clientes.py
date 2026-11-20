
from datos.conexion import conectar


class RepositorioClientes:

    def registrar(self, cliente):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO clientes (
                id_cliente, nombre, telefono, correo
            )
            VALUES (?, ?, ?, ?)
        """, (
            cliente.id_cliente,
            cliente.nombre,
            cliente.telefono,
            cliente.correo
        ))

        conexion.commit()
        conexion.close()

        print("Cliente guardado en SQLite correctamente.")

    def listar(self):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()

        conexion.close()

        return clientes
