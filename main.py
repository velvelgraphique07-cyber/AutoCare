from datos.crear_tablas import crear_tablas
from modelos.cliente import Cliente
from servicios.servicio_clientes import ServicioClientes
from modelos.vehiculo import Vehiculo
from servicios.servicio_vehiculos import ServicioVehiculos
from modelos.mecanico import Mecanico
from servicios.servicio_mecanicos import ServicioMecanicos
from modelos.orden_reparacion import OrdenReparacion
from servicios.servicio_reparaciones import ServicioReparaciones
from modelos.diagnostico import Diagnostico
from servicios.servicio_diagnosticos import ServicioDiagnosticos
from modelos.mantenimiento import Mantenimiento
from servicios.servicio_mantenimiento import ServicioMantenimiento
from modelos.detalle_reparacion import DetalleReparacion
from servicios.servicio_detalles_reparacion import ServicioDetallesReparacion
from modelos.repuesto import Repuesto
from servicios.servicio_inventario import ServicioInventario
from modelos.alerta_mantenimiento import AlertaMantenimiento
from datos.estadisticas import obtener_estadisticas


def crear_vehiculo_desde_id(id_vehiculo):
    """Construye un Vehiculo usando los datos guardados en SQLite."""
    fila = ServicioVehiculos().buscar_vehiculo(id_vehiculo)
    if not fila:
        return None

    cliente = Cliente(fila[5], "", "", "")
    return Vehiculo(
        fila[0], fila[1], fila[2], fila[3], fila[4], cliente
    )


def crear_orden_desde_id(id_orden):
    """Construye una OrdenReparacion con su vehículo asociado."""
    fila = ServicioReparaciones().buscar_orden(id_orden)
    if not fila:
        return None

    vehiculo = crear_vehiculo_desde_id(fila[1])
    if not vehiculo:
        return None

    orden = OrdenReparacion(fila[0], vehiculo, fila[2], fila[3])
    orden.estado = fila[4]
    return orden


def menu_clientes():
    servicio = ServicioClientes()

    while True:
        print("\n========== GESTIÓN DE CLIENTES ==========")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Actualizar cliente")
        print("5. Eliminar cliente")
        print("0. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            break
        elif opcion == "1":
            print("\nREGISTRAR CLIENTE")
            cliente = Cliente(
                int(input("ID del cliente: ")),
                input("Nombre: "),
                input("Teléfono: "),
                input("Correo: ")
            )
            servicio.registrar_cliente(cliente)
        elif opcion == "2":
            print("\nLISTA DE CLIENTES")
            for cliente in servicio.listar_clientes():
                print(cliente)
        elif opcion == "3":
            id_cliente = int(input("ID del cliente que buscas: "))
            cliente = servicio.buscar_cliente(id_cliente)
            print(cliente if cliente else "Cliente no encontrado.")
        elif opcion == "4":
            cliente = Cliente(
                int(input("ID del cliente: ")),
                input("Nuevo nombre: "),
                input("Nuevo teléfono: "),
                input("Nuevo correo: ")
            )
            servicio.actualizar_cliente(cliente)
        elif opcion == "5":
            servicio.eliminar_cliente(
                int(input("ID del cliente que deseas eliminar: "))
            )
        else:
            print("Opción no válida.")


def menu_vehiculos():
    servicio = ServicioVehiculos()

    while True:
        print("\n========== GESTIÓN DE VEHÍCULOS ==========")
        print("1. Registrar vehículo")
        print("2. Listar vehículos")
        print("3. Buscar vehículo")
        print("4. Actualizar vehículo")
        print("5. Eliminar vehículo")
        print("0. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            break
        elif opcion in ("1", "4"):
            id_vehiculo = int(input("ID del vehículo: "))
            marca = input("Marca: " if opcion == "1" else "Nueva marca: ")
            modelo = input("Modelo: " if opcion == "1" else "Nuevo modelo: ")
            patente = input("Patente: " if opcion == "1" else "Nueva patente: ")
            anio = int(input("Año: " if opcion == "1" else "Nuevo año: "))
            id_cliente = int(input("ID del propietario: "))
            cliente = Cliente(id_cliente, "", "", "")
            vehiculo = Vehiculo(
                id_vehiculo, marca, modelo, patente, anio, cliente
            )
            if opcion == "1":
                servicio.registrar_vehiculo(vehiculo)
            else:
                servicio.actualizar_vehiculo(vehiculo)
        elif opcion == "2":
            print("\nLISTA DE VEHÍCULOS")
            for vehiculo in servicio.listar_vehiculos():
                print(vehiculo)
        elif opcion == "3":
            vehiculo = servicio.buscar_vehiculo(
                int(input("ID del vehículo: "))
            )
            print(vehiculo if vehiculo else "Vehículo no encontrado.")
        elif opcion == "5":
            servicio.eliminar_vehiculo(
                int(input("ID del vehículo que deseas eliminar: "))
            )
        else:
            print("Opción no válida.")


def menu_mecanicos():
    servicio = ServicioMecanicos()

    while True:
        print("\n========== GESTIÓN DE MECÁNICOS ==========")
        print("1. Registrar mecánico")
        print("2. Listar mecánicos")
        print("3. Buscar mecánico")
        print("4. Actualizar mecánico")
        print("5. Eliminar mecánico")
        print("0. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            break
        elif opcion in ("1", "4"):
            mecanico = Mecanico(
                int(input("ID del mecánico: ")),
                input("Nombre: " if opcion == "1" else "Nuevo nombre: "),
                input("Especialidad: " if opcion == "1" else "Nueva especialidad: "),
                input("Teléfono: " if opcion == "1" else "Nuevo teléfono: ")
            )
            if opcion == "1":
                servicio.registrar_mecanico(mecanico)
            else:
                servicio.actualizar_mecanico(mecanico)
        elif opcion == "2":
            print("\nLISTA DE MECÁNICOS")
            for mecanico in servicio.listar_mecanicos():
                print(mecanico)
        elif opcion == "3":
            mecanico = servicio.buscar_mecanico(
                int(input("ID del mecánico: "))
            )
            print(mecanico if mecanico else "Mecánico no encontrado.")
        elif opcion == "5":
            servicio.eliminar_mecanico(
                int(input("ID del mecánico que deseas eliminar: "))
            )
        else:
            print("Opción no válida.")


def menu_ordenes():
    servicio = ServicioReparaciones()
    servicio_vehiculos = ServicioVehiculos()
    servicio_mecanicos = ServicioMecanicos()

    while True:
        print("\n========== GESTIÓN DE ÓRDENES ==========")
        print("1. Registrar orden")
        print("2. Listar órdenes")
        print("3. Buscar orden")
        print("4. Actualizar orden")
        print("5. Eliminar orden")
        print("0. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            break
        elif opcion == "1":
            id_orden = int(input("ID de la orden: "))
            id_vehiculo = int(input("ID del vehículo: "))
            vehiculo = crear_vehiculo_desde_id(id_vehiculo)
            if not vehiculo:
                print("El vehículo no existe.")
                continue
            fecha = input("Fecha (DD/MM/AAAA): ")
            descripcion = input("Descripción de la reparación: ")
            id_mecanico = int(input("ID del mecánico asignado: "))
            mecanico_fila = servicio_mecanicos.buscar_mecanico(id_mecanico)
            if not mecanico_fila:
                print("El mecánico no existe.")
                continue
            orden = OrdenReparacion(id_orden, vehiculo, fecha, descripcion)
            mecanico = Mecanico(
                mecanico_fila[0], mecanico_fila[1],
                mecanico_fila[2], mecanico_fila[3]
            )
            orden.asignar_mecanico(mecanico)
            servicio.registrar_orden(orden)
        elif opcion == "2":
            print("\nLISTA DE ÓRDENES")
            for orden in servicio.listar_ordenes():
                print(orden)
        elif opcion == "3":
            id_orden = int(input("ID de la orden: "))
            orden = servicio.buscar_orden(id_orden)
            if orden:
                print(orden)
                print("Mecánicos asignados:")
                for mecanico in servicio.listar_mecanicos_asignados(id_orden):
                    print(mecanico)
            else:
                print("Orden no encontrada.")
        elif opcion == "4":
            id_orden = int(input("ID de la orden: "))
            id_vehiculo = int(input("ID del vehículo: "))
            vehiculo = crear_vehiculo_desde_id(id_vehiculo)
            if not vehiculo:
                print("El vehículo no existe.")
                continue
            fecha = input("Nueva fecha (DD/MM/AAAA): ")
            descripcion = input("Nueva descripción: ")
            estado = input("Nuevo estado: ")
            orden = OrdenReparacion(id_orden, vehiculo, fecha, descripcion)
            orden.cambiar_estado(estado)
            servicio.actualizar_orden(orden)
        elif opcion == "5":
            servicio.eliminar_orden(
                int(input("ID de la orden que deseas eliminar: "))
            )
        else:
            print("Opción no válida.")


def menu_diagnosticos():
    servicio = ServicioDiagnosticos()
    servicio_ordenes = ServicioReparaciones()

    while True:
        print("\n========== GESTIÓN DE DIAGNÓSTICOS ==========")
        print("1. Registrar diagnóstico")
        print("2. Listar diagnósticos")
        print("3. Buscar diagnóstico")
        print("4. Actualizar diagnóstico")
        print("5. Eliminar diagnóstico")
        print("0. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            break
        elif opcion in ("1", "4"):
            id_diagnostico = int(input("ID del diagnóstico: "))
            if opcion == "4" and not servicio.buscar_diagnostico(id_diagnostico):
                print("Diagnóstico no encontrado.")
                continue
            id_orden = int(input("ID de la orden de reparación: "))
            orden_objeto = crear_orden_desde_id(id_orden)
            if not orden_objeto:
                print("La orden de reparación no existe o no tiene vehículo válido.")
                continue
            fecha = input("Fecha (DD/MM/AAAA): ")
            descripcion = input("Problema detectado: ")
            observaciones = input("Observaciones: ")
            diagnostico = Diagnostico(
                id_diagnostico, orden_objeto, fecha, descripcion, observaciones
            )
            if opcion == "1":
                servicio.registrar_diagnostico(diagnostico)
            else:
                servicio.actualizar_diagnostico(diagnostico)
        elif opcion == "2":
            print("\nLISTA DE DIAGNÓSTICOS")
            for diagnostico in servicio.listar_diagnosticos():
                print(diagnostico)
        elif opcion == "3":
            diagnostico = servicio.buscar_diagnostico(
                int(input("ID del diagnóstico: "))
            )
            print(diagnostico if diagnostico else "Diagnóstico no encontrado.")
        elif opcion == "5":
            servicio.eliminar_diagnostico(
                int(input("ID del diagnóstico que deseas eliminar: "))
            )
        else:
            print("Opción no válida.")


def menu_mantenimientos():
    servicio = ServicioMantenimiento()

    while True:
        print("\n========== GESTIÓN DE MANTENIMIENTOS ==========")
        print("1. Registrar mantenimiento")
        print("2. Listar mantenimientos")
        print("3. Buscar mantenimiento")
        print("4. Actualizar mantenimiento")
        print("5. Eliminar mantenimiento")
        print("0. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            break
        elif opcion in ("1", "4"):
            id_mantenimiento = int(input("ID del mantenimiento: "))
            if opcion == "4" and not servicio.buscar_mantenimiento(id_mantenimiento):
                print("Mantenimiento no encontrado.")
                continue
            id_vehiculo = int(input("ID del vehículo: "))
            vehiculo = crear_vehiculo_desde_id(id_vehiculo)
            if not vehiculo:
                print("El vehículo no existe.")
                continue
            fecha = input("Fecha (DD/MM/AAAA): ")
            tipo = input("Tipo de mantenimiento: ")
            descripcion = input("Descripción: ")
            kilometraje = int(input("Kilometraje: "))
            mantenimiento = Mantenimiento(
                id_mantenimiento, vehiculo, fecha, tipo, descripcion, kilometraje
            )
            if opcion == "1":
                servicio.registrar_mantenimiento(mantenimiento)
            else:
                mantenimiento.estado = input("Estado (Programado/Completado): ")
                servicio.actualizar_mantenimiento(mantenimiento)
        elif opcion == "2":
            print("\nLISTA DE MANTENIMIENTOS")
            for fila in servicio.listar_mantenimientos():
                print(fila)
        elif opcion == "3":
            fila = servicio.buscar_mantenimiento(
                int(input("ID del mantenimiento: "))
            )
            print(fila if fila else "Mantenimiento no encontrado.")
        elif opcion == "5":
            servicio.eliminar_mantenimiento(
                int(input("ID del mantenimiento que deseas eliminar: "))
            )
        else:
            print("Opción no válida.")


def menu_detalles_reparacion():
    servicio = ServicioDetallesReparacion()

    while True:
        print("\n========== GESTIÓN DE DETALLES DE REPARACIÓN ==========")
        print("1. Registrar detalle")
        print("2. Listar detalles")
        print("3. Buscar detalle")
        print("4. Actualizar detalle")
        print("5. Eliminar detalle")
        print("0. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            break
        elif opcion in ("1", "4"):
            id_detalle = int(input("ID del detalle: "))
            if opcion == "4" and not servicio.buscar_detalle(id_detalle):
                print("Detalle no encontrado.")
                continue
            id_orden = int(input("ID de la orden de reparación: "))
            orden = crear_orden_desde_id(id_orden)
            if not orden:
                print("La orden de reparación no existe.")
                continue
            descripcion = input("Descripción del trabajo: ")
            horas = float(input("Cantidad de horas: "))
            costo_hora = float(input("Costo de mano de obra por hora: "))
            detalle = DetalleReparacion(
                id_detalle, orden, descripcion, horas, costo_hora
            )
            if opcion == "1":
                servicio.registrar_detalle(detalle)
            else:
                servicio.actualizar_detalle(detalle)
        elif opcion == "2":
            print("\nLISTA DE DETALLES DE REPARACIÓN")
            for fila in servicio.listar_detalles():
                print(fila)
        elif opcion == "3":
            fila = servicio.buscar_detalle(int(input("ID del detalle: ")))
            print(fila if fila else "Detalle no encontrado.")
        elif opcion == "5":
            servicio.eliminar_detalle(
                int(input("ID del detalle que deseas eliminar: "))
            )
        else:
            print("Opción no válida.")
def menu_inventario():
    servicio = ServicioInventario()

    while True:
        print("\n========== GESTIÓN DE REPUESTOS E INVENTARIO ==========")
        print("1. Registrar repuesto")
        print("2. Listar repuestos")
        print("3. Buscar repuesto")
        print("4. Actualizar repuesto")
        print("5. Actualizar stock")
        print("6. Eliminar repuesto")
        print("0. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            break
        elif opcion in ("1", "4"):
            id_repuesto = int(input("ID del repuesto: "))
            if opcion == "4" and not servicio.buscar_repuesto(id_repuesto):
                print("Repuesto no encontrado.")
                continue
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            precio = float(input("Precio: "))
            stock = int(input("Cantidad en stock: "))
            repuesto = Repuesto(id_repuesto, nombre, descripcion, precio, stock)
            if opcion == "1":
                servicio.registrar_repuesto(repuesto)
            else:
                servicio.actualizar_repuesto(repuesto)
        elif opcion == "2":
            print("\nLISTA DE REPUESTOS")
            for fila in servicio.listar_repuestos():
                print(fila)
        elif opcion == "3":
            fila = servicio.buscar_repuesto(int(input("ID del repuesto: ")))
            print(fila if fila else "Repuesto no encontrado.")
        elif opcion == "5":
            id_repuesto = int(input("ID del repuesto: "))
            nueva_cantidad = int(input("Nueva cantidad de stock: "))
            servicio.actualizar_stock(id_repuesto, nueva_cantidad)
        elif opcion == "6":
            servicio.eliminar_repuesto(
                int(input("ID del repuesto que deseas eliminar: "))
            )
        else:
            print("Opción no válida.")


def menu_alertas():
    servicio = ServicioMantenimiento()

    while True:
        print("\n========== GESTIÓN DE ALERTAS DE MANTENIMIENTO ==========")
        print("1. Registrar alerta")
        print("2. Listar alertas")
        print("3. Buscar alerta")
        print("4. Actualizar alerta")
        print("5. Eliminar alerta")
        print("0. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            break
        elif opcion in ("1", "4"):
            id_alerta = int(input("ID de la alerta: "))
            if opcion == "4" and not servicio.buscar_alerta(id_alerta):
                print("Alerta no encontrada.")
                continue
            id_vehiculo = int(input("ID del vehículo: "))
            vehiculo = crear_vehiculo_desde_id(id_vehiculo)
            if not vehiculo:
                print("El vehículo no existe.")
                continue
            fecha = input("Fecha programada (DD/MM/AAAA): ")
            mensaje = input("Mensaje de la alerta: ")
            kilometraje = int(input("Kilometraje programado: "))
            alerta = AlertaMantenimiento(
                id_alerta, vehiculo, fecha, mensaje, kilometraje
            )
            if opcion == "1":
                servicio.registrar_alerta(alerta)
            else:
                alerta.estado = input("Estado (Pendiente/Completada): ")
                servicio.actualizar_alerta(alerta)
        elif opcion == "2":
            print("\nLISTA DE ALERTAS")
            for fila in servicio.listar_alertas():
                print(fila)
        elif opcion == "3":
            fila = servicio.buscar_alerta(int(input("ID de la alerta: ")))
            print(fila if fila else "Alerta no encontrada.")
        elif opcion == "5":
            servicio.eliminar_alerta(
                int(input("ID de la alerta que deseas eliminar: "))
            )
        else:
            print("Opción no válida.")


def menu_estadisticas():
    estadisticas = obtener_estadisticas()
    print("\n========== ESTADÍSTICAS DE AUTOCARE ==========")
    print("Total de clientes:", estadisticas["clientes"])
    print("Total de vehículos:", estadisticas["vehiculos"])
    print("Total de mecánicos:", estadisticas["mecanicos"])


def mostrar_menu():
    print("\n" + "=" * 45)
    print("             AUTOCARE")
    print(" Sistema de Diagnóstico y Mantenimiento")
    print("=" * 45)
    print("1. Gestionar clientes")
    print("2. Gestionar vehículos")
    print("3. Gestionar mecánicos")
    print("4. Gestionar órdenes de reparación")
    print("5. Gestionar diagnósticos")
    print("6. Gestionar mantenimientos")
    print("7. Gestionar detalles de reparación")
    print("8. Gestionar repuestos e inventario")
    print("9. Gestionar alertas de mantenimiento")
    print("10. Consultar estadísticas")
    print("0. Salir")
    print("=" * 45)


def main():
    crear_tablas()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            print("\nGracias por utilizar AutoCare.")
            break
        elif opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_vehiculos()
        elif opcion == "3":
            menu_mecanicos()
        elif opcion == "4":
            menu_ordenes()
        elif opcion == "5":
            menu_diagnosticos()
        elif opcion == "6":
            menu_mantenimientos()
        elif opcion == "7":
            menu_detalles_reparacion()
        elif opcion == "8":
            menu_inventario()
        elif opcion == "9":
            menu_alertas()
        elif opcion == "10":
            menu_estadisticas()
        else:
            print("\nOpción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()