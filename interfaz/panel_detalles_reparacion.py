from tkinter import messagebox

from modelos.detalle_reparacion import DetalleReparacion
from modelos.cliente import Cliente
from modelos.orden_reparacion import OrdenReparacion
from modelos.vehiculo import Vehiculo
from servicios.servicio_detalles_reparacion import ServicioDetallesReparacion
from servicios.servicio_reparaciones import ServicioReparaciones
from servicios.servicio_vehiculos import ServicioVehiculos

from interfaz.panel_crud import PanelCRUD


class PanelDetallesReparacion(PanelCRUD):

    def __init__(self, parent):
        self.servicio = ServicioDetallesReparacion()
        self.servicio_ordenes = ServicioReparaciones()
        self.servicio_vehiculos = ServicioVehiculos()
        self.ordenes = self.servicio_ordenes.listar_ordenes()
        opciones_ordenes = [
            "{} - Orden {}".format(fila[0], fila[0])
            for fila in self.ordenes
        ]

        columnas = [
            ("ID", "id_detalle", 70, 0),
            ("ID orden", "id_orden", 80, 1),
            ("Descripción", "descripcion", 280, 2),
            ("Horas", "cantidad_horas", 90, 3),
            ("Costo/hora", "costo_mano_obra", 110, 4),
            ("Costo total", "costo_total", 110, 5)
        ]
        campos = [
            {"titulo": "ID", "clave": "id_detalle", "tipo": "numero", "opciones": None},
            {"titulo": "Orden", "clave": "id_orden", "tipo": "combo", "opciones": opciones_ordenes},
            {"titulo": "Descripción", "clave": "descripcion", "tipo": "texto_largo", "opciones": None},
            {"titulo": "Cantidad de horas", "clave": "cantidad_horas", "tipo": "numero", "opciones": None},
            {"titulo": "Costo por hora", "clave": "costo_mano_obra", "tipo": "numero", "opciones": None}
        ]
        super().__init__(
            parent,
            columnas,
            self.cargar,
            campos,
            self.registrar,
            self.actualizar,
            self.eliminar,
            self.consultar
        )

    def cargar(self):
        resultado = []
        for fila in self.servicio.listar_detalles():
            costo_total = float(fila[3]) * float(fila[4])
            resultado.append((
                fila[0], fila[1], fila[2],
                fila[3], fila[4], round(costo_total, 2)
            ))
        return resultado

    def crear_orden(self, id_orden):
        fila_orden = self.servicio_ordenes.buscar_orden(id_orden)
        if not fila_orden:
            return None

        fila_vehiculo = self.servicio_vehiculos.buscar_vehiculo(
            fila_orden[1]
        )
        if not fila_vehiculo:
            return None

        cliente = Cliente(fila_vehiculo[5], "", "", "")
        vehiculo = Vehiculo(
            fila_vehiculo[0],
            fila_vehiculo[1],
            fila_vehiculo[2],
            fila_vehiculo[3],
            fila_vehiculo[4],
            cliente
        )
        orden = OrdenReparacion(
            fila_orden[0],
            vehiculo,
            fila_orden[2],
            fila_orden[3]
        )
        orden.cambiar_estado(fila_orden[4])
        return orden

    def validar(self, datos):
        obligatorios = (
            "id_detalle", "id_orden", "descripcion",
            "cantidad_horas", "costo_mano_obra"
        )
        if any(not datos.get(clave) for clave in obligatorios):
            messagebox.showwarning(
                "Campos obligatorios",
                "Complete todos los campos del formulario."
            )
            return None

        try:
            id_detalle = int(datos["id_detalle"])
            id_orden = int(datos["id_orden"].split(" - ", 1)[0])
            horas = float(datos["cantidad_horas"])
            costo_hora = float(datos["costo_mano_obra"])
            if horas < 0 or costo_hora < 0:
                raise ValueError
        except (ValueError, IndexError):
            messagebox.showwarning(
                "Dato inválido",
                "Las horas y el costo deben ser números no negativos."
            )
            return None

        orden = self.crear_orden(id_orden)
        if orden is None:
            messagebox.showwarning(
                "Orden no válida",
                "Seleccione una orden existente."
            )
            return None

        return DetalleReparacion(
            id_detalle,
            orden,
            datos["descripcion"].strip(),
            horas,
            costo_hora
        )

    def registrar(self, datos):
        detalle = self.validar(datos)
        if detalle is None:
            return False
        if not self.servicio.registrar_detalle(detalle):
            messagebox.showwarning(
                "Registro no realizado",
                "El detalle ya existe o no pudo registrarse."
            )
            return False
        return True

    def actualizar(self, datos, fila):
        detalle = self.validar(datos)
        if detalle is None:
            return False
        if not self.servicio.actualizar_detalle(detalle):
            messagebox.showwarning(
                "Actualización no realizada",
                "No se encontró el detalle seleccionado."
            )
            return False
        return True

    def eliminar(self, fila):
        if not self.servicio.eliminar_detalle(int(fila[0])):
            messagebox.showwarning(
                "Eliminación no realizada",
                "No se encontró el detalle seleccionado."
            )
            return False
        return True

    def consultar(self, fila):
        messagebox.showinfo(
            "Detalle de reparación",
            "ID: {}\nID orden: {}\nDescripción: {}\nHoras: {}\n"
            "Costo por hora: {}\nCosto total: {}".format(*fila)
        )
