
from datos.conexion import conectar


def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    # TABLA CLIENTES
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            correo TEXT NOT NULL
        )
    """)

    # TABLA VEHICULOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehiculos (
            id_vehiculo INTEGER PRIMARY KEY,
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            patente TEXT NOT NULL,
            anio INTEGER NOT NULL,
            id_cliente INTEGER NOT NULL,
            FOREIGN KEY (id_cliente)
                REFERENCES clientes(id_cliente)
        )
    """)

    # TABLA MECANICOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mecanicos (
            id_mecanico INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            especialidad TEXT NOT NULL,
            telefono TEXT NOT NULL,
            disponible INTEGER NOT NULL
        )
    """)

    # TABLA ORDENES DE REPARACION
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ordenes_reparacion (
            id_orden INTEGER PRIMARY KEY,
            id_vehiculo INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            estado TEXT NOT NULL,
            FOREIGN KEY (id_vehiculo)
                REFERENCES vehiculos(id_vehiculo)
        )
    """)

    # TABLA RELACION ORDENES Y MECANICOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orden_mecanicos (
            id_orden INTEGER NOT NULL,
            id_mecanico INTEGER NOT NULL,
            PRIMARY KEY (id_orden, id_mecanico),
            FOREIGN KEY (id_orden)
                REFERENCES ordenes_reparacion(id_orden),
            FOREIGN KEY (id_mecanico)
                REFERENCES mecanicos(id_mecanico)
        )
    """)

    # TABLA DIAGNOSTICOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS diagnosticos (
            id_diagnostico INTEGER PRIMARY KEY,
            id_orden INTEGER NOT NULL UNIQUE,
            fecha TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            observaciones TEXT NOT NULL,
            FOREIGN KEY (id_orden)
                REFERENCES ordenes_reparacion(id_orden)
        )
    """)
    # TABLA MANTENIMIENTOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mantenimientos (
            id_mantenimiento INTEGER PRIMARY KEY,
            id_vehiculo INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            tipo TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            kilometraje INTEGER NOT NULL,
            estado TEXT NOT NULL,
            FOREIGN KEY (id_vehiculo)
                REFERENCES vehiculos(id_vehiculo)
        )
    """)
# TABLA DETALLES DE REPARACION
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS detalles_reparacion (
            id_detalle INTEGER PRIMARY KEY,
            id_orden INTEGER NOT NULL,
            descripcion TEXT NOT NULL,
            cantidad_horas REAL NOT NULL,
            costo_mano_obra REAL NOT NULL,
            FOREIGN KEY (id_orden)
                REFERENCES ordenes_reparacion(id_orden)
        )
    """)

    # TABLA REPUESTOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS repuestos (
            id_repuesto INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            precio REAL NOT NULL,
            cantidad_stock INTEGER NOT NULL
        )
    """)
    # TABLA ALERTAS DE MANTENIMIENTO
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alertas_mantenimiento (
            id_alerta INTEGER PRIMARY KEY,
            id_vehiculo INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            mensaje TEXT NOT NULL,
            kilometraje_programado INTEGER NOT NULL,
            estado TEXT NOT NULL,
            FOREIGN KEY (id_vehiculo)
                REFERENCES vehiculos(id_vehiculo)
        )
    """)
    conexion.commit()
    conexion.close()

    print("Tablas iniciales creadas correctamente.")
