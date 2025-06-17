import flet as ft

from Model.Ejercicios import Ejercicios


class DragExerciseTarget(ft.DragTarget):
    def __init__(self, identifier: int, ejercicio: Ejercicios):
        self.identifier = identifier
        self.content = ft.Container(
            content=ft.Row([
                ft.Text(f"{self.identifier}"),
                ft.Text(f"{ejercicio.name[0]}")
            ])
        )

        super().__init__(self.content)

class RoutineOrder(ft.View):
    def __init__(self, root: ft.Page, routine_id: int):
        super().__init__()
        self.route = "/routine/order"
        self.root = root
        self.routine_id = routine_id

        self.controls = [
            ft.Row([
                ft.IconButton(ft.icons.ARROW_BACK, icon_size=25, on_click=lambda e: self.root.go("/"))
            ])
        ]