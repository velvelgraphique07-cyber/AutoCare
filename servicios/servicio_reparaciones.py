
from repositories.reparaciones import RepositorioReparaciones
from repositories.vehiculos import RepositorioVehiculos


class ServicioReparaciones:

    def __init__(self):
        self.repositorio = RepositorioReparaciones()
        self.repositorio_vehiculos = RepositorioVehiculos()

    def registrar_orden(self, orden):
        vehiculos = self.repositorio_vehiculos.listar()

        if not any(
            fila[0] == orden.vehiculo.id_vehiculo
            for fila in vehiculos
        ):
            print("Error: el vehículo no está registrado.")
            return False

        ordenes = self.repositorio.listar()

        if any(fila[0] == orden.id_orden for fila in ordenes):
            print("La orden de reparación ya está registrada.")
            return False

        self.repositorio.registrar(orden)
        print("Orden registrada correctamente mediante el servicio.")
        return True

    def listar_ordenes(self):
        return self.repositorio.listar()
