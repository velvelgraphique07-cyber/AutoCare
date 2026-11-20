
class GestorTaller:
    """
    Administra las operaciones principales del taller AutoCare.
    """

    def __init__(self, nombre):
        self.nombre = nombre

        # Listas de elementos del taller
        self.clientes = []
        self.vehiculos = []
        self.mecanicos = []
        self.ordenes = []
        self.diagnosticos = []
        self.mantenimientos = []
        self.detalles_reparacion = []
        self.repuestos = []
        self.alertas = []

    # GESTIÓN DE CLIENTES

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print("Cliente registrado correctamente.")

    # GESTIÓN DE VEHÍCULOS

    def registrar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print("Vehículo registrado correctamente.")

    # GESTIÓN DE MECÁNICOS

    def registrar_mecanico(self, mecanico):
        self.mecanicos.append(mecanico)
        print("Mecánico registrado correctamente.")

    # GESTIÓN DE ÓRDENES

    def registrar_orden(self, orden):
        self.ordenes.append(orden)
        print("Orden registrada correctamente.")

    # GESTIÓN DE DIAGNÓSTICOS

    def registrar_diagnostico(self, diagnostico):
        self.diagnosticos.append(diagnostico)
        print("Diagnóstico registrado correctamente.")

    # GESTIÓN DE MANTENIMIENTOS

    def registrar_mantenimiento(self, mantenimiento):
        self.mantenimientos.append(mantenimiento)
        print("Mantenimiento registrado correctamente.")

    # GESTIÓN DE DETALLES DE REPARACIÓN

    def registrar_detalle(self, detalle):
        self.detalles_reparacion.append(detalle)
        print("Detalle de reparación registrado correctamente.")

    # GESTIÓN DE REPUESTOS

    def registrar_repuesto(self, repuesto):
        self.repuestos.append(repuesto)
        print("Repuesto registrado correctamente.")

    # GESTIÓN DE ALERTAS

    def registrar_alerta(self, alerta):
        self.alertas.append(alerta)
        print("Alerta registrada correctamente.")

    # RESUMEN GENERAL

    def mostrar_resumen(self):
        print("\n=== RESUMEN DEL TALLER ===")
        print("Taller:", self.nombre)
        print("Clientes:", len(self.clientes))
        print("Vehículos:", len(self.vehiculos))
        print("Mecánicos:", len(self.mecanicos))
        print("Órdenes:", len(self.ordenes))
        print("Diagnósticos:", len(self.diagnosticos))
        print("Mantenimientos:", len(self.mantenimientos))
        print("Detalles de reparación:", len(self.detalles_reparacion))
        print("Repuestos:", len(self.repuestos))
        print("Alertas:", len(self.alertas))
