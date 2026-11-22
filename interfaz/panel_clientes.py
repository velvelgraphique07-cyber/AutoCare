import sqlite3
from tkinter import messagebox

from modelos.cliente import Cliente
from servicios.servicio_clientes import ServicioClientes

from interfaz.panel_crud import PanelCRUD


class PanelClientes(PanelCRUD):

    def __init__(self, parent):
        self.servicio = ServicioClientes()
        columnas = [
            ("ID", "id_cliente", 80, 0),
            ("Nombre", "nombre", 220, 1),
            ("Teléfono", "telefono", 150, 2),
            ("Correo", "correo", 220, 3)
        ]
        campos = [
            {"titulo": "ID", "clave": "id_cliente", "tipo": "numero", "opciones": None},
            {"titulo": "Nombre", "clave": "nombre", "tipo": "texto", "opciones": None},
            {"titulo": "Teléfono", "clave": "telefono", "tipo": "texto", "opciones": None},
            {"titulo": "Correo", "clave": "correo", "tipo": "texto", "opciones": None}
        ]
        super().__init__(
            parent,
            columnas,
            self.servicio.listar_clientes,
            campos,
            self.registrar,
            self.actualizar,
            self.eliminar,
            self.consultar
        )

    def validar(self, datos):
        obligatorios = ("id_cliente", "nombre", "telefono", "correo")
        if any(not datos.get(clave) for clave in obligatorios):
            messagebox.showwarning(
                "Campos obligatorios",
                "Complete todos los campos del formulario."
            )
            return None

        try:
            id_cliente = int(datos["id_cliente"])
        except ValueError:
            messagebox.showwarning(
                "Dato inválido",
                "El ID debe ser un número entero."
            )
            return None

        return Cliente(
            id_cliente,
            datos["nombre"].strip(),
            datos["telefono"].strip(),
            datos["correo"].strip()
        )

    def registrar(self, datos):
        cliente = self.validar(datos)
        if cliente is None:
            return False
        if not self.servicio.registrar_cliente(cliente):
            messagebox.showwarning(
                "Registro no realizado",
                "El cliente ya existe o no pudo registrarse."
            )
            return False
        return True

    def actualizar(self, datos, fila):
        cliente = self.validar(datos)
        if cliente is None:
            return False
        if not self.servicio.actualizar_cliente(cliente):
            messagebox.showwarning(
                "Actualización no realizada",
                "No se encontró el cliente seleccionado."
            )
            return False
        return True

    def eliminar(self, fila):
        id_cliente = int(fila[0])
        try:
            if not self.servicio.eliminar_cliente(id_cliente):
                messagebox.showwarning(
                    "Eliminación no realizada",
                    "No se encontró el cliente seleccionado."
                )
                return False
            return True
        except sqlite3.IntegrityError:
            messagebox.showerror(
                "No se puede eliminar",
                "El cliente tiene vehículos registrados y no puede eliminarse."
            )
            return False

    def consultar(self, fila):
        messagebox.showinfo(
            "Detalle del cliente",
            "ID: {}\nNombre: {}\nTeléfono: {}\nCorreo: {}".format(*fila)
        )
