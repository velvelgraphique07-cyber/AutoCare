
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

    def buscar_por_id(self, id_cliente):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM clientes WHERE id_cliente = ?",
            (id_cliente,)
        )

        cliente = cursor.fetchone()
        conexion.close()

        return cliente

    def actualizar(self, cliente):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE clientes
            SET nombre = ?, telefono = ?, correo = ?
            WHERE id_cliente = ?
        """, (
            cliente.nombre,
            cliente.telefono,
            cliente.correo,
            cliente.id_cliente
        ))

        conexion.commit()
        actualizado = cursor.rowcount > 0
        conexion.close()

        return actualizado

    def eliminar(self, id_cliente):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM clientes WHERE id_cliente = ?",
            (id_cliente,)
        )

        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()

        return eliminado
