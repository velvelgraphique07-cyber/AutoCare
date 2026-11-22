from tkinter import messagebox

from modelos.cliente import Cliente
from modelos.mantenimiento import Mantenimiento
from modelos.vehiculo import Vehiculo
from servicios.servicio_mantenimiento import ServicioMantenimiento
from servicios.servicio_vehiculos import ServicioVehiculos

from interfaz.panel_crud import PanelCRUD


class PanelMantenimientos(PanelCRUD):

    def __init__(self, parent):
        self.servicio = ServicioMantenimiento()
        self.servicio_vehiculos = ServicioVehiculos()
        self.vehiculos = self.servicio_vehiculos.listar_vehiculos()
        opciones_vehiculos = [
            "{} - {} {}".format(fila[0], fila[1], fila[2])
            for fila in self.vehiculos
        ]

        columnas = [
            ("ID", "id_mantenimiento", 70, 0),
            ("ID vehículo", "id_vehiculo", 90, 1),
            ("Vehículo", "vehiculo", 180, 2),
            ("Fecha", "fecha", 100, 3),
            ("Tipo", "tipo", 120, 4),
            ("Descripción", "descripcion", 220, 5),
            ("Kilometraje", "kilometraje", 100, 6),
            ("Estado", "estado", 110, 7)
        ]
        campos = [
            {"titulo": "ID", "clave": "id_mantenimiento", "tipo": "numero", "opciones": None},
            {"titulo": "Vehículo", "clave": "id_vehiculo", "tipo": "combo", "opciones": opciones_vehiculos},
            {"titulo": "Fecha", "clave": "fecha", "tipo": "texto", "opciones": None},
            {"titulo": "Tipo", "clave": "tipo", "tipo": "texto", "opciones": None},
            {"titulo": "Descripción", "clave": "descripcion", "tipo": "texto_largo", "opciones": None},
            {"titulo": "Kilometraje", "clave": "kilometraje", "tipo": "numero", "opciones": None},
            {"titulo": "Estado", "clave": "estado", "tipo": "combo", "opciones": ["Programado", "Completado", "Cancelado"]}
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
        for fila in self.servicio.listar_mantenimientos():
            resultado.append((
                fila[0],
                fila[1],
                nombres_vehiculos.get(fila[1], ""),
                fila[2],
                fila[3],
                fila[4],
                fila[5],
                fila[6]
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
            "id_mantenimiento", "id_vehiculo", "fecha",
            "tipo", "descripcion", "kilometraje", "estado"
        )
        if any(not datos.get(clave) for clave in obligatorios):
            messagebox.showwarning(
                "Campos obligatorios",
                "Complete todos los campos del formulario."
            )
            return None

        try:
            id_mantenimiento = int(datos["id_mantenimiento"])
            id_vehiculo = int(datos["id_vehiculo"].split(" - ", 1)[0])
            kilometraje = int(datos["kilometraje"])
            if kilometraje < 0:
                raise ValueError
        except (ValueError, IndexError):
            messagebox.showwarning(
                "Dato inválido",
                "El ID y el kilometraje deben ser números enteros no negativos."
            )
            return None

        vehiculo = self.crear_vehiculo(id_vehiculo)
        if vehiculo is None:
            messagebox.showwarning(
                "Vehículo no válido",
                "Seleccione un vehículo registrado."
            )
            return None

        mantenimiento = Mantenimiento(
            id_mantenimiento,
            vehiculo,
            datos["fecha"].strip(),
            datos["tipo"].strip(),
            datos["descripcion"].strip(),
            kilometraje
        )
        mantenimiento.cambiar_estado(datos["estado"])
        return mantenimiento

    def registrar(self, datos):
        mantenimiento = self.validar(datos)
        if mantenimiento is None:
            return False
        if not self.servicio.registrar_mantenimiento(mantenimiento):
            messagebox.showwarning(
                "Registro no realizado",
                "El mantenimiento ya existe o el vehículo no está registrado."
            )
            return False
        return True

    def actualizar(self, datos, fila):
        mantenimiento = self.validar(datos)
        if mantenimiento is None:
            return False
        if not self.servicio.actualizar_mantenimiento(mantenimiento):
            messagebox.showwarning(
                "Actualización no realizada",
                "No se encontró el mantenimiento seleccionado."
            )
            return False
        return True

    def eliminar(self, fila):
        if not self.servicio.eliminar_mantenimiento(int(fila[0])):
            messagebox.showwarning(
                "Eliminación no realizada",
                "No se encontró el mantenimiento seleccionado."
            )
            return False
        return True

    def consultar(self, fila):
        messagebox.showinfo(
            "Detalle del mantenimiento",
            "ID: {}\nVehículo: {}\nFecha: {}\nTipo: {}\n"
            "Descripción: {}\nKilometraje: {} km\nEstado: {}".format(
                fila[0], fila[2], fila[3], fila[4],
                fila[5], fila[6], fila[7]
            )
        )
