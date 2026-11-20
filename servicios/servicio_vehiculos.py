
from repositories.vehiculos import RepositorioVehiculos
from repositories.clientes import RepositorioClientes


class ServicioVehiculos:

    def __init__(self):
        self.repositorio = RepositorioVehiculos()
        self.repositorio_clientes = RepositorioClientes()

    def registrar_vehiculo(self, vehiculo):
        clientes = self.repositorio_clientes.listar()

        if not any(
            fila[0] == vehiculo.cliente.id_cliente
            for fila in clientes
        ):
            print("Error: el cliente no está registrado.")
            return False

        vehiculos = self.repositorio.listar()

        if any(fila[0] == vehiculo.id_vehiculo for fila in vehiculos):
            print("El vehículo ya está registrado.")
            return False

        self.repositorio.registrar(vehiculo)
        print("Vehículo registrado correctamente mediante el servicio.")
        return True

    def listar_vehiculos(self):
        return self.repositorio.listar()
