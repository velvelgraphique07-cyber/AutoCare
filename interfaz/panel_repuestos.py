from tkinter import messagebox

from modelos.repuesto import Repuesto
from servicios.servicio_inventario import ServicioInventario

from interfaz.panel_crud import PanelCRUD


class PanelRepuestos(PanelCRUD):

    def __init__(self, parent):
        self.servicio = ServicioInventario()
        columnas = [
            ("ID", "id_repuesto", 70, 0),
            ("Nombre", "nombre", 180, 1),
            ("Descripción", "descripcion", 280, 2),
            ("Precio", "precio", 100, 3),
            ("Stock", "cantidad_stock", 100, 4)
        ]
        campos = [
            {"titulo": "ID", "clave": "id_repuesto", "tipo": "numero", "opciones": None},
            {"titulo": "Nombre", "clave": "nombre", "tipo": "texto", "opciones": None},
            {"titulo": "Descripción", "clave": "descripcion", "tipo": "texto_largo", "opciones": None},
            {"titulo": "Precio", "clave": "precio", "tipo": "numero", "opciones": None},
            {"titulo": "Cantidad en stock", "clave": "cantidad_stock", "tipo": "numero", "opciones": None}
        ]
        super().__init__(
            parent,
            columnas,
            self.servicio.listar_repuestos,
            campos,
            self.registrar,
            self.actualizar,
            self.eliminar,
            self.consultar
        )

    def validar(self, datos):
        obligatorios = (
            "id_repuesto", "nombre",
            "descripcion", "precio", "cantidad_stock"
        )
        if any(not datos.get(clave) for clave in obligatorios):
            messagebox.showwarning(
                "Campos obligatorios",
                "Complete todos los campos del formulario."
            )
            return None

        try:
            id_repuesto = int(datos["id_repuesto"])
            precio = float(datos["precio"])
            stock = int(datos["cantidad_stock"])
            if precio < 0 or stock < 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Dato inválido",
                "El ID y el stock deben ser enteros; el precio no puede ser negativo."
            )
            return None

        return Repuesto(
            id_repuesto,
            datos["nombre"].strip(),
            datos["descripcion"].strip(),
            precio,
            stock
        )

    def registrar(self, datos):
        repuesto = self.validar(datos)
        if repuesto is None:
            return False
        if not self.servicio.registrar_repuesto(repuesto):
            messagebox.showwarning(
                "Registro no realizado",
                "El repuesto ya existe, el stock o el precio son negativos."
            )
            return False
        return True

    def actualizar(self, datos, fila):
        repuesto = self.validar(datos)
        if repuesto is None:
            return False
        if not self.servicio.actualizar_repuesto(repuesto):
            messagebox.showwarning(
                "Actualización no realizada",
                "No se encontró el repuesto seleccionado."
            )
            return False
        return True

    def eliminar(self, fila):
        if not self.servicio.eliminar_repuesto(int(fila[0])):
            messagebox.showwarning(
                "Eliminación no realizada",
                "No se encontró el repuesto seleccionado."
            )
            return False
        return True

    def consultar(self, fila):
        messagebox.showinfo(
            "Detalle del repuesto",
            "ID: {}\nNombre: {}\nDescripción: {}\nPrecio: {}\nStock: {}".format(*fila)
        )
