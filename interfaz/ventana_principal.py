
import tkinter as tk
from datos.estadisticas import obtener_estadisticas


class VentanaPrincipal:

    def __init__(self, root):
        self.root = root

        self.root.title("AutoCare - Sistema de Gestión")
        self.root.geometry("1100x700")
        self.root.configure(bg="#F2F4F7")

        # ENCABEZADO
        encabezado = tk.Frame(
            self.root,
            bg="#1E3A5F",
            height=110
        )
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        titulo = tk.Label(
            encabezado,
            text="AUTOCARE",
            font=("Arial", 26, "bold"),
            bg="#1E3A5F",
            fg="white"
        )
        titulo.pack(pady=(20, 5))

        subtitulo = tk.Label(
            encabezado,
            text="Sistema de Diagnóstico y Mantenimiento Vehicular",
            font=("Arial", 11),
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
            "Repuestos",
            "Alertas"
        ]

        for opcion in opciones:
            boton = tk.Button(
                menu,
                text=opcion,
                font=("Arial", 11),
                bg="#172B46",
                fg="white",
                activebackground="#315780",
                activeforeground="white",
                relief="flat",
                anchor="w",
                padx=20,
                pady=12,
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
            font=("Arial", 22, "bold"),
            bg="#F2F4F7",
            fg="#1E3A5F"
        )
        self.titulo_seccion.pack(anchor="w")

        self.mensaje = tk.Label(
            self.contenido,
            text="Bienvenido al sistema AutoCare.",
            font=("Arial", 12),
            bg="#F2F4F7",
            fg="#555555"
        )
        self.mensaje.pack(anchor="w", pady=15)

        # TARJETAS DE ESTADÍSTICAS
        tarjetas = tk.Frame(
            self.contenido,
            bg="#F2F4F7"
        )
        tarjetas.pack(fill="x", pady=30)


        datos = obtener_estadisticas()

        estadisticas = [
            ("Clientes registrados", str(datos["clientes"])),
            ("Vehículos registrados", str(datos["vehiculos"])),
            ("Mecánicos registrados", str(datos["mecanicos"]))
        ]


        for nombre, cantidad in estadisticas:
            tarjeta = tk.Frame(
                tarjetas,
                bg="white",
                width=200,
                height=120,
                highlightbackground="#DCE3EA",
                highlightthickness=1
            )
            tarjeta.pack(side="left", padx=10)
            tarjeta.pack_propagate(False)

            tk.Label(
                tarjeta,
                text=nombre,
                font=("Arial", 11),
                bg="white",
                fg="#555555"
            ).pack(pady=(20, 5))

            tk.Label(
                tarjeta,
                text=cantidad,
                font=("Arial", 24, "bold"),
                bg="white",
                fg="#1E3A5F"
            ).pack()


    def mostrar_seccion(self, nombre):
        self.titulo_seccion.config(text=nombre)
        self.mensaje.config(
            text="Sección seleccionada: " + nombre
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
