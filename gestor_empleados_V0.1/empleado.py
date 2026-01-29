# Definimos la clase empleado
class Empleado:
    def __init__(self, id, nombre, apellidos, edad,correo, departamento):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.correo = correo
        self.departamento = departamento

    # Método que comprueba si los datos del empleado son válidos
    def es_valido(self):
        if not self.id or not self.nombre or not self.apellidos or not self.edad or not self.correo or not self.departamento:
            return False
        if not isinstance(self.edad, int) or self.edad <= 0:
            return False
        return True