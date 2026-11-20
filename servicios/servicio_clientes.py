
from repositories.clientes import RepositorioClientes


class ServicioClientes:

    def __init__(self):
        self.repositorio = RepositorioClientes()

    def registrar_cliente(self, cliente):
        clientes = self.repositorio.listar()

        if any(fila[0] == cliente.id_cliente for fila in clientes):
            print("El cliente ya está registrado.")
            return False

        self.repositorio.registrar(cliente)
        print("Cliente registrado correctamente mediante el servicio.")
        return True

    def listar_clientes(self):
        return self.repositorio.listar()
