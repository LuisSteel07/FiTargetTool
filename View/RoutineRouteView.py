import flet as ft


class RoutineRouteView:
    def __init__(self, page: ft.Page):
        self.page = page

    def showView(self):
        return ft.View(
                    route="/routine",
                    controls=[
                        ft.Row([
                            ft.IconButton(ft.icons.ARROW_BACK, icon_size=25, on_click=lambda e: self.page.views.pop())
                        ]),
                        ft.Row([
                            ft.Column([
                                ft.Text("Wassaaaaaaa")
                            ]),
                            ft.Column([
                                new_ejercicio,
                                dia_control,
                                cant_tandas,
                                ft.Row(list_values_reps),
                                ft.Row(list_values_weights),
                                ft.FilledButton("Guardar", ft.icons.CREATE)
                            ])
                        ])
                    ]
                )