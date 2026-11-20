
from datos.conexion import conectar


def obtener_estadisticas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM clientes")
    total_clientes = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM vehiculos")
    total_vehiculos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM mecanicos")
    total_mecanicos = cursor.fetchone()[0]

    conexion.close()

    return {
        "clientes": total_clientes,
        "vehiculos": total_vehiculos,
        "mecanicos": total_mecanicos
    }
