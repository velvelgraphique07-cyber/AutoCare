
class Vehiculo:
    """
    Representa un vehículo registrado en AutoCare.
    """

    def __init__(self, id_vehiculo, marca, modelo, patente, anio, cliente):
        self.id_vehiculo = id_vehiculo
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.anio = anio
        self.cliente = cliente

    def mostrar_informacion(self):
        print("=== INFORMACIÓN DEL VEHÍCULO ===")
        print("ID:", self.id_vehiculo)
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Patente:", self.patente)
        print("Año:", self.anio)
        print("Propietario:", self.cliente.nombre)
