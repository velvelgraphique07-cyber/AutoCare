
class Diagnostico:
    """
    Representa el diagnóstico técnico de un vehículo.
    """

    def __init__(self, id_diagnostico, orden, fecha, descripcion, observaciones):
        self.id_diagnostico = id_diagnostico
        self.orden = orden
        self.fecha = fecha
        self.descripcion = descripcion
        self.observaciones = observaciones

    def mostrar_informacion(self):
        print("\n=== DIAGNÓSTICO DEL VEHÍCULO ===")
        print("Número:", self.id_diagnostico)
        print("Orden:", self.orden.id_orden)
        print("Vehículo:", self.orden.vehiculo.marca,
              self.orden.vehiculo.modelo)
        print("Fecha:", self.fecha)
        print("Problema detectado:", self.descripcion)
        print("Observaciones:", self.observaciones)
