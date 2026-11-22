import sqlite3
from tkinter import messagebox

from modelos.cliente import Cliente
from modelos.mecanico import Mecanico
from modelos.orden_reparacion import OrdenReparacion
from modelos.vehiculo import Vehiculo
from servicios.servicio_mecanicos import ServicioMecanicos
from servicios.servicio_reparaciones import ServicioReparaciones
from servicios.servicio_vehiculos import ServicioVehiculos

from interfaz.panel_crud import PanelCRUD


class PanelOrdenes(PanelCRUD):

    def __init__(self, parent):
        self.servicio = ServicioReparaciones()
        self.servicio_vehiculos = ServicioVehiculos()
        self.servicio_mecanicos = ServicioMecanicos()
        self.vehiculos = self.servicio_vehiculos.listar_vehiculos()
        self.mecanicos = self.servicio_mecanicos.listar_mecanicos()

        opciones_vehiculos = [
            "{} - {} {}".format(fila[0], fila[1], fila[2])
            for fila in self.vehiculos
        ]
        opciones_mecanicos = [
            "{} - {}".format(fila[0], fila[1]) for fila in self.mecanicos
        ]

        columnas = [
            ("ID", "id_orden", 70, 0),
            ("ID vehículo", "id_vehiculo", 90, 1),
            ("Vehículo", "vehiculo", 180, 2),
            ("Fecha", "fecha", 100, 3),
            ("Descripción", "descripcion", 260, 4),
            ("Estado", "estado", 110, 5),
            ("Mecánicos", "mecanicos", 180, 6)
        ]
        campos = [
            {"titulo": "ID", "clave": "id_orden", "tipo": "numero", "opciones": None},
            {"titulo": "Vehículo", "clave": "id_vehiculo", "tipo": "combo", "opciones": opciones_vehiculos},
            {"titulo": "Fecha", "clave": "fecha", "tipo": "texto", "opciones": None},
            {"titulo": "Descripción", "clave": "descripcion", "tipo": "texto_largo", "opciones": None},
            {"titulo": "Estado", "clave": "estado", "tipo": "combo", "opciones": ["Pendiente", "En proceso", "Completada", "Cancelada"]},
            {"titulo": "Mecánico inicial", "clave": "id_mecanico", "tipo": "combo", "opciones": opciones_mecanicos}
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
        nombres_vehiculos = {
            fila[0]: "{} {}".format(fila[1], fila[2])
            for fila in self.vehiculos
        }
        resultado = []
        for fila in self.servicio.listar_ordenes():
            mecanicos = self.servicio.listar_mecanicos_asignados(fila[0])
            nombres_mecanicos = ", ".join(item[1] for item in mecanicos)
            resultado.append((
                fila[0],
                fila[1],
                nombres_vehiculos.get(fila[1], ""),
                fila[2],
                fila[3],
                fila[4],
                nombres_mecanicos
            ))
        return resultado

    def crear_vehiculo(self, id_vehiculo):
        fila = self.servicio_vehiculos.buscar_vehiculo(id_vehiculo)
        if not fila:
            return None
        cliente = Cliente(fila[5], "", "", "")
        return Vehiculo(fila[0], fila[1], fila[2], fila[3], fila[4], cliente)

    def validar(self, datos):
        obligatorios = (
            "id_orden", "id_vehiculo", "fecha",
            "descripcion", "estado"
        )
        if any(not datos.get(clave) for clave in obligatorios):
            messagebox.showwarning(
                "Campos obligatorios",
                "Complete el ID, vehículo, fecha, descripción y estado."
            )
            return None

        try:
            id_orden = int(datos["id_orden"])
            id_vehiculo = int(datos["id_vehiculo"].split(" - ", 1)[0])
        except (ValueError, IndexError):
            messagebox.showwarning(
                "Dato inválido",
                "El ID y el vehículo deben tener valores válidos."
            )
            return None

        vehiculo = self.crear_vehiculo(id_vehiculo)
        if vehiculo is None:
            messagebox.showwarning(
                "Vehículo no válido",
                "Seleccione un vehículo registrado."
            )
            return None

        orden = OrdenReparacion(
            id_orden,
            vehiculo,
            datos["fecha"].strip(),
            datos["descripcion"].strip()
        )
        orden.cambiar_estado(datos["estado"])
        return orden

    def registrar(self, datos):
        orden = self.validar(datos)
        if orden is None:
            return False

        mecanico_texto = datos.get("id_mecanico")
        if mecanico_texto:
            try:
                id_mecanico = int(mecanico_texto.split(" - ", 1)[0])
            except (ValueError, IndexError):
                id_mecanico = None
            if id_mecanico is not None:
                fila = self.servicio_mecanicos.buscar_mecanico(id_mecanico)
                if fila:
                    mecanico = Mecanico(fila[0], fila[1], fila[2], fila[3])
                    mecanico.disponible = bool(fila[4])
                    orden.asignar_mecanico(mecanico)

        if not self.servicio.registrar_orden(orden):
            messagebox.showwarning(
                "Registro no realizado",
                "La orden ya existe o no pudo registrarse."
            )
            return False
        return True

    def actualizar(self, datos, fila):
        orden = self.validar(datos)
        if orden is None:
            return False
        if not self.servicio.actualizar_orden(orden):
            messagebox.showwarning(
                "Actualización no realizada",
                "No se encontró la orden seleccionada."
            )
            return False
        return True

    def eliminar(self, fila):
        try:
            if not self.servicio.eliminar_orden(int(fila[0])):
                messagebox.showwarning(
                    "Eliminación no realizada",
                    "No se encontró la orden seleccionada."
                )
                return False
            return True
        except sqlite3.IntegrityError:
            messagebox.showerror(
                "No se puede eliminar",
                "La orden tiene diagnósticos o detalles asociados."
            )
            return False

    def consultar(self, fila):
        messagebox.showinfo(
            "Detalle de la orden",
            "ID: {}\nVehículo: {}\nFecha: {}\nDescripción: {}\n"
            "Estado: {}\nMecánicos: {}".format(
                fila[0], fila[2], fila[3], fila[4], fila[5], fila[6]
            )
        )
