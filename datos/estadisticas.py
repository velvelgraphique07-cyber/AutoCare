
from datos.conexion import conectar


def obtener_estadisticas():
    conexion = conectar()
    try:
        cursor = conexion.cursor()

        cursor.execute("SELECT COUNT(*) FROM clientes")
        total_clientes = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM vehiculos")
        total_vehiculos = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM mecanicos")
        total_mecanicos = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM ordenes_reparacion")
        total_ordenes = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COALESCE(SUM(cantidad_stock), 0) FROM repuestos"
        )
        repuestos_disponibles = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM alertas_mantenimiento")
        total_alertas = cursor.fetchone()[0]

        return {
            "clientes": total_clientes,
            "vehiculos": total_vehiculos,
            "mecanicos": total_mecanicos,
            "ordenes": total_ordenes,
            "repuestos": repuestos_disponibles,
            "alertas": total_alertas
        }
    finally:
        conexion.close()
