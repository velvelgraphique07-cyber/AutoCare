
from repositories.mantenimientos import RepositorioMantenimientos
from repositories.alertas import RepositorioAlertas
from repositories.vehiculos import RepositorioVehiculos


class ServicioMantenimiento:

    def __init__(self):
        self.repositorio_mantenimientos = RepositorioMantenimientos()
        self.repositorio_alertas = RepositorioAlertas()
        self.repositorio_vehiculos = RepositorioVehiculos()

    def registrar_mantenimiento(self, mantenimiento):
        vehiculos = self.repositorio_vehiculos.listar()

        if not any(
            fila[0] == mantenimiento.vehiculo.id_vehiculo
            for fila in vehiculos
        ):
            print("Error: el vehículo no está registrado.")
            return False

        mantenimientos = self.repositorio_mantenimientos.listar()

        if any(
            fila[0] == mantenimiento.id_mantenimiento
            for fila in mantenimientos
        ):
            print("El mantenimiento ya está registrado.")
            return False

        self.repositorio_mantenimientos.registrar(mantenimiento)
        print("Mantenimiento registrado correctamente mediante el servicio.")
        return True

    def listar_mantenimientos(self):
        return self.repositorio_mantenimientos.listar()

    def registrar_alerta(self, alerta):
        vehiculos = self.repositorio_vehiculos.listar()

        if not any(
            fila[0] == alerta.vehiculo.id_vehiculo
            for fila in vehiculos
        ):
            print("Error: el vehículo no está registrado.")
            return False

        alertas = self.repositorio_alertas.listar()

        if any(fila[0] == alerta.id_alerta for fila in alertas):
            print("La alerta ya está registrada.")
            return False

        self.repositorio_alertas.registrar(alerta)
        print("Alerta registrada correctamente mediante el servicio.")
        return True

    def listar_alertas(self):
        return self.repositorio_alertas.listar()
