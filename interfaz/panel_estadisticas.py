import sqlite3
import tkinter as tk
from tkinter import messagebox

from datos.estadisticas import obtener_estadisticas


class PanelEstadisticas(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#F2F4F7")
        self.contenedor = tk.Frame(self, bg="#F2F4F7")
        self.contenedor.pack(fill="both", expand=True)
        self.actualizar()

    def actualizar(self):
        for widget in self.contenedor.winfo_children():
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
            ("Clientes", datos["clientes"], "#1E3A5F"),
            ("Vehículos", datos["vehiculos"], "#315780"),
            ("Mecánicos", datos["mecanicos"], "#2F6B8A"),
            ("Órdenes", datos["ordenes"], "#4C739B"),
            ("Repuestos disponibles", datos["repuestos"], "#3C8063"),
            ("Alertas", datos["alertas"], "#A66A32")
        ]

        encabezado = tk.Frame(self.contenedor, bg="#F2F4F7")
        encabezado.pack(fill="x", pady=(0, 10))

        tk.Label(
            encabezado,
            text="Resumen general de AutoCare",
            font=("Segoe UI", 14, "bold"),
            bg="#F2F4F7",
            fg="#1E3A5F"
        ).pack(side="left")

        tk.Button(
            encabezado,
            text="Actualizar",
            font=("Segoe UI", 10),
            bg="#1E3A5F",
            fg="white",
            relief="flat",
            padx=12,
            command=self.actualizar
        ).pack(side="right")

        grilla = tk.Frame(self.contenedor, bg="#F2F4F7")
        grilla.pack(fill="both", expand=True)
        grilla.grid_columnconfigure((0, 1, 2), weight=1, uniform="stats")

        for indice, (nombre, cantidad, color) in enumerate(tarjetas):
            fila = indice // 3
            columna = indice % 3
            tarjeta = tk.Frame(
                grilla,
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
            grilla.grid_rowconfigure(fila, weight=1)

            tk.Label(
                tarjeta,
                text=nombre,
                font=("Segoe UI", 11),
                bg="white",
                fg="#555555"
            ).pack(pady=(25, 5))
            tk.Label(
                tarjeta,
                text=str(cantidad),
                font=("Segoe UI", 26, "bold"),
                bg="white",
                fg=color
            ).pack()
