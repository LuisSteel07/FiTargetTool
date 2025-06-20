import flet as ft

from Components.UserData import info_cliente_view
from Controler.Delete import delete_client
from DataPanels.AddPeso import add_peso
from DataPanels.ChangeDataUser import change_client_view
from DataPanels.ProgressGraphics import collection_graphics_view, show_graphic
from Components.RoutineComponent import routine_view
from Controler.Controler import get_client



class ClientView(ft.View):
    def __init__(self, root: ft.Page, data: str):
        super().__init__()
        self.root = root
        self.client = get_client(name=data)
        self.scroll = ft.ScrollMode.ALWAYS

        self.controls.append(
            ft.Column(
                [
                    ft.Row([
                        ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: self.root.go("/"))
                    ]),
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.icons.DELETE_ROUNDED,
                                bgcolor=ft.colors.RED_400,
                                icon_color=ft.colors.RED_900,
                                on_click=lambda e: {
                                    delete_client(self.client),
                                    self.root.go("/")
                                }
                            ),
                            ft.FilledButton(
                                "Editar Valores",
                                on_click=lambda e: change_client_view(root, self.client.id),
                            ),
                            info_cliente_view(self.client)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row([
                        ft.Container(
                            content=ft.Column([
                                ft.Text(f"Rutina: {self.client.rutina.nombre}", size=25, weight=ft.FontWeight.BOLD),
                                routine_view(self.client.rutina, root)
                            ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            margin=10,
                            padding=20,
                            bgcolor=ft.colors.YELLOW_800,
                            border_radius=20,
                            width=950,
                        ),
                    ],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([
                        ft.Container(
                            content=collection_graphics_view(root, self.client.progreso),
                            width=400,
                            padding=10
                        ),
                        ft.Column([
                            ft.Row([
                                ft.Text("Registro de Pesos", size=22, weight=ft.FontWeight.BOLD),
                                ft.TextButton("Agregar Peso", on_click=lambda e: add_peso(root, self.client.pesos.id))
                            ]),
                            ft.Container(
                                content=show_graphic(self.client.pesos.list_pesos),
                                width=400,
                                padding=10
                            )
                        ])
                    ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER)
                ],
            )
        )