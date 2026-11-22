from tkinter import messagebox

from modelos.alerta_mantenimiento import AlertaMantenimiento
from modelos.cliente import Cliente
from modelos.vehiculo import Vehiculo
from servicios.servicio_mantenimiento import ServicioMantenimiento
from servicios.servicio_vehiculos import ServicioVehiculos

from interfaz.panel_crud import PanelCRUD


class PanelAlertas(PanelCRUD):

    def __init__(self, parent):
        self.servicio = ServicioMantenimiento()
        self.servicio_vehiculos = ServicioVehiculos()
        self.vehiculos = self.servicio_vehiculos.listar_vehiculos()
        opciones_vehiculos = [
            "{} - {} {}".format(fila[0], fila[1], fila[2])
            for fila in self.vehiculos
        ]

        columnas = [
            ("ID", "id_alerta", 70, 0),
            ("ID vehículo", "id_vehiculo", 90, 1),
            ("Vehículo", "vehiculo", 180, 2),
            ("Fecha", "fecha", 100, 3),
            ("Mensaje", "mensaje", 260, 4),
            ("Km programado", "kilometraje_programado", 120, 5),
            ("Estado", "estado", 110, 6)
        ]
        campos = [
            {"titulo": "ID", "clave": "id_alerta", "tipo": "numero", "opciones": None},
            {"titulo": "Vehículo", "clave": "id_vehiculo", "tipo": "combo", "opciones": opciones_vehiculos},
            {"titulo": "Fecha programada", "clave": "fecha", "tipo": "texto", "opciones": None},
            {"titulo": "Mensaje", "clave": "mensaje", "tipo": "texto_largo", "opciones": None},
            {"titulo": "Kilometraje programado", "clave": "kilometraje_programado", "tipo": "numero", "opciones": None},
            {"titulo": "Estado", "clave": "estado", "tipo": "combo", "opciones": ["Pendiente", "Completada"]}
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
        for fila in self.servicio.listar_alertas():
            resultado.append((
                fila[0],
                fila[1],
                nombres_vehiculos.get(fila[1], ""),
                fila[2],
                fila[3],
                fila[4],
                fila[5]
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
            "id_alerta", "id_vehiculo", "fecha",
            "mensaje", "kilometraje_programado", "estado"
        )
        if any(not datos.get(clave) for clave in obligatorios):
            messagebox.showwarning(
                "Campos obligatorios",
                "Complete todos los campos del formulario."
            )
            return None

        try:
            id_alerta = int(datos["id_alerta"])
            id_vehiculo = int(datos["id_vehiculo"].split(" - ", 1)[0])
            kilometraje = int(datos["kilometraje_programado"])
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

        alerta = AlertaMantenimiento(
            id_alerta,
            vehiculo,
            datos["fecha"].strip(),
            datos["mensaje"].strip(),
            kilometraje
        )
        if datos["estado"] == "Completada":
            alerta.marcar_completada()
        else:
            alerta.estado = "Pendiente"
        return alerta

    def registrar(self, datos):
        alerta = self.validar(datos)
        if alerta is None:
            return False
        if not self.servicio.registrar_alerta(alerta):
            messagebox.showwarning(
                "Registro no realizado",
                "La alerta ya existe o el vehículo no está registrado."
            )
            return False
        return True

    def actualizar(self, datos, fila):
        alerta = self.validar(datos)
        if alerta is None:
            return False
        if not self.servicio.actualizar_alerta(alerta):
            messagebox.showwarning(
                "Actualización no realizada",
                "No se encontró la alerta seleccionada."
            )
            return False
        return True

    def eliminar(self, fila):
        if not self.servicio.eliminar_alerta(int(fila[0])):
            messagebox.showwarning(
                "Eliminación no realizada",
                "No se encontró la alerta seleccionada."
            )
            return False
        return True

    def consultar(self, fila):
        messagebox.showinfo(
            "Detalle de la alerta",
            "ID: {}\nVehículo: {}\nFecha: {}\nMensaje: {}\n"
            "Kilometraje: {} km\nEstado: {}".format(
                fila[0], fila[2], fila[3], fila[4], fila[5], fila[6]
            )
        )
