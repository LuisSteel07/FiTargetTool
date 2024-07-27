from Model.Peso import Peso
from Model.Rutina import Rutina
from Model.Progreso import Progreso


class Cliente:
    def __init__(self, _id: int, _nombre: str, _edad: int, _rutina: Rutina, _progreso: Progreso, _pesos: Peso, _foto: str):
        self.id = _id
        self.nombre = _nombre
        self.edad = _edad
        self.rutina = _rutina
        self.progreso = _progreso
        self.pesos = _pesos
        self.foto = _foto
