
from repositories.detalles_reparacion import RepositorioDetallesReparacion
from repositories.reparaciones import RepositorioReparaciones


class ServicioDetallesReparacion:

    def __init__(self):
        self.repositorio = RepositorioDetallesReparacion()
        self.repositorio_ordenes = RepositorioReparaciones()

    def registrar_detalle(self, detalle):
        orden = self.repositorio_ordenes.buscar_por_id(
            detalle.orden.id_orden
        )

        if not orden:
            print("Error: la orden de reparación no está registrada.")
            return False

        existente = self.repositorio.buscar_por_id(
            detalle.id_detalle
        )

        if existente:
            print("El detalle de reparación ya está registrado.")
            return False

        self.repositorio.registrar(detalle)
        print("Detalle de reparación registrado correctamente.")
        return True

    def listar_detalles(self):
        return self.repositorio.listar()

    def buscar_detalle(self, id_detalle):
        return self.repositorio.buscar_por_id(id_detalle)

    def actualizar_detalle(self, detalle):
        orden = self.repositorio_ordenes.buscar_por_id(
            detalle.orden.id_orden
        )

        if not orden:
            print("Error: la orden de reparación no está registrada.")
            return False

        actualizado = self.repositorio.actualizar(detalle)

        if actualizado:
            print("Detalle de reparación actualizado correctamente.")
        else:
            print("No se encontró el detalle de reparación.")

        return actualizado

    def eliminar_detalle(self, id_detalle):
        eliminado = self.repositorio.eliminar(id_detalle)

        if eliminado:
            print("Detalle de reparación eliminado correctamente.")
        else:
            print("No se encontró el detalle de reparación.")

        return eliminado
