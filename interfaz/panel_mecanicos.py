import sqlite3
from tkinter import messagebox

from modelos.mecanico import Mecanico
from servicios.servicio_mecanicos import ServicioMecanicos

from interfaz.panel_crud import PanelCRUD


class PanelMecanicos(PanelCRUD):

    def __init__(self, parent):
        self.servicio = ServicioMecanicos()
        columnas = [
            ("ID", "id_mecanico", 80, 0),
            ("Nombre", "nombre", 220, 1),
            ("Especialidad", "especialidad", 180, 2),
            ("Teléfono", "telefono", 150, 3),
            ("Disponible", "disponible", 100, 4)
        ]
        campos = [
            {"titulo": "ID", "clave": "id_mecanico", "tipo": "numero", "opciones": None},
            {"titulo": "Nombre", "clave": "nombre", "tipo": "texto", "opciones": None},
            {"titulo": "Especialidad", "clave": "especialidad", "tipo": "texto", "opciones": None},
            {"titulo": "Teléfono", "clave": "telefono", "tipo": "texto", "opciones": None},
            {"titulo": "Disponible", "clave": "disponible", "tipo": "combo", "opciones": ["Sí", "No"]}
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
        for fila in self.servicio.listar_mecanicos():
            disponible = "Sí" if int(fila[4]) == 1 else "No"
            resultado.append((
                fila[0], fila[1], fila[2], fila[3], disponible
            ))
        return resultado

    def validar(self, datos):
        obligatorios = (
            "id_mecanico", "nombre",
            "especialidad", "telefono", "disponible"
        )
        if any(not datos.get(clave) for clave in obligatorios):
            messagebox.showwarning(
                "Campos obligatorios",
                "Complete todos los campos del formulario."
            )
            return None

        try:
            id_mecanico = int(datos["id_mecanico"])
        except ValueError:
            messagebox.showwarning(
                "Dato inválido",
                "El ID debe ser un número entero."
            )
            return None

        mecanico = Mecanico(
            id_mecanico,
            datos["nombre"].strip(),
            datos["especialidad"].strip(),
            datos["telefono"].strip()
        )
        mecanico.disponible = datos["disponible"] == "Sí"
        return mecanico

    def registrar(self, datos):
        mecanico = self.validar(datos)
        if mecanico is None:
            return False
        if not self.servicio.registrar_mecanico(mecanico):
            messagebox.showwarning(
                "Registro no realizado",
                "El mecánico ya existe o no pudo registrarse."
            )
            return False
        return True

    def actualizar(self, datos, fila):
        mecanico = self.validar(datos)
        if mecanico is None:
            return False
        if not self.servicio.actualizar_mecanico(mecanico):
            messagebox.showwarning(
                "Actualización no realizada",
                "No se encontró el mecánico seleccionado."
            )
            return False
        return True

    def eliminar(self, fila):
        try:
            if not self.servicio.eliminar_mecanico(int(fila[0])):
                messagebox.showwarning(
                    "Eliminación no realizada",
                    "No se encontró el mecánico seleccionado."
                )
                return False
            return True
        except sqlite3.IntegrityError:
            messagebox.showerror(
                "No se puede eliminar",
                "El mecánico está asignado a una o más órdenes."
            )
            return False

    def consultar(self, fila):
        messagebox.showinfo(
            "Detalle del mecánico",
            "ID: {}\nNombre: {}\nEspecialidad: {}\n"
            "Teléfono: {}\nDisponible: {}".format(*fila)
        )
