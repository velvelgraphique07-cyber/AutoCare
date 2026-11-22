import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


class DialogoFormulario(tk.Toplevel):

    def __init__(self, parent, titulo, campos, valores=None, al_guardar=None):
        super().__init__(parent)
        self.title(titulo)
        self.geometry("520x460")
        self.resizable(False, False)
        self.configure(bg="#F2F4F7")
        self.transient(parent)
        self.grab_set()
        self.al_guardar = al_guardar
        self.campos = campos
        self.controles = {}

        contenedor = tk.Frame(self, bg="#F2F4F7", padx=25, pady=20)
        contenedor.pack(fill="both", expand=True)

        tk.Label(
            contenedor,
            text=titulo,
            font=("Segoe UI", 16, "bold"),
            bg="#F2F4F7",
            fg="#1E3A5F"
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 18))

        valores = valores or {}
        for indice, campo in enumerate(campos, start=1):
            etiqueta = campo["titulo"]
            clave = campo["clave"]

            tk.Label(
                contenedor,
                text=etiqueta,
                font=("Segoe UI", 10),
                bg="#F2F4F7",
                fg="#555555"
            ).grid(row=indice, column=0, sticky="w", pady=6)

            if campo["tipo"] == "combo":
                control = ttk.Combobox(
                    contenedor,
                    values=campo["opciones"],
                    state="readonly",
                    width=34
                )
                if clave in valores:
                    control.set(str(valores[clave]))
                elif campo["opciones"]:
                    control.current(0)
            elif campo["tipo"] == "texto_largo":
                control = tk.Text(contenedor, width=36, height=4)
                if clave in valores:
                    control.insert("1.0", str(valores[clave]))
            else:
                control = tk.Entry(contenedor, width=37)
                if clave in valores:
                    control.insert(0, str(valores[clave]))

            control.grid(row=indice, column=1, pady=6, padx=(12, 0))
            self.controles[clave] = control

        acciones = tk.Frame(contenedor, bg="#F2F4F7")
        acciones.grid(row=len(campos) + 1, column=0, columnspan=2, pady=(18, 0))

        tk.Button(
            acciones,
            text="Cancelar",
            font=("Segoe UI", 10),
            bg="#FFFFFF",
            fg="#555555",
            relief="solid",
            bd=1,
            width=12,
            command=self.destroy
        ).pack(side="left", padx=6)

        tk.Button(
            acciones,
            text="Guardar",
            font=("Segoe UI", 10, "bold"),
            bg="#3C8063",
            fg="white",
            relief="flat",
            width=12,
            command=self.guardar
        ).pack(side="left", padx=6)

    def guardar(self):
        datos = {}
        for clave, control in self.controles.items():
            if isinstance(control, tk.Text):
                datos[clave] = control.get("1.0", "end").strip()
            else:
                datos[clave] = control.get().strip()

        if self.al_guardar is not None:
            if self.al_guardar(datos):
                self.destroy()


class PanelCRUD(tk.Frame):

    def __init__(
        self,
        parent,
        columnas,
        cargador,
        campos,
        registrar,
        actualizar,
        eliminar,
        consultar=None
    ):
        super().__init__(parent, bg="#F2F4F7")
        self.columnas = columnas
        self.cargador = cargador
        self.campos = campos
        self.registrar = registrar
        self.actualizar = actualizar
        self.eliminar = eliminar
        self.consultar = consultar
        self.filas_actuales = []

        barra = tk.Frame(self, bg="#F2F4F7")
        barra.pack(fill="x", pady=(0, 12))

        tk.Label(
            barra,
            text="Buscar:",
            font=("Segoe UI", 10),
            bg="#F2F4F7",
            fg="#555555"
        ).pack(side="left")

        self.buscar_texto = tk.Entry(barra, width=32)
        self.buscar_texto.pack(side="left", padx=(8, 6))
        self.buscar_texto.bind("<KeyRelease>", lambda event: self.filtrar())

        tk.Button(
            barra,
            text="Limpiar",
            font=("Segoe UI", 9),
            bg="#FFFFFF",
            fg="#555555",
            relief="solid",
            bd=1,
            command=self.limpiar_busqueda
        ).pack(side="left")

        tk.Button(
            barra,
            text="+ Registrar",
            font=("Segoe UI", 10, "bold"),
            bg="#1E3A5F",
            fg="white",
            relief="flat",
            padx=12,
            command=self.abrir_registro
        ).pack(side="right", padx=(6, 0))

        tk.Button(
            barra,
            text="Modificar",
            font=("Segoe UI", 10),
            bg="#315780",
            fg="white",
            relief="flat",
            padx=12,
            command=self.abrir_modificacion
        ).pack(side="right", padx=(6, 0))

        tk.Button(
            barra,
            text="Consultar",
            font=("Segoe UI", 10),
            bg="#4C739B",
            fg="white",
            relief="flat",
            padx=12,
            command=self.consultar_seleccion
        ).pack(side="right", padx=(6, 0))

        tk.Button(
            barra,
            text="Eliminar",
            font=("Segoe UI", 10),
            bg="#A64B4B",
            fg="white",
            relief="flat",
            padx=12,
            command=self.eliminar_seleccion
        ).pack(side="right", padx=(6, 0))

        marco_tabla = tk.Frame(
            self,
            bg="white",
            highlightbackground="#DCE3EA",
            highlightthickness=1
        )
        marco_tabla.pack(fill="both", expand=True)

        encabezados = [columna[0] for columna in columnas]
        self.tabla = ttk.Treeview(
            marco_tabla,
            columns=encabezados,
            show="headings"
        )

        for encabezado, ancho in ((c[0], c[2]) for c in columnas):
            self.tabla.heading(encabezado, text=encabezado)
            self.tabla.column(encabezado, width=ancho, anchor="w")

        scroll_y = ttk.Scrollbar(
            marco_tabla,
            orient="vertical",
            command=self.tabla.yview
        )
        scroll_x = ttk.Scrollbar(
            marco_tabla,
            orient="horizontal",
            command=self.tabla.xview
        )
        self.tabla.configure(
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        self.tabla.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")
        marco_tabla.grid_rowconfigure(0, weight=1)
        marco_tabla.grid_columnconfigure(0, weight=1)

        self.refrescar()

    def refrescar(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        try:
            self.filas_actuales = list(self.cargador())
            for fila in self.filas_actuales:
                self.tabla.insert("", "end", values=fila)
        except sqlite3.Error as error:
            messagebox.showerror(
                "Error al cargar datos",
                "No se pudieron listar los registros:\n{}".format(error)
            )

    def filtrar(self):
        texto = self.buscar_texto.get().strip().lower()
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for fila in self.filas_actuales:
            if not texto or texto in " ".join(str(valor) for valor in fila).lower():
                self.tabla.insert("", "end", values=fila)

    def limpiar_busqueda(self):
        self.buscar_texto.delete(0, "end")
        self.filtrar()

    def seleccion(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning(
                "Selección requerida",
                "Seleccione un registro en la tabla."
            )
            return None
        return self.tabla.item(seleccion[0], "values")

    def abrir_registro(self):
        DialogoFormulario(
            self,
            "Registrar",
            self.campos,
            al_guardar=self.guardar_registro
        )

    def abrir_modificacion(self):
        fila = self.seleccion()
        if fila is None:
            return

        valores = {}
        for columna in self.columnas:
            valores[columna[1]] = fila[columna[3]]

        for campo in self.campos:
            clave = campo["clave"]
            if campo["tipo"] == "combo" and clave in valores:
                for opcion in campo["opciones"]:
                    if str(opcion).startswith(str(valores[clave]) + " -"):
                        valores[clave] = opcion
                        break

        DialogoFormulario(
            self,
            "Modificar registro",
            self.campos,
            valores,
            al_guardar=lambda datos: self.guardar_actualizacion(
                datos,
                fila
            )
        )

    def guardar_registro(self, datos):
        try:
            resultado = self.registrar(datos)
            if resultado:
                messagebox.showinfo("Operación exitosa", "Registro guardado.")
                self.refrescar()
                return True
            return False
        except (sqlite3.Error, ValueError, TypeError) as error:
            messagebox.showerror("Error", str(error))
            return False

    def guardar_actualizacion(self, datos, fila):
        try:
            resultado = self.actualizar(datos, fila)
            if resultado:
                messagebox.showinfo("Operación exitosa", "Registro actualizado.")
                self.refrescar()
                return True
            return False
        except (sqlite3.Error, ValueError, TypeError) as error:
            messagebox.showerror("Error", str(error))
            return False

    def consultar_seleccion(self):
        fila = self.seleccion()
        if fila is None:
            return
        if self.consultar:
            self.consultar(fila)

    def eliminar_seleccion(self):
        fila = self.seleccion()
        if fila is None:
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Desea eliminar el registro seleccionado?"
        )
        if not confirmar:
            return

        try:
            if self.eliminar(fila):
                messagebox.showinfo("Operación exitosa", "Registro eliminado.")
                self.refrescar()
        except (sqlite3.Error, ValueError, TypeError) as error:
            messagebox.showerror("Error al eliminar", str(error))
