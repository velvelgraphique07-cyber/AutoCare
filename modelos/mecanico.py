
class Mecanico:
    """
    Representa a un mecánico que trabaja en AutoCare.
    """

    def __init__(self, id_mecanico, nombre, especialidad, telefono):
        self.id_mecanico = id_mecanico
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono
        self.disponible = True

    def mostrar_informacion(self):
        print("=== INFORMACIÓN DEL MECÁNICO ===")
        print("ID:", self.id_mecanico)
        print("Nombre:", self.nombre)
        print("Especialidad:", self.especialidad)
        print("Teléfono:", self.telefono)
        print("Disponible:", "Sí" if self.disponible else "No")
