
from repositories.repuestos import RepositorioRepuestos


class ServicioInventario:

    def __init__(self):
        self.repositorio = RepositorioRepuestos()

    def registrar_repuesto(self, repuesto):
        existente = self.repositorio.buscar_por_id(
            repuesto.id_repuesto
        )

        if existente:
            print("El repuesto ya está registrado.")
            return False

        if repuesto.precio < 0 or repuesto.cantidad_stock < 0:
            print("Error: el precio y el stock no pueden ser negativos.")
            return False

        self.repositorio.registrar(repuesto)
        print("Repuesto registrado correctamente.")
        return True

    def listar_repuestos(self):
        return self.repositorio.listar()

    def buscar_repuesto(self, id_repuesto):
        return self.repositorio.buscar_por_id(id_repuesto)

    def actualizar_repuesto(self, repuesto):
        if repuesto.precio < 0 or repuesto.cantidad_stock < 0:
            print("Error: el precio y el stock no pueden ser negativos.")
            return False

        actualizado = self.repositorio.actualizar(repuesto)

        if actualizado:
            print("Repuesto actualizado correctamente.")
        else:
            print("No se encontró el repuesto.")

        return actualizado

    def actualizar_stock(self, id_repuesto, nueva_cantidad):
        if nueva_cantidad < 0:
            print("Error: el stock no puede ser negativo.")
            return False

        existente = self.repositorio.buscar_por_id(id_repuesto)

        if not existente:
            print("No se encontró el repuesto.")
            return False

        self.repositorio.actualizar_stock(
            id_repuesto,
            nueva_cantidad
        )

        return True

    def eliminar_repuesto(self, id_repuesto):
        eliminado = self.repositorio.eliminar(id_repuesto)

        if eliminado:
            print("Repuesto eliminado correctamente.")
        else:
            print("No se encontró el repuesto.")

        return eliminado
