import flet as ft

from Controler.Controler import get_list_id_rutines, get_routine
from Model.Rutina import Rutina


class RowActionRoutine:
    def __init__(self, num, name, root: ft.Page):
        self.num = num,
        self.name = name,
        self.root = root

    def get_datarow(self):
        return ft.DataRow([
            ft.DataCell(ft.Text(f"{self.num[0]}")),
            ft.DataCell(ft.Text(self.name[0])),
            ft.IconButton(ft.icons.EDIT, width=45, on_click=lambda e: self.root.go(f"/routine/{self.num[0]}"))
        ])


class RoutineView(ft.View):
    def __init__(self, root: ft.Page):
        super().__init__()
        self.route = "/routines"
        self.root = root

        self.table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Nombre")),
                ft.DataColumn(ft.Text("Editar")),
            ],
            rows=self.get_rows_table_view()
        )

        self.controls = [
            ft.Row([
                ft.IconButton(ft.icons.ARROW_BACK, icon_size=25, on_click=lambda e: self.root.go("/"))
            ]),
            ft.Row(
                controls = [
                    ft.Container(
                        content=self.table,
                        margin=10,
                        padding=20,
                        bgcolor=ft.colors.YELLOW_900,
                        border_radius=20,
                        width=480
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),

        ]

    def get_rows_table_view(self) -> list[ft.DataRow]:
        rutines_id = get_list_id_rutines()
        table_rows: list[ft.DataRow] = []
        rutines: list[Rutina] = []

        for i in rutines_id:
            rutines.append(get_routine(i))

        for rutine in rutines:
            table_rows.append(self.create_data_row(rutine.id, rutine.nombre))

        return table_rows

    def create_data_row(self, identifier, name) -> ft.DataRow:
        return ft.DataRow(cells=[
            ft.DataCell(ft.Text(f"{identifier}")),
            ft.DataCell(ft.Text(f"{name}")),
            ft.DataCell(ft.IconButton(ft.icons.EDIT, width=45, on_click=lambda e: self.root.go(f"/routine/{identifier}")))
        ])