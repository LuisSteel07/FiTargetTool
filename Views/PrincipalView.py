import flet as ft

from Components.AutoCompleteSuggestionData import auto_complete_suggestion_data
from DataPanels.CreateClient import create_client_view
from DataPanels.CreateRoutine import create_routine_view
from DataPanels.ShowFullDataClient import show_full_datatable


class PrincipalView(ft.View):
    def __init__(self, root: ft.Page):
        super().__init__()
        self.route = "/"
        self.root = root
        self.adaptive = True,
        self.scroll = ft.ScrollMode.ALWAYS

        self.input_search = ft.AutoComplete(
            suggestions=auto_complete_suggestion_data(),
            on_select=lambda e: self.root.go(f"/client/{e.selection.value}"),
        )

        self.controls = [
            ft.Row([
                ft.TextButton(
                    "Crear Cliente",
                    on_click=lambda e: create_client_view(self.root)
                ),
                ft.TextButton(
                    "Crear Rutina",
                    on_click=lambda e: create_routine_view(self.root)
                ),
                ft.TextButton(
                    "Ver Clientes",
                    tooltip="Muestra una lista de todos los clientes",
                    on_click=lambda e: show_full_datatable(self.root)
                ),
                ft.TextButton(
                    "Rutinas",
                    tooltip="Muestra una lista de las Rutinas creadas",
                    on_click=lambda e: self.root.go("/routines")
                ),
            ]),
            ft.Row([
                ft.Column([
                    ft.Text("Nombre de Cliente: ", size=22, weight=ft.FontWeight.BOLD),
                    ft.Container(
                        content=self.input_search,
                        bgcolor=ft.colors.BLUE_GREY,
                        width=400,
                        padding=10,
                        border_radius=20
                    )
                ])
            ], alignment=ft.MainAxisAlignment.CENTER)
        ]
