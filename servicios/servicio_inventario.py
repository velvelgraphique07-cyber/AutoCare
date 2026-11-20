
from repositories.repuestos import RepositorioRepuestos


class ServicioInventario:

    def __init__(self):
        self.repositorio = RepositorioRepuestos()

    def registrar_repuesto(self, repuesto):
        repuestos = self.repositorio.listar()

        if any(fila[0] == repuesto.id_repuesto for fila in repuestos):
            print("El repuesto ya está registrado.")
            return False

        self.repositorio.registrar(repuesto)
        print("Repuesto registrado correctamente mediante el servicio.")
        return True

    def listar_repuestos(self):
        return self.repositorio.listar()

    def actualizar_stock(self, id_repuesto, nueva_cantidad):
        if nueva_cantidad < 0:
            print("Error: el stock no puede ser negativo.")
            return False

        return self.repositorio.actualizar_stock(
            id_repuesto,
            nueva_cantidad
        )
