
from repositories.vehiculos import RepositorioVehiculos
from repositories.clientes import RepositorioClientes


class ServicioVehiculos:

    def __init__(self):
        self.repositorio = RepositorioVehiculos()
        self.repositorio_clientes = RepositorioClientes()

    def registrar_vehiculo(self, vehiculo):
        cliente = self.repositorio_clientes.buscar_por_id(
            vehiculo.cliente.id_cliente
        )

        if not cliente:
            print("Error: el cliente no está registrado.")
            return False

        existente = self.repositorio.buscar_por_id(
            vehiculo.id_vehiculo
        )

        if existente:
            print("El vehículo ya está registrado.")
            return False

        self.repositorio.registrar(vehiculo)
        print("Vehículo registrado correctamente.")
        return True

    def listar_vehiculos(self):
        return self.repositorio.listar()

    def buscar_vehiculo(self, id_vehiculo):
        return self.repositorio.buscar_por_id(id_vehiculo)

    def actualizar_vehiculo(self, vehiculo):
        cliente = self.repositorio_clientes.buscar_por_id(
            vehiculo.cliente.id_cliente
        )

        if not cliente:
            print("Error: el cliente no está registrado.")
            return False

        actualizado = self.repositorio.actualizar(vehiculo)

        if actualizado:
            print("Vehículo actualizado correctamente.")
        else:
            print("No se encontró el vehículo.")

        return actualizado

    def eliminar_vehiculo(self, id_vehiculo):
        eliminado = self.repositorio.eliminar(id_vehiculo)

        if eliminado:
            print("Vehículo eliminado correctamente.")
        else:
            print("No se encontró el vehículo.")

        return eliminado
