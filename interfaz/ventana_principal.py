
import os
import sqlite3
import sys
import tkinter as tk
from tkinter import messagebox

if __package__ in (None, ""):
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datos.estadisticas import obtener_estadisticas
from interfaz.panel_clientes import PanelClientes
from interfaz.panel_diagnosticos import PanelDiagnosticos
from interfaz.panel_detalles_reparacion import PanelDetallesReparacion
from interfaz.panel_alertas import PanelAlertas
from interfaz.panel_estadisticas import PanelEstadisticas
from interfaz.panel_mantenimientos import PanelMantenimientos
from interfaz.panel_mecanicos import PanelMecanicos
from interfaz.panel_ordenes import PanelOrdenes
from interfaz.panel_repuestos import PanelRepuestos
from interfaz.panel_vehiculos import PanelVehiculos


class VentanaPrincipal:

    def __init__(self, root):
        self.root = root

        self.root.title("AutoCare - Sistema de Gestión")
        self.root.geometry("1200x750")
        self.root.minsize(1100, 700)
        self.root.configure(bg="#F2F4F7")

        # ENCABEZADO
        encabezado = tk.Frame(
            self.root,
            bg="#1E3A5F",
            height=95
        )
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        titulo = tk.Label(
            encabezado,
            text="AUTOCARE",
            font=("Segoe UI", 24, "bold"),
            bg="#1E3A5F",
            fg="white"
        )
        titulo.pack(pady=(14, 2))

        subtitulo = tk.Label(
            encabezado,
            text="Sistema de Diagnóstico y Mantenimiento Vehicular",
            font=("Segoe UI", 10),
            bg="#1E3A5F",
            fg="#DCE6F1"
        )
        subtitulo.pack()

        # ESTRUCTURA PRINCIPAL
        cuerpo = tk.Frame(self.root, bg="#F2F4F7")
        cuerpo.pack(fill="both", expand=True)

        # MENÚ LATERAL
        menu = tk.Frame(cuerpo, bg="#172B46", width=230)
        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)

        opciones = [
            "Inicio",
            "Clientes",
            "Vehículos",
            "Mecánicos",
            "Órdenes de reparación",
            "Diagnósticos",
            "Mantenimientos",
            "Detalles de reparación",
            "Repuestos e inventario",
            "Alertas de mantenimiento",
            "Estadísticas"
        ]

        for opcion in opciones:
            boton = tk.Button(
                menu,
                text=opcion,
                font=("Segoe UI", 10),
                bg="#172B46",
                fg="white",
                activebackground="#315780",
                activeforeground="white",
                relief="flat",
                anchor="w",
                padx=20,
                pady=10,
                command=lambda nombre=opcion: self.mostrar_seccion(nombre)
            )
            boton.pack(fill="x")

        # ÁREA DE CONTENIDO
        self.contenido = tk.Frame(
            cuerpo,
            bg="#F2F4F7"
        )
        self.contenido.pack(
            side="right",
            fill="both",
            expand=True,
            padx=30,
            pady=30
        )

        self.titulo_seccion = tk.Label(
            self.contenido,
            text="Panel principal",
            font=("Segoe UI", 21, "bold"),
            bg="#F2F4F7",
            fg="#1E3A5F"
        )
        self.titulo_seccion.pack(anchor="w")

        self.mensaje = tk.Label(
            self.contenido,
            text="Bienvenido al sistema AutoCare.",
            font=("Segoe UI", 11),
            bg="#F2F4F7",
            fg="#555555"
        )
        self.mensaje.pack(anchor="w", pady=15)

        self.area_seccion = tk.Frame(
            self.contenido,
            bg="#F2F4F7"
        )
        self.area_seccion.pack(fill="both", expand=True, pady=(10, 0))
        self.mostrar_inicio()

    def mostrar_seccion(self, nombre):
        self.titulo_seccion.config(text=nombre)
        if nombre == "Inicio":
            self.mostrar_inicio()
            return

        for widget in self.area_seccion.winfo_children():
            widget.destroy()

        if nombre == "Clientes":
            self.mensaje.config(text="Gestión de clientes registrados.")
            PanelClientes(self.area_seccion).pack(fill="both", expand=True)
            return
        if nombre == "Vehículos":
            self.mensaje.config(text="Gestión de vehículos y propietarios.")
            PanelVehiculos(self.area_seccion).pack(fill="both", expand=True)
            return
        if nombre == "Mecánicos":
            self.mensaje.config(text="Gestión de mecánicos y disponibilidad.")
            PanelMecanicos(self.area_seccion).pack(fill="both", expand=True)
            return
        if nombre == "Órdenes de reparación":
            self.mensaje.config(text="Gestión de órdenes y mecánicos asignados.")
            PanelOrdenes(self.area_seccion).pack(fill="both", expand=True)
            return
        if nombre == "Diagnósticos":
            self.mensaje.config(text="Gestión de diagnósticos técnicos.")
            PanelDiagnosticos(self.area_seccion).pack(fill="both", expand=True)
            return
        if nombre == "Mantenimientos":
            self.mensaje.config(text="Gestión de mantenimientos programados y completados.")
            PanelMantenimientos(self.area_seccion).pack(fill="both", expand=True)
            return
        if nombre == "Detalles de reparación":
            self.mensaje.config(text="Gestión de trabajos y costos de mano de obra.")
            PanelDetallesReparacion(self.area_seccion).pack(fill="both", expand=True)
            return
        if nombre == "Repuestos e inventario":
            self.mensaje.config(text="Gestión de repuestos e inventario.")
            PanelRepuestos(self.area_seccion).pack(fill="both", expand=True)
            return
        if nombre == "Alertas de mantenimiento":
            self.mensaje.config(text="Gestión de alertas de mantenimiento.")
            PanelAlertas(self.area_seccion).pack(fill="both", expand=True)
            return
        if nombre == "Estadísticas":
            self.mensaje.config(text="Resumen actualizado de la base de datos.")
            PanelEstadisticas(self.area_seccion).pack(fill="both", expand=True)
            return

        self.mensaje.config(text="Módulo disponible para la siguiente etapa.")
        panel = tk.Frame(
            self.area_seccion,
            bg="white",
            highlightbackground="#DCE3EA",
            highlightthickness=1
        )
        panel.pack(fill="both", expand=True)

        tk.Label(
            panel,
            text=nombre,
            font=("Segoe UI", 16, "bold"),
            bg="white",
            fg="#1E3A5F"
        ).pack(pady=(35, 8))

        tk.Label(
            panel,
            text="Este panel se conectará al backend en la etapa correspondiente.",
            font=("Segoe UI", 11),
            bg="white",
            fg="#777777"
        ).pack()

    def mostrar_inicio(self):
        self.titulo_seccion.config(text="Panel principal")
        self.mensaje.config(text="Bienvenido al sistema AutoCare.")

        for widget in self.area_seccion.winfo_children():
            widget.destroy()

        try:
            datos = obtener_estadisticas()
        except sqlite3.Error as error:
            messagebox.showerror(
                "Error al cargar estadísticas",
                "No se pudieron consultar los datos de SQLite:\n{}".format(error)
            )
            datos = {
                "clientes": 0,
                "vehiculos": 0,
                "mecanicos": 0,
                "ordenes": 0,
                "repuestos": 0,
                "alertas": 0
            }

        tarjetas = [
            ("Clientes registrados", datos["clientes"], "#1E3A5F"),
            ("Vehículos registrados", datos["vehiculos"], "#315780"),
            ("Mecánicos registrados", datos["mecanicos"], "#2F6B8A"),
            ("Órdenes de reparación", datos["ordenes"], "#4C739B"),
            ("Repuestos disponibles", datos["repuestos"], "#3C8063"),
            ("Alertas de mantenimiento", datos["alertas"], "#A66A32")
        ]

        contenedor = tk.Frame(self.area_seccion, bg="#F2F4F7")
        contenedor.pack(fill="both", expand=True)
        contenedor.grid_columnconfigure((0, 1, 2), weight=1, uniform="cards")

        for indice, (nombre, cantidad, color) in enumerate(tarjetas):
            fila = indice // 3
            columna = indice % 3

            tarjeta = tk.Frame(
                contenedor,
                bg="white",
                highlightbackground="#DCE3EA",
                highlightthickness=1
            )
            tarjeta.grid(
                row=fila,
                column=columna,
                sticky="nsew",
                padx=10,
                pady=10
            )
            contenedor.grid_rowconfigure(fila, weight=1)

            franja = tk.Frame(tarjeta, bg=color, height=7)
            franja.pack(fill="x")

            tk.Label(
                tarjeta,
                text=nombre,
                font=("Segoe UI", 11),
                bg="white",
                fg="#555555"
            ).pack(pady=(24, 5))

            tk.Label(
                tarjeta,
                text=str(cantidad),
                font=("Segoe UI", 26, "bold"),
                bg="white",
                fg=color
            ).pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
