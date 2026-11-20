
from repositories.reparaciones import RepositorioReparaciones
from repositories.vehiculos import RepositorioVehiculos


class ServicioReparaciones:

    def __init__(self):
        self.repositorio = RepositorioReparaciones()
        self.repositorio_vehiculos = RepositorioVehiculos()

    def registrar_orden(self, orden):
        vehiculo = self.repositorio_vehiculos.buscar_por_id(
            orden.vehiculo.id_vehiculo
        )

        if not vehiculo:
            print("Error: el vehículo no está registrado.")
            return False

        existente = self.repositorio.buscar_por_id(
            orden.id_orden
        )

        if existente:
            print("La orden de reparación ya está registrada.")
            return False

        self.repositorio.registrar(orden)
        print("Orden registrada correctamente.")
        return True

    def listar_ordenes(self):
        return self.repositorio.listar()

    def buscar_orden(self, id_orden):
        return self.repositorio.buscar_por_id(id_orden)

    def listar_mecanicos_asignados(self, id_orden):
        return self.repositorio.listar_mecanicos(id_orden)

    def actualizar_orden(self, orden):
        vehiculo = self.repositorio_vehiculos.buscar_por_id(
            orden.vehiculo.id_vehiculo
        )

        if not vehiculo:
            print("Error: el vehículo no está registrado.")
            return False

        actualizado = self.repositorio.actualizar(orden)

        if actualizado:
            print("Orden actualizada correctamente.")
        else:
            print("No se encontró la orden.")

        return actualizado

    def eliminar_orden(self, id_orden):
        eliminado = self.repositorio.eliminar(id_orden)

        if eliminado:
            print("Orden eliminada correctamente.")
        else:
            print("No se encontró la orden.")

        return eliminado
