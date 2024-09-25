from Model.Ejercicios import Ejercicios


class Rutina:
    def __init__(self, _id: int, _nombre: str, _lunes: list[Ejercicios], _martes: list[Ejercicios], _miercoles: list[Ejercicios], _jueves: list[Ejercicios], _viernes: list[Ejercicios], _sabado: list[Ejercicios], _domingo: list[Ejercicios]):
        self.id = _id
        self.nombre = _nombre
        self.lunes = _lunes
        self.martes = _martes
        self.miercoles = _miercoles
        self.jueves = _jueves
        self.viernes = _viernes
        self.sabado = _sabado
        self.domingo = _domingo
