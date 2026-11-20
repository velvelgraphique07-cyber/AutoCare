
class DetalleReparacion:
    """
    Representa un trabajo específico dentro de una orden
    de reparación de AutoCare.
    """

    def __init__(
        self,
        id_detalle,
        orden,
        descripcion,
        cantidad_horas,
        costo_mano_obra
    ):
        self.id_detalle = id_detalle
        self.orden = orden
        self.descripcion = descripcion
        self.cantidad_horas = cantidad_horas
        self.costo_mano_obra = costo_mano_obra

    def calcular_costo(self):
        return self.cantidad_horas * self.costo_mano_obra

    def mostrar_informacion(self):
        print("\n=== DETALLE DE REPARACIÓN ===")
        print("Número:", self.id_detalle)
        print("Orden:", self.orden.id_orden)
        print("Descripción:", self.descripcion)
        print("Horas de trabajo:", self.cantidad_horas)
        print("Costo por hora: $", self.costo_mano_obra)
        print("Costo total: $", self.calcular_costo())
