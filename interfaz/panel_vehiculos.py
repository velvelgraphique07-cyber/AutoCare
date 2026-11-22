import sqlite3
from tkinter import messagebox

from modelos.cliente import Cliente
from modelos.vehiculo import Vehiculo
from servicios.servicio_clientes import ServicioClientes
from servicios.servicio_vehiculos import ServicioVehiculos

from interfaz.panel_crud import PanelCRUD


class PanelVehiculos(PanelCRUD):

    def __init__(self, parent):
        self.servicio = ServicioVehiculos()
        self.servicio_clientes = ServicioClientes()

        self.clientes = self.servicio_clientes.listar_clientes()
        opciones_clientes = [
            "{} - {}".format(fila[0], fila[1]) for fila in self.clientes
        ]

        columnas = [
            ("ID", "id_vehiculo", 70, 0),
            ("Marca", "marca", 130, 1),
            ("Modelo", "modelo", 150, 2),
            ("Patente", "patente", 100, 3),
            ("Año", "anio", 70, 4),
            ("ID cliente", "id_cliente", 90, 5),
            ("Propietario", "propietario", 180, 6)
        ]
        campos = [
            {"titulo": "ID", "clave": "id_vehiculo", "tipo": "numero", "opciones": None},
            {"titulo": "Marca", "clave": "marca", "tipo": "texto", "opciones": None},
            {"titulo": "Modelo", "clave": "modelo", "tipo": "texto", "opciones": None},
            {"titulo": "Patente", "clave": "patente", "tipo": "texto", "opciones": None},
            {"titulo": "Año", "clave": "anio", "tipo": "numero", "opciones": None},
            {"titulo": "Propietario", "clave": "id_cliente", "tipo": "combo", "opciones": opciones_clientes}
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
        nombres = {fila[0]: fila[1] for fila in self.clientes}
        resultado = []
        for fila in self.servicio.listar_vehiculos():
            resultado.append((
                fila[0], fila[1], fila[2], fila[3],
                fila[4], fila[5], nombres.get(fila[5], "")
            ))
        return resultado

    def validar(self, datos):
        obligatorios = (
            "id_vehiculo", "marca", "modelo",
            "patente", "anio", "id_cliente"
        )
        if any(not datos.get(clave) for clave in obligatorios):
            messagebox.showwarning(
                "Campos obligatorios",
                "Complete todos los campos del formulario."
            )
            return None

        try:
            id_vehiculo = int(datos["id_vehiculo"])
            anio = int(datos["anio"])
            id_cliente = int(datos["id_cliente"].split(" - ", 1)[0])
        except (ValueError, IndexError):
            messagebox.showwarning(
                "Dato inválido",
                "ID, año y propietario deben tener valores válidos."
            )
            return None

        cliente = Cliente(id_cliente, "", "", "")
        return Vehiculo(
            id_vehiculo,
            datos["marca"].strip(),
            datos["modelo"].strip(),
            datos["patente"].strip(),
            anio,
            cliente
        )

    def registrar(self, datos):
        vehiculo = self.validar(datos)
        if vehiculo is None:
            return False
        if not self.servicio.registrar_vehiculo(vehiculo):
            messagebox.showwarning(
                "Registro no realizado",
                "El vehículo ya existe o el propietario no está registrado."
            )
            return False
        return True

    def actualizar(self, datos, fila):
        vehiculo = self.validar(datos)
        if vehiculo is None:
            return False
        if not self.servicio.actualizar_vehiculo(vehiculo):
            messagebox.showwarning(
                "Actualización no realizada",
                "No se encontró el vehículo o el propietario no existe."
            )
            return False
        return True

    def eliminar(self, fila):
        try:
            if not self.servicio.eliminar_vehiculo(int(fila[0])):
                messagebox.showwarning(
                    "Eliminación no realizada",
                    "No se encontró el vehículo seleccionado."
                )
                return False
            return True
        except sqlite3.IntegrityError:
            messagebox.showerror(
                "No se puede eliminar",
                "El vehículo tiene órdenes o mantenimientos asociados."
            )
            return False

    def consultar(self, fila):
        messagebox.showinfo(
            "Detalle del vehículo",
            "ID: {}\nMarca: {}\nModelo: {}\nPatente: {}\nAño: {}\n"
            "ID cliente: {}\nPropietario: {}".format(*fila)
        )
