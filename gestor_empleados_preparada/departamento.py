class Departamento:
    def __init__(self, id: int, nombre: str, empleados_necesarios: int, presupuesto: float, horas_disponibles: float):
        self.id = id
        self.nombre = nombre
        self.empleados_necesarios = empleados_necesarios
        self.presupuesto = presupuesto
        self.horas_disponibles = horas_disponibles

    def es_valido(self) -> bool:
        if self.id <= 0:
            return False
        if not self.nombre or not self.nombre.strip():
            return False
        if self.empleados_necesarios < 0:
            return False
        if self.presupuesto < 0:
            return False
        if self.horas_disponibles < 0:
            return False
        return True
