
from repositories.mantenimientos import RepositorioMantenimientos
from repositories.alertas import RepositorioAlertas
from repositories.vehiculos import RepositorioVehiculos


class ServicioMantenimiento:

    def __init__(self):
        self.repositorio_mantenimientos = RepositorioMantenimientos()
        self.repositorio_alertas = RepositorioAlertas()
        self.repositorio_vehiculos = RepositorioVehiculos()

    def registrar_mantenimiento(self, mantenimiento):
        vehiculo = self.repositorio_vehiculos.buscar_por_id(
            mantenimiento.vehiculo.id_vehiculo
        )

        if not vehiculo:
            print("Error: el vehículo no está registrado.")
            return False

        existente = self.repositorio_mantenimientos.buscar_por_id(
            mantenimiento.id_mantenimiento
        )

        if existente:
            print("El mantenimiento ya está registrado.")
            return False

        self.repositorio_mantenimientos.registrar(mantenimiento)
        print("Mantenimiento registrado correctamente.")
        return True

    def listar_mantenimientos(self):
        return self.repositorio_mantenimientos.listar()

    def buscar_mantenimiento(self, id_mantenimiento):
        return self.repositorio_mantenimientos.buscar_por_id(
            id_mantenimiento
        )

    def actualizar_mantenimiento(self, mantenimiento):
        vehiculo = self.repositorio_vehiculos.buscar_por_id(
            mantenimiento.vehiculo.id_vehiculo
        )

        if not vehiculo:
            print("Error: el vehículo no está registrado.")
            return False

        actualizado = self.repositorio_mantenimientos.actualizar(
            mantenimiento
        )

        if actualizado:
            print("Mantenimiento actualizado correctamente.")
        else:
            print("No se encontró el mantenimiento.")

        return actualizado

    def eliminar_mantenimiento(self, id_mantenimiento):
        eliminado = self.repositorio_mantenimientos.eliminar(
            id_mantenimiento
        )

        if eliminado:
            print("Mantenimiento eliminado correctamente.")
        else:
            print("No se encontró el mantenimiento.")

        return eliminado

    def registrar_alerta(self, alerta):
        vehiculo = self.repositorio_vehiculos.buscar_por_id(
            alerta.vehiculo.id_vehiculo
        )

        if not vehiculo:
            print("Error: el vehículo no está registrado.")
            return False

        alertas = self.repositorio_alertas.listar()

        if any(fila[0] == alerta.id_alerta for fila in alertas):
            print("La alerta ya está registrada.")
            return False

        self.repositorio_alertas.registrar(alerta)
        print("Alerta registrada correctamente.")
        return True

    def listar_alertas(self):
        return self.repositorio_alertas.listar()
    
    def buscar_alerta(self, id_alerta):
        return self.repositorio_alertas.buscar_por_id(id_alerta)

    def actualizar_alerta(self, alerta):
        vehiculo = self.repositorio_vehiculos.buscar_por_id(
            alerta.vehiculo.id_vehiculo
        )

        if not vehiculo:
            print("Error: el vehículo no está registrado.")
            return False

        actualizado = self.repositorio_alertas.actualizar(alerta)

        if actualizado:
            print("Alerta actualizada correctamente.")
        else:
            print("No se encontró la alerta.")

        return actualizado

    def eliminar_alerta(self, id_alerta):
        eliminado = self.repositorio_alertas.eliminar(id_alerta)

        if eliminado:
            print("Alerta eliminada correctamente.")
        else:
            print("No se encontró la alerta.")

        return eliminado

