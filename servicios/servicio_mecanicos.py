
from repositories.mecanicos import RepositorioMecanicos


class ServicioMecanicos:

    def __init__(self):
        self.repositorio = RepositorioMecanicos()

    def registrar_mecanico(self, mecanico):
        existente = self.repositorio.buscar_por_id(
            mecanico.id_mecanico
        )

        if existente:
            print("El mecánico ya está registrado.")
            return False

        self.repositorio.registrar(mecanico)
        print("Mecánico registrado correctamente.")
        return True

    def listar_mecanicos(self):
        return self.repositorio.listar()

    def buscar_mecanico(self, id_mecanico):
        return self.repositorio.buscar_por_id(id_mecanico)

    def actualizar_mecanico(self, mecanico):
        actualizado = self.repositorio.actualizar(mecanico)

        if actualizado:
            print("Mecánico actualizado correctamente.")
        else:
            print("No se encontró el mecánico.")

        return actualizado

    def eliminar_mecanico(self, id_mecanico):
        eliminado = self.repositorio.eliminar(id_mecanico)

        if eliminado:
            print("Mecánico eliminado correctamente.")
        else:
            print("No se encontró el mecánico.")

        return eliminado
