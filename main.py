
from datos.crear_tablas import crear_tablas
from modelos.cliente import Cliente
from servicios.servicio_clientes import ServicioClientes
from modelos.vehiculo import Vehiculo
from servicios.servicio_vehiculos import ServicioVehiculos
from servicios.servicio_clientes import ServicioClientes
from modelos.mecanico import Mecanico
from servicios.servicio_mecanicos import ServicioMecanicos
from modelos.orden_reparacion import OrdenReparacion
from servicios.servicio_reparaciones import ServicioReparaciones


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

            id_cliente = int(input("ID del cliente: "))
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")

            cliente = Cliente(
                id_cliente, nombre, telefono, correo
            )

            servicio.registrar_cliente(cliente)

        elif opcion == "2":
            print("\nLISTA DE CLIENTES")

            for cliente in servicio.listar_clientes():
                print(cliente)

        elif opcion == "3":
            id_cliente = int(input("ID del cliente que buscas: "))
            cliente = servicio.buscar_cliente(id_cliente)

            if cliente:
                print(cliente)
            else:
                print("Cliente no encontrado.")

        elif opcion == "4":
            print("\nACTUALIZAR CLIENTE")

            id_cliente = int(input("ID del cliente: "))
            nombre = input("Nuevo nombre: ")
            telefono = input("Nuevo teléfono: ")
            correo = input("Nuevo correo: ")

            cliente = Cliente(
                id_cliente, nombre, telefono, correo
            )

            servicio.actualizar_cliente(cliente)

        elif opcion == "5":
            id_cliente = int(input("ID del cliente que deseas eliminar: "))
            servicio.eliminar_cliente(id_cliente)

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

        elif opcion == "1":
            print("\nREGISTRAR VEHÍCULO")

            id_vehiculo = int(input("ID del vehículo: "))
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            patente = input("Patente: ")
            anio = int(input("Año: "))
            id_cliente = int(input("ID del propietario: "))

            cliente = Cliente(
                id_cliente, "", "", ""
            )

            vehiculo = Vehiculo(
                id_vehiculo, marca, modelo,
                patente, anio, cliente
            )

            servicio.registrar_vehiculo(vehiculo)

        elif opcion == "2":
            print("\nLISTA DE VEHÍCULOS")

            for vehiculo in servicio.listar_vehiculos():
                print(vehiculo)

        elif opcion == "3":
            id_vehiculo = int(input("ID del vehículo: "))
            vehiculo = servicio.buscar_vehiculo(id_vehiculo)

            if vehiculo:
                print(vehiculo)
            else:
                print("Vehículo no encontrado.")

        elif opcion == "4":
            print("\nACTUALIZAR VEHÍCULO")

            id_vehiculo = int(input("ID del vehículo: "))
            marca = input("Nueva marca: ")
            modelo = input("Nuevo modelo: ")
            patente = input("Nueva patente: ")
            anio = int(input("Nuevo año: "))
            id_cliente = int(input("ID del propietario: "))

            cliente = Cliente(
                id_cliente, "", "", ""
            )

            vehiculo = Vehiculo(
                id_vehiculo, marca, modelo,
                patente, anio, cliente
            )

            servicio.actualizar_vehiculo(vehiculo)

        elif opcion == "5":
            id_vehiculo = int(input("ID del vehículo que deseas eliminar: "))
            servicio.eliminar_vehiculo(id_vehiculo)

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

        elif opcion == "1":
            print("\nREGISTRAR MECÁNICO")

            id_mecanico = int(input("ID del mecánico: "))
            nombre = input("Nombre: ")
            especialidad = input("Especialidad: ")
            telefono = input("Teléfono: ")

            mecanico = Mecanico(
                id_mecanico, nombre, especialidad, telefono
            )

            servicio.registrar_mecanico(mecanico)

        elif opcion == "2":
            print("\nLISTA DE MECÁNICOS")

            for mecanico in servicio.listar_mecanicos():
                print(mecanico)

        elif opcion == "3":
            id_mecanico = int(input("ID del mecánico: "))
            mecanico = servicio.buscar_mecanico(id_mecanico)

            if mecanico:
                print(mecanico)
            else:
                print("Mecánico no encontrado.")

        elif opcion == "4":
            print("\nACTUALIZAR MECÁNICO")

            id_mecanico = int(input("ID del mecánico: "))
            nombre = input("Nuevo nombre: ")
            especialidad = input("Nueva especialidad: ")
            telefono = input("Nuevo teléfono: ")

            mecanico = Mecanico(
                id_mecanico, nombre, especialidad, telefono
            )

            servicio.actualizar_mecanico(mecanico)

        elif opcion == "5":
            id_mecanico = int(input("ID del mecánico que deseas eliminar: "))
            servicio.eliminar_mecanico(id_mecanico)

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
            print("\nREGISTRAR ORDEN")

            id_orden = int(input("ID de la orden: "))
            id_vehiculo = int(input("ID del vehículo: "))

            if not servicio_vehiculos.buscar_vehiculo(id_vehiculo):
                print("El vehículo no existe.")
                continue

            fecha = input("Fecha (DD/MM/AAAA): ")
            descripcion = input("Descripción de la reparación: ")

            id_mecanico = int(input("ID del mecánico asignado: "))

            if not servicio_mecanicos.buscar_mecanico(id_mecanico):
                print("El mecánico no existe.")
                continue

            vehiculo = Vehiculo(
                id_vehiculo, "", "", "", 0, None
            )

            orden = OrdenReparacion(
                id_orden, vehiculo, fecha, descripcion
            )

            mecanico = Mecanico(
                id_mecanico, "", "", ""
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
            print("\nACTUALIZAR ORDEN")

            id_orden = int(input("ID de la orden: "))
            id_vehiculo = int(input("ID del vehículo: "))

            fecha = input("Nueva fecha (DD/MM/AAAA): ")
            descripcion = input("Nueva descripción: ")
            estado = input("Nuevo estado: ")

            vehiculo = Vehiculo(
                id_vehiculo, "", "", "", 0, None
            )

            orden = OrdenReparacion(
                id_orden, vehiculo, fecha, descripcion
            )

            orden.cambiar_estado(estado)
            servicio.actualizar_orden(orden)

        elif opcion == "5":
            id_orden = int(input("ID de la orden que deseas eliminar: "))
            servicio.eliminar_orden(id_orden)

        else:
            print("Opción no válida.")
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
            print("\nGESTIÓN DE MANTENIMIENTOS")

        elif opcion == "7":
            print("\nGESTIÓN DE DETALLES DE REPARACIÓN")

        elif opcion == "8":
            print("\nGESTIÓN DE REPUESTOS E INVENTARIO")

        elif opcion == "9":
            print("\nGESTIÓN DE ALERTAS DE MANTENIMIENTO")

        elif opcion == "10":
            print("\nESTADÍSTICAS DE AUTOCARE")

        else:
            print("\nOpción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
