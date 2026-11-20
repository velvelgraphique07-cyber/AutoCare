
from repositories.clientes import RepositorioClientes


class ServicioClientes:

    def __init__(self):
        self.repositorio = RepositorioClientes()

    def registrar_cliente(self, cliente):
        existente = self.repositorio.buscar_por_id(cliente.id_cliente)

        if existente:
            print("El cliente ya está registrado.")
            return False

        self.repositorio.registrar(cliente)
        print("Cliente registrado correctamente.")
        return True

    def listar_clientes(self):
        return self.repositorio.listar()

    def buscar_cliente(self, id_cliente):
        return self.repositorio.buscar_por_id(id_cliente)

    def actualizar_cliente(self, cliente):
        actualizado = self.repositorio.actualizar(cliente)

        if actualizado:
            print("Cliente actualizado correctamente.")
        else:
            print("No se encontró el cliente.")

        return actualizado

    def eliminar_cliente(self, id_cliente):
        eliminado = self.repositorio.eliminar(id_cliente)

        if eliminado:
            print("Cliente eliminado correctamente.")
        else:
            print("No se encontró el cliente.")

        return eliminado
