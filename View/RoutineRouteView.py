import flet as ft

from Model.Dia import Dia


class RoutineRouteView:
    def __init__(self, page: ft.Page, ident):
        self.page = page
        self.routine_id = ident
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

    def show_view(self):
        return ft.View(
            route="/routine",
            controls=[
                ft.Row([
                    ft.IconButton(ft.icons.ARROW_BACK, icon_size=25, on_click=lambda e: self.page.go("/"))
                ]),
                ft.Row([
                    ft.Column([
                        self.new_ejercicio,
                        self.dia_control,
                        self.cant_tandas,
                        self.list_values_reps,
                        self.list_values_weights,
                        ft.FilledButton("Guardar", ft.icons.CREATE)
                    ])
                ])
            ]
        )

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
                self.page.update()
        except ValueError as e:
            self.list_values_reps.controls.clear()
            self.list_values_weights.controls.clear()
            self.page.update()
            print(f"Excepcion asegurada ((ValueError)) --> {e}")
