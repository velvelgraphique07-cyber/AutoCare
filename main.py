
from modelos.cliente import Cliente
from modelos.vehiculo import Vehiculo
from modelos.mecanico import Mecanico
from modelos.gestor_taller import GestorTaller
from modelos.orden_reparacion import OrdenReparacion
from modelos.diagnostico import Diagnostico
from modelos.mantenimiento import Mantenimiento
from modelos.detalle_reparacion import DetalleReparacion
from modelos.repuesto import Repuesto
from modelos.alerta_mantenimiento import AlertaMantenimiento
from repositories.reparaciones import RepositorioReparaciones
from repositories.diagnosticos import RepositorioDiagnosticos
from repositories.mantenimientos import RepositorioMantenimientos
from repositories.detalles_reparacion import RepositorioDetallesReparacion
from repositories.repuestos import RepositorioRepuestos
from repositories.alertas import RepositorioAlertas
from servicios.servicio_clientes import ServicioClientes
from servicios.servicio_vehiculos import ServicioVehiculos
from servicios.servicio_reparaciones import ServicioReparaciones
from servicios.servicio_inventario import ServicioInventario
from servicios.servicio_mantenimiento import ServicioMantenimiento
from datos.crear_tablas import crear_tablas

# Crear las tablas antes de utilizar los servicios
crear_tablas()

# Crear el taller
taller = GestorTaller("AutoCare")

# Crear cliente
cliente1 = Cliente(1, "Juan Pérez", "1123456789", "juan@gmail.com")

# Crear vehículo
vehiculo1 = Vehiculo(
    1, "Toyota", "Corolla", "AB123CD", 2022, cliente1
)

# Crear mecánicos
mecanico1 = Mecanico(
    1, "Carlos López", "Mecánica general", "1122233344"
)

mecanico2 = Mecanico(
    2, "Pedro Gómez", "Electricidad automotriz", "1144455566"
)

# Registrar mediante los servicios
servicio_clientes = ServicioClientes()
servicio_vehiculos = ServicioVehiculos()

servicio_clientes.registrar_cliente(cliente1)
servicio_vehiculos.registrar_vehiculo(vehiculo1)

taller.registrar_cliente(cliente1)
taller.registrar_vehiculo(vehiculo1)
taller.registrar_mecanico(mecanico1)
taller.registrar_mecanico(mecanico2)


# Crear orden de reparación
orden1 = OrdenReparacion(
    1, vehiculo1, "18/11/2026",
    "Revisión del motor y sistema eléctrico"
)

orden1.asignar_mecanico(mecanico1)
orden1.asignar_mecanico(mecanico2)

servicio_reparaciones = ServicioReparaciones()
servicio_reparaciones.registrar_orden(orden1)

taller.registrar_orden(orden1)

# Crear diagnóstico
diagnostico1 = Diagnostico(
    1,
    orden1,
    "18/11/2026",
    "Falla en el motor",
    "Se detectó ruido anormal y vibración"
)
taller.registrar_diagnostico(diagnostico1)

# Crear el servicio de mantenimiento
servicio_mantenimiento = ServicioMantenimiento()

# Crear mantenimiento preventivo
mantenimiento1 = Mantenimiento(
    1,
    vehiculo1,
    "20/11/2026",
    "Preventivo",
    "Cambio de aceite y revisión de filtros",
    45000
)

servicio_mantenimiento.registrar_mantenimiento(mantenimiento1)
taller.registrar_mantenimiento(mantenimiento1)

# Crear detalle de reparación
detalle1 = DetalleReparacion(
    1,
    orden1,
    "Reparación del motor",
    3,
    15000
)
taller.registrar_detalle(detalle1)

# Crear repuesto
repuesto1 = Repuesto(
    1,
    "Filtro de aceite",
    "Filtro para Toyota Corolla",
    12000,
    10
)

servicio_inventario = ServicioInventario()
servicio_inventario.registrar_repuesto(repuesto1)

taller.registrar_repuesto(repuesto1)

# Crear alerta de mantenimiento
alerta1 = AlertaMantenimiento(
    1,
    vehiculo1,
    "20/12/2026",
    "Recordatorio: realizar cambio de aceite",
    50000
)
servicio_mantenimiento.registrar_alerta(alerta1)

taller.registrar_alerta(alerta1)


# Mostrar información
orden1.mostrar_informacion()
diagnostico1.mostrar_informacion()
mantenimiento1.mostrar_informacion()
detalle1.mostrar_informacion()
repuesto1.mostrar_informacion()
alerta1.mostrar_informacion()

# Probar actualización del inventario
print("\n=== PRUEBA DE INVENTARIO ===")
repuesto1.actualizar_stock(-2)
servicio_inventario.actualizar_stock(
    repuesto1.id_repuesto,
    repuesto1.cantidad_stock
)
repuesto1.mostrar_informacion()

# Probar alerta
print("\n=== PRUEBA DE ALERTA ===")
alerta1.marcar_completada()
alerta1.mostrar_informacion()

print()
taller.mostrar_resumen()

from datos.conexion import conectar

# Probar conexión con SQLite
conexion = conectar()
print("\nBase de datos AutoCare conectada correctamente.")
conexion.close()



from repositories.clientes import RepositorioClientes

# Consultar clientes guardados en SQLite
print("\n=== CLIENTES GUARDADOS EN SQLITE ===")

for cliente in servicio_clientes.listar_clientes():
    print(cliente)

from repositories.vehiculos import RepositorioVehiculos

# Probar el repositorio de vehículos
# Consultar vehículos guardados en SQLite
print("\n=== VEHÍCULOS GUARDADOS EN SQLITE ===")

for vehiculo in servicio_vehiculos.listar_vehiculos():
    print(vehiculo)



from repositories.mecanicos import RepositorioMecanicos

# Probar el repositorio de mecánicos
repositorio_mecanicos = RepositorioMecanicos()

mecanicos_guardados = repositorio_mecanicos.listar()

for mecanico in [mecanico1, mecanico2]:
    if not any(fila[0] == mecanico.id_mecanico for fila in mecanicos_guardados):
        repositorio_mecanicos.registrar(mecanico)

print("\n=== MECÁNICOS GUARDADOS EN SQLITE ===")

for mecanico in repositorio_mecanicos.listar():
    print(mecanico)


# Consultar órdenes guardadas en SQLite
print("\n=== ÓRDENES GUARDADAS EN SQLITE ===")

for orden in servicio_reparaciones.listar_ordenes():
    print(orden)

repositorio_reparaciones = RepositorioReparaciones()
print("\n=== MECÁNICOS ASIGNADOS A LA ORDEN ===")

for mecanico in repositorio_reparaciones.listar_mecanicos(1):
    print(mecanico)


## Consultar diagnósticos guardados en SQLite

repositorio_diagnosticos = RepositorioDiagnosticos()
print("\n=== DIAGNÓSTICOS GUARDADOS EN SQLITE ===")

for diagnostico in repositorio_diagnosticos.listar():
    print(diagnostico)

# Consultar mantenimientos guardados en SQLite
print("\n=== MANTENIMIENTOS GUARDADOS EN SQLITE ===")

for mantenimiento in servicio_mantenimiento.listar_mantenimientos():
    print(mantenimiento)


# Probar repositorio de detalles de reparación
repositorio_detalles = RepositorioDetallesReparacion()

detalles_guardados = repositorio_detalles.listar()

if not any(fila[0] == detalle1.id_detalle for fila in detalles_guardados):
    repositorio_detalles.registrar(detalle1)

print("\n=== DETALLES DE REPARACIÓN GUARDADOS EN SQLITE ===")

for detalle in repositorio_detalles.listar():
    print(detalle)


# Consultar repuestos guardados en SQLite
print("\n=== REPUESTOS GUARDADOS EN SQLITE ===")

for repuesto in servicio_inventario.listar_repuestos():
    print(repuesto)


# Consultar alertas guardadas en SQLite
print("\n=== ALERTAS DE MANTENIMIENTO GUARDADAS EN SQLITE ===")

for alerta in servicio_mantenimiento.listar_alertas():
    print(alerta)