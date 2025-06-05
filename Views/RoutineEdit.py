import flet as ft

from Controler.Controler import get_routine
from Controler.Update import update_full_routine
from Model.Ejercicios import Ejercicios
from Model.Rutina import Rutina


def extract_list_exercises(list_new_value_name: list[ft.TextField], list_exercises: list[Ejercicios]) -> list[Ejercicios]:
    new_list_exercises: list[Ejercicios] = []
    list_new_value_name.pop(0)
    position = 0

    for new_value_name in list_new_value_name:
        new_list_exercises.append(
            Ejercicios(
                new_value_name.value,
                list_exercises[position].reps[0],
                list_exercises[position].weights
            )
        )
        position += 1

    return new_list_exercises


class TableRoutineEdit:
    def __init__(self, identifier):
        self.identifier = identifier
        self.routine = get_routine(self.identifier)

        def list_textfield_routine(list_exercises, dia: str) -> list:
            list_textfield = [ft.Text(value=dia, size=18, color=ft.colors.BLUE)]

            if len(list_exercises) == 0:
                list_textfield.append(ft.Text("Vacío", size=18, color=ft.colors.RED))
            else:
                for exercise in list_exercises:
                    list_textfield.append(ft.TextField(value=exercise.name[0], width=120))

            return list_textfield

        self.list_lunes: list[ft.TextField] = list_textfield_routine(self.routine.lunes, "Lunes")
        self.list_martes: list[ft.TextField] = list_textfield_routine(self.routine.martes, "Martes")
        self.list_miercoles: list[ft.TextField] = list_textfield_routine(self.routine.miercoles, "Miércoles")
        self.list_jueves: list[ft.TextField] = list_textfield_routine(self.routine.jueves, "Jueves")
        self.list_viernes: list[ft.TextField] = list_textfield_routine(self.routine.viernes, "Viernes")
        self.list_sabado: list[ft.TextField] = list_textfield_routine(self.routine.sabado, "Sábado")
        self.list_domingo: list[ft.TextField] = list_textfield_routine(self.routine.domingo, "Domingo")

    def show_table(self):
        return ft.Row([
            ft.Column(self.list_lunes, width=130),
            ft.Column(self.list_martes, width=130),
            ft.Column(self.list_miercoles, width=130),
            ft.Column(self.list_jueves, width=130),
            ft.Column(self.list_viernes, width=130),
            ft.Column(self.list_sabado, width=130),
            ft.Column(self.list_domingo, width=130),
        ])

    def extract_routine_values(self) -> Rutina:
        routine: Rutina = Rutina(self.identifier, self.routine.nombre, [], [], [], [], [], [], [])
        list_textfield = [self.list_lunes, self.list_martes, self.list_miercoles, self.list_jueves, self.list_viernes, self.list_sabado, self.list_domingo]

        for day in range(0, 6):


            for new_ejers in list_textfield[day]:
                if new_ejers.value == "Vacío" or new_ejers.value == "" or new_ejers.value == " " or new_ejers.value == "Lunes" or new_ejers.value == "Martes" or new_ejers.value == "Miércoles" or new_ejers.value == "Jueves" or new_ejers.value == "Viernes" or new_ejers.value == "Sábado" or new_ejers.value == "Domingo":
                    continue
                elif day == 0:
                    routine.lunes = extract_list_exercises(list_textfield[day], self.routine.lunes)
                elif day == 1:
                    routine.martes = extract_list_exercises(list_textfield[day], self.routine.martes)
                elif day == 2:
                    routine.miercoles = extract_list_exercises(list_textfield[day], self.routine.miercoles)
                elif day == 3:
                    routine.jueves = extract_list_exercises(list_textfield[day], self.routine.jueves)
                elif day == 4:
                    routine.viernes = extract_list_exercises(list_textfield[day], self.routine.viernes)
                elif day == 5:
                    routine.sabado = extract_list_exercises(list_textfield[day], self.routine.sabado)
                elif day == 6:
                    routine.domingo = extract_list_exercises(list_textfield[day], self.routine.domingo)
        return routine


class RoutineEdit(ft.View):
    def __init__(self, root: ft.Page, identifier):
        super().__init__()
        self.root = root
        self.route = "/routine/delete"
        self.identifier = identifier
        self.routine = get_routine(self.identifier)
        self.table_routine = TableRoutineEdit(self.identifier)

        self.controls = [
            ft.Row([
                ft.IconButton(ft.icons.ARROW_BACK, icon_size=25, on_click=lambda e: self.root.go(f"/routine/{self.identifier}")),
            ]),
            ft.Row([
                ft.Container(
                    content=self.table_routine.show_table(),
                    width=1000,
                    height=800
                ),
                ft.TextButton("Guardar", on_click=lambda e: self.modify_routine()),
            ],alignment=ft.MainAxisAlignment.CENTER)
        ]

    def modify_routine(self):
        update_full_routine(self.identifier, self.table_routine.extract_routine_values())
        self.root.go(f"/routine/{self.identifier}")
