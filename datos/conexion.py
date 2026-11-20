
import sqlite3


def conectar():
    """
    Establece la conexión con la base de datos AutoCare.
    """

    conexion = sqlite3.connect("autocare.db")

    # Activar las claves foráneas de SQLite
    conexion.execute("PRAGMA foreign_keys = ON")

    return conexion
