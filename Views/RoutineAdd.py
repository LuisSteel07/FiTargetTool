import flet as ft

from Controler.Update import update_rutina
from Model.Ejercicios import Ejercicios
from Model.Dia import Dia


class RoutineAdd(ft.View):
    def __init__(self, root: ft.Page, ident):
        super().__init__()
        self.root = root
        self.routine_id = ident
        self.route = "/routine/add"

        self.new_ejercicio = ft.TextField(label="Nuevo Ejercicio", tooltip="Diga el nuevo ejercicio a agregar")
        self.list_values_reps = ft.Row()
        self.list_values_weights = ft.Row()
        self.dia_control = ft.Dropdown(
            options=[
                ft.dropdown.Option(Dia.LUNES.value),
                ft.dropdown.Option(Dia.MARTES.value),
                ft.dropdown.Option(Dia.MIERCOLES.value),
                ft.dropdown.Option(Dia.JUEVES.value),
                ft.dropdown.Option(Dia.VIERNES.value),
                ft.dropdown.Option(Dia.SABADO.value),
                ft.dropdown.Option(Dia.DOMINGO.value),
            ],
            width=140,
        )
        self.cant_tandas = ft.TextField(
            label="Cantidad de Tandas",
            tooltip="Diga la cantidad de tandas del ejercicio",
            value="0",
            input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-8]*$", replacement_string="0"),
            on_change=lambda e: self.on_change_tandas()
        )

        self.controls = [
            ft.Row([
                ft.IconButton(ft.icons.ARROW_BACK, icon_size=25, on_click=lambda e: self.root.go(f"/routine/{self.routine_id}"))
            ]),
            ft.Row([
                ft.Column([
                    self.new_ejercicio,
                    self.dia_control,
                    self.cant_tandas,
                    self.list_values_reps,
                    self.list_values_weights,
                    ft.FilledButton("Guardar", ft.icons.CREATE, on_click=lambda e: self.save_instance())
                ])
            ])
        ]


    def on_change_tandas(self):
        try:
            if int(self.cant_tandas.value) > 0:
                self.list_values_reps.controls.clear()
                self.list_values_weights.controls.clear()
                for e in range(0, int(self.cant_tandas.value)):
                    self.list_values_reps.controls.append(ft.TextField(
                        label="Cantidad de Reps.",
                        tooltip="Diga la cantidad de reps del ejercicio",
                        value="0",
                        width=100,
                        input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-9999]*$", replacement_string="0")
                    ))
                    self.list_values_weights.controls.append(ft.TextField(
                        label="Cantidad de Peso.",
                        tooltip="Diga la cantidad de peso del ejercicio",
                        value="0",
                        width=100,
                        input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-99999999]*$", replacement_string="0")
                    ))
                self.root.update()
        except ValueError as e:
            self.list_values_reps.controls.clear()
            self.list_values_weights.controls.clear()
            self.root.update()
            print(f"Excepcion asegurada ((ValueError)) --> {e}")

    def create_ejercicio_object(self) -> Ejercicios:
        list_reps: list[int] = []
        list_weights: list[float] = []

        for rep in self.list_values_reps.controls:
            list_reps.append(int(rep.value))

        for weight in self.list_values_weights.controls:
            list_weights.append(float(weight.value))

        return Ejercicios(self.new_ejercicio.value, list_reps, list_weights)

    def save_instance(self):
        ejercicio = self.create_ejercicio_object()
        update_rutina(self.routine_id, self.dia_control.value, ejercicio)
        self.root.go(f"/routine/{self.routine_id}")