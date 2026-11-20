
class OrdenReparacion:
    """
    Representa una orden de reparación de AutoCare.
    """

    def __init__(self, id_orden, vehiculo, fecha, descripcion):
        self.id_orden = id_orden
        self.vehiculo = vehiculo
        self.fecha = fecha
        self.descripcion = descripcion
        self.mecanicos = []
        self.estado = "Pendiente"

    def asignar_mecanico(self, mecanico):
        if mecanico not in self.mecanicos:
            self.mecanicos.append(mecanico)
            print("Mecánico asignado correctamente.")
        else:
            print("Este mecánico ya está asignado.")

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_informacion(self):
        print("\n=== ORDEN DE REPARACIÓN ===")
        print("Número:", self.id_orden)
        print("Vehículo:", self.vehiculo.marca, self.vehiculo.modelo)
        print("Fecha:", self.fecha)
        print("Descripción:", self.descripcion)
        print("Estado:", self.estado)

        print("Mecánicos asignados:")
        for mecanico in self.mecanicos:
            print("-", mecanico.nombre)
