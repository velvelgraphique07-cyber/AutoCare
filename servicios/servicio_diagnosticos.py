
from repositories.diagnosticos import RepositorioDiagnosticos
from repositories.reparaciones import RepositorioReparaciones


class ServicioDiagnosticos:

    def __init__(self):
        self.repositorio = RepositorioDiagnosticos()
        self.repositorio_ordenes = RepositorioReparaciones()

    def registrar_diagnostico(self, diagnostico):
        orden = self.repositorio_ordenes.buscar_por_id(
            diagnostico.orden.id_orden
        )

        if not orden:
            print("Error: la orden de reparación no está registrada.")
            return False

        existente = self.repositorio.buscar_por_id(
            diagnostico.id_diagnostico
        )

        if existente:
            print("El diagnóstico ya está registrado.")
            return False

        self.repositorio.registrar(diagnostico)
        print("Diagnóstico registrado correctamente.")
        return True

    def listar_diagnosticos(self):
        return self.repositorio.listar()

    def buscar_diagnostico(self, id_diagnostico):
        return self.repositorio.buscar_por_id(id_diagnostico)

    def actualizar_diagnostico(self, diagnostico):
        orden = self.repositorio_ordenes.buscar_por_id(
            diagnostico.orden.id_orden
        )

        if not orden:
            print("Error: la orden de reparación no está registrada.")
            return False

        actualizado = self.repositorio.actualizar(diagnostico)

        if actualizado:
            print("Diagnóstico actualizado correctamente.")
        else:
            print("No se encontró el diagnóstico.")

        return actualizado

    def eliminar_diagnostico(self, id_diagnostico):
        eliminado = self.repositorio.eliminar(id_diagnostico)

        if eliminado:
            print("Diagnóstico eliminado correctamente.")
        else:
            print("No se encontró el diagnóstico.")

        return eliminado
