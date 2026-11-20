
class Cliente:
    """
    Representa a un cliente del taller AutoCare.
    """

    def __init__(self, id_cliente, nombre, telefono, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def mostrar_informacion(self):
        print("=== INFORMACIÓN DEL CLIENTE ===")
        print("ID:", self.id_cliente)
        print("Nombre:", self.nombre)
        print("Teléfono:", self.telefono)
        print("Correo:", self.correo)
