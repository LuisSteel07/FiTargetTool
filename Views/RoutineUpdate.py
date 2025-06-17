import flet as ft

from Controler.Controler import get_routine
from Components.RoutineComponent import routine_view


class RoutineUpdate(ft.View):
    def __init__(self, root: ft.Page, identifier):
        super().__init__()
        self.root = root
        self.route = self.root.route
        self.identifier = identifier
        self.routine = get_routine(self.identifier)

        self.routine_list = ft.Container(
            content=routine_view(self.routine, self.root),
            margin=10,
            padding=20,
            bgcolor=ft.colors.YELLOW_900,
            border_radius=20,
            width=960
        )

        self.controls = [
            ft.Row([
                ft.IconButton(ft.icons.ARROW_BACK, icon_size=25, on_click=lambda e: self.root.go("/routines")),
            ]),
            ft.Row([
                ft.Column([
                    ft.Row([
                        ft.IconButton(
                            ft.icons.ADD,
                            icon_size=25,
                            on_click=lambda e: self.root.go(f"/routine/add/{self.identifier}"),
                            tooltip="Crear nuevo ejercicio"
                        ),
                        ft.IconButton(
                            ft.icons.DELETE,
                            icon_size=25,
                            on_click=lambda e: self.root.go(f"/routine/delete/{self.identifier}"),
                            tooltip="Eliminar un ejercicio"
                        ),
                        ft.IconButton(
                            ft.icons.UPDATE,
                            icon_size=25,
                            on_click=lambda e: self.root.go(f"/routine/update/{self.identifier}"),
                            tooltip="Edita los nombres de los ejercicios"
                        ),
                        ft.IconButton(
                            ft.icons.SORT,
                            icon_size=25,
                            on_click=lambda e: self.root.go(f"/routine/order/{self.identifier}"),
                            tooltip="Ordena los ejercicios"
                        )
                    ]),
                    self.routine_list
                ])
            ], alignment=ft.MainAxisAlignment.CENTER),
        ]