import sqlite3
from tkinter import messagebox

from modelos.cliente import Cliente
from modelos.diagnostico import Diagnostico
from modelos.orden_reparacion import OrdenReparacion
from modelos.vehiculo import Vehiculo
from servicios.servicio_diagnosticos import ServicioDiagnosticos
from servicios.servicio_reparaciones import ServicioReparaciones
from servicios.servicio_vehiculos import ServicioVehiculos

from interfaz.panel_crud import PanelCRUD


class PanelDiagnosticos(PanelCRUD):

    def __init__(self, parent):
        self.servicio = ServicioDiagnosticos()
        self.servicio_ordenes = ServicioReparaciones()
        self.servicio_vehiculos = ServicioVehiculos()
        self.ordenes = self.servicio_ordenes.listar_ordenes()
        opciones_ordenes = [
            "{} - Orden {}".format(fila[0], fila[0])
            for fila in self.ordenes
        ]

        columnas = [
            ("ID", "id_diagnostico", 70, 0),
            ("ID orden", "id_orden", 80, 1),
            ("Fecha", "fecha", 100, 2),
            ("Problema", "descripcion", 260, 3),
            ("Observaciones", "observaciones", 260, 4)
        ]
        campos = [
            {"titulo": "ID", "clave": "id_diagnostico", "tipo": "numero", "opciones": None},
            {"titulo": "Orden", "clave": "id_orden", "tipo": "combo", "opciones": opciones_ordenes},
            {"titulo": "Fecha", "clave": "fecha", "tipo": "texto", "opciones": None},
            {"titulo": "Problema detectado", "clave": "descripcion", "tipo": "texto_largo", "opciones": None},
            {"titulo": "Observaciones", "clave": "observaciones", "tipo": "texto_largo", "opciones": None}
        ]
        super().__init__(
            parent,
            columnas,
            self.servicio.listar_diagnosticos,
            campos,
            self.registrar,
            self.actualizar,
            self.eliminar,
            self.consultar
        )

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
            "id_diagnostico", "id_orden",
            "fecha", "descripcion", "observaciones"
        )
        if any(not datos.get(clave) for clave in obligatorios):
            messagebox.showwarning(
                "Campos obligatorios",
                "Complete todos los campos del formulario."
            )
            return None

        try:
            id_diagnostico = int(datos["id_diagnostico"])
            id_orden = int(datos["id_orden"].split(" - ", 1)[0])
        except (ValueError, IndexError):
            messagebox.showwarning(
                "Dato inválido",
                "El ID del diagnóstico y el ID de la orden deben ser válidos."
            )
            return None

        orden = self.crear_orden(id_orden)
        if orden is None:
            messagebox.showwarning(
                "Orden no válida",
                "Seleccione una orden existente."
            )
            return None

        return Diagnostico(
            id_diagnostico,
            orden,
            datos["fecha"].strip(),
            datos["descripcion"].strip(),
            datos["observaciones"].strip()
        )

    def registrar(self, datos):
        diagnostico = self.validar(datos)
        if diagnostico is None:
            return False
        try:
            if not self.servicio.registrar_diagnostico(diagnostico):
                messagebox.showwarning(
                    "Registro no realizado",
                    "El diagnóstico ya existe o la orden ya tiene diagnóstico."
                )
                return False
            return True
        except sqlite3.IntegrityError:
            messagebox.showerror(
                "Diagnóstico no registrado",
                "La orden seleccionada ya tiene un diagnóstico asociado."
            )
            return False

    def actualizar(self, datos, fila):
        diagnostico = self.validar(datos)
        if diagnostico is None:
            return False
        try:
            if not self.servicio.actualizar_diagnostico(diagnostico):
                messagebox.showwarning(
                    "Actualización no realizada",
                    "No se encontró el diagnóstico seleccionado."
                )
                return False
            return True
        except sqlite3.IntegrityError:
            messagebox.showerror(
                "Diagnóstico no actualizado",
                "La orden seleccionada ya tiene otro diagnóstico asociado."
            )
            return False

    def eliminar(self, fila):
        if not self.servicio.eliminar_diagnostico(int(fila[0])):
            messagebox.showwarning(
                "Eliminación no realizada",
                "No se encontró el diagnóstico seleccionado."
            )
            return False
        return True

    def consultar(self, fila):
        messagebox.showinfo(
            "Detalle del diagnóstico",
            "ID: {}\nID orden: {}\nFecha: {}\nProblema: {}\nObservaciones: {}".format(
                fila[0], fila[1], fila[2], fila[3], fila[4]
            )
        )
