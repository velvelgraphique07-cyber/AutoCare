
class Mantenimiento:
    """
    Representa un mantenimiento realizado o programado
    para un vehículo en AutoCare.
    """

    def __init__(
        self,
        id_mantenimiento,
        vehiculo,
        fecha,
        tipo,
        descripcion,
        kilometraje
    ):
        self.id_mantenimiento = id_mantenimiento
        self.vehiculo = vehiculo
        self.fecha = fecha
        self.tipo = tipo
        self.descripcion = descripcion
        self.kilometraje = kilometraje
        self.estado = "Programado"

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_informacion(self):
        print("\n=== MANTENIMIENTO DEL VEHÍCULO ===")
        print("Número:", self.id_mantenimiento)
        print("Vehículo:", self.vehiculo.marca, self.vehiculo.modelo)
        print("Fecha:", self.fecha)
        print("Tipo:", self.tipo)
        print("Descripción:", self.descripcion)
        print("Kilometraje:", self.kilometraje, "km")
        print("Estado:", self.estado)
