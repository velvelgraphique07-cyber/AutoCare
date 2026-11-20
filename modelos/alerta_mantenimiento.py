
class AlertaMantenimiento:
    """
    Representa una alerta para recordar el mantenimiento
    preventivo de un vehículo.
    """

    def __init__(
        self,
        id_alerta,
        vehiculo,
        fecha,
        mensaje,
        kilometraje_programado
    ):
        self.id_alerta = id_alerta
        self.vehiculo = vehiculo
        self.fecha = fecha
        self.mensaje = mensaje
        self.kilometraje_programado = kilometraje_programado
        self.estado = "Pendiente"

    def marcar_completada(self):
        self.estado = "Completada"
        print("Alerta marcada como completada.")

    def mostrar_informacion(self):
        print("\n=== ALERTA DE MANTENIMIENTO ===")
        print("Número:", self.id_alerta)
        print("Vehículo:", self.vehiculo.marca, self.vehiculo.modelo)
        print("Fecha programada:", self.fecha)
        print("Mensaje:", self.mensaje)
        print("Kilometraje programado:", self.kilometraje_programado, "km")
        print("Estado:", self.estado)
