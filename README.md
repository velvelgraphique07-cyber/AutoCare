# AUTOCARE
## Sistema de Diagnóstico y Mantenimiento Preventivo de Vehículos

**Proyecto académico desarrollado en Python y SQLite.**

### 1. Descripción del proyecto

AutoCare es un sistema de gestión diseñado para organizar y administrar las actividades de un taller mecánico. Permite registrar clientes y vehículos, gestionar mecánicos, controlar órdenes de reparación, almacenar diagnósticos y mantenimientos, administrar repuestos e inventario y generar alertas de mantenimiento.

El objetivo principal es facilitar la organización de la información del taller y mejorar el seguimiento de los trabajos realizados en cada vehículo.

### 2. Objetivos

- Gestionar la información de los clientes y sus vehículos.
- Registrar y consultar mecánicos.
- Administrar órdenes de reparación y asignaciones de mecánicos.
- Registrar diagnósticos y mantenimientos.
- Controlar detalles de reparación y repuestos.
- Gestionar el inventario.
- Crear alertas para recordar futuros mantenimientos.
- Consultar estadísticas básicas del taller.

### 3. Tecnologías utilizadas

- **Python:** lenguaje de programación utilizado para desarrollar el sistema.
- **SQLite:** sistema de base de datos para almacenar la información.
- **Visual Studio Code:** entorno de desarrollo.
- **Git y GitHub:** herramientas utilizadas para el control de versiones y almacenamiento del código fuente.

### 4. Funcionalidades principales

El sistema cuenta con un menú principal que permite acceder a los siguientes módulos:

1. Gestión de clientes.
2. Gestión de vehículos.
3. Gestión de mecánicos.
4. Gestión de órdenes de reparación.
5. Gestión de diagnósticos.
6. Gestión de mantenimientos.
7. Gestión de detalles de reparación.
8. Gestión de repuestos e inventario.
9. Gestión de alertas de mantenimiento.
10. Consulta de estadísticas.

Los módulos de gestión permiten realizar operaciones de registro, consulta, búsqueda, actualización y eliminación, según las opciones disponibles en cada módulo.

### 5. Estructura del proyecto

El proyecto está organizado en diferentes carpetas para separar las responsabilidades del sistema:

```text
AutoCare/
│
├── datos/
│   ├── conexion.py
│   ├── crear_tablas.py
│   └── estadisticas.py
│
├── interfaz/
│   └── ventana_principal.py
│
├── modelos/
│   ├── alerta_mantenimiento.py
│   ├── cliente.py
│   ├── detalle_reparacion.py
│   ├── diagnostico.py
│   ├── gestor_taller.py
│   ├── mantenimiento.py
│   ├── mecanico.py
│   ├── orden_reparacion.py
│   ├── repuesto.py
│   └── vehiculo.py
│
├── repositories/
│   ├── alertas.py
│   ├── clientes.py
│   ├── detalles_reparacion.py
│   ├── diagnosticos.py
│   ├── mantenimientos.py
│   ├── mecanicos.py
│   ├── reparaciones.py
│   ├── repuestos.py
│   └── vehiculos.py
│
├── servicios/
│   ├── servicio_clientes.py
│   ├── servicio_detalles_reparacion.py
│   ├── servicio_diagnosticos.py
│   ├── servicio_inventario.py
│   ├── servicio_mantenimiento.py
│   ├── servicio_mecanicos.py
│   ├── servicio_reparaciones.py
│   └── servicio_vehiculos.py
│
├── main.py
├── README.md
└── .gitignore
```

**Descripción de las carpetas:**

- **modelos:** contiene las clases que representan las entidades del sistema.
- **datos:** administra la conexión con SQLite, la creación de tablas y las estadísticas.
- **repositories:** contiene las operaciones de acceso y gestión de los datos almacenados.
- **servicios:** organiza la lógica y las operaciones de cada módulo.
- **interfaz:** contiene la ventana gráfica desarrollada con Tkinter.
- **main.py:** archivo principal que inicia el sistema mediante un menú de consola.

### 6. Clases principales

El sistema está organizado alrededor de diez clases principales:

- Cliente
- GestorTaller
- Mecanico
- Vehiculo
- OrdenReparacion
- Diagnostico
- Mantenimiento
- DetalleReparacion
- Repuesto
- AlertaMantenimiento

Estas clases representan las entidades principales y las responsabilidades del sistema AutoCare.

### 7. Interfaz gráfica

El proyecto incluye una interfaz gráfica inicial desarrollada con **Tkinter**, que presenta:

- Encabezado con el nombre AutoCare.
- Menú lateral de navegación.
- Área principal de contenido.
- Tarjetas con estadísticas de clientes, vehículos y mecánicos.

La interfaz permite seleccionar distintas secciones del sistema. Su desarrollo puede ampliarse para conectar cada opción con las operaciones de gestión correspondientes.
### 8. Requisitos para ejecutar el proyecto

Para ejecutar AutoCare se necesita:

- Tener Python instalado.
- Disponer de Visual Studio Code o una terminal.
- Tener acceso a los archivos del proyecto.

SQLite está integrado en la biblioteca estándar de Python, por lo que no requiere una instalación adicional para este proyecto.

### 9. Instalación y ejecución

**Paso 1.** Clonar el repositorio:

```bash
git clone https://github.com/velvelgraphique07-cyber/AutoCare.git
```

**Paso 2.** Entrar en la carpeta del proyecto:

```bash
cd AutoCare
```

**Paso 3.** Ejecutar el programa:

```bash
python main.py
```

Al iniciar, el sistema crea las tablas necesarias de la base de datos y muestra el menú principal.

### 10. Base de datos

AutoCare utiliza SQLite para almacenar los registros del sistema en una base de datos local.

El archivo de base de datos se genera y utiliza localmente. No es necesario incluir una base de datos personal con información de prueba en el repositorio público.

### 11. Control de versiones

El proyecto utiliza Git para registrar los cambios realizados durante el desarrollo y GitHub para alojar el repositorio remoto.

**Repositorio:** https://github.com/velvelgraphique07-cyber/AutoCare

### 12. Autoría

Proyecto académico desarrollado como parte de la formación en Desarrollo de Sistemas.

**Nombre del proyecto:** AutoCare  
**Área:** Desarrollo de Sistemas  
**Lenguaje:** Python  
**Base de datos:** SQLite