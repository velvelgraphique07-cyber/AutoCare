
class Repuesto:
    """
    Representa un repuesto disponible en el inventario
    del taller AutoCare.
    """

    def __init__(
        self,
        id_repuesto,
        nombre,
        descripcion,
        precio,
        cantidad_stock
    ):
        self.id_repuesto = id_repuesto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad_stock = cantidad_stock

    def actualizar_stock(self, cantidad):
        if self.cantidad_stock + cantidad >= 0:
            self.cantidad_stock += cantidad
            print("Stock actualizado correctamente.")
        else:
            print("Error: no hay suficiente stock.")

    def mostrar_informacion(self):
        print("\n=== INFORMACIÓN DEL REPUESTO ===")
        print("Código:", self.id_repuesto)
        print("Nombre:", self.nombre)
        print("Descripción:", self.descripcion)
        print("Precio: $", self.precio)
        print("Cantidad disponible:", self.cantidad_stock)
