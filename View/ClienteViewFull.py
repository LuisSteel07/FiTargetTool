from flet import (TextButton, colors, AutoCompleteSuggestion, Column, MainAxisAlignment, Page, Row, Text, Container,
                  FontWeight, FilledButton, ButtonStyle)
from View.InfoClienteView import info_cliente_view
from View.ProgressGraphics import collection_graphics_view, show_graphic
from View.RutineView import routine_view
from View.EditData import add_peso, add_rutine, change_rutine_view, change_client_view, modify_rutine
from Controler.Controler import get_client


def show_client_view(root: Page, data: AutoCompleteSuggestion) -> Column:
    client = get_client(data.value)
    return Column(
        [
            FilledButton("Editar Valores", on_click=lambda e: change_client_view(root, client.id)),
            info_cliente_view(client),
            Container(
                content=Column([
                    Row([
                        Text(f"{client.rutina.nombre}", size=20, weight=FontWeight.BOLD),
                        TextButton("Agregar Ejercicio",
                                   style=ButtonStyle(color=colors.BLACK, overlay_color=colors.BLUE_GREY_800),
                                   on_click=lambda e: add_rutine(root, client.rutina.id)
                                   ),
                        TextButton("Cambiar Rutina",
                                   style=ButtonStyle(color=colors.BLACK, overlay_color=colors.BLUE_GREY_800),
                                   on_click=lambda e: change_rutine_view(root, client.rutina.id)
                                   ),
                        TextButton("Modificar Rutina",
                                   style=ButtonStyle(color=colors.BLACK, overlay_color=colors.BLUE_GREY_800),
                                   on_click=lambda e: modify_rutine(root, client.rutina, client.rutina.id)
                                   )
                    ]),
                    routine_view(client.rutina)
                ]),
                margin=10,
                padding=20,
                bgcolor=colors.BLUE_GREY,
                border_radius=20,
                width=950
            ),
            Row([
                Container(
                    content=collection_graphics_view(root, client.progreso),
                    width=400,
                    padding=10
                ),
                Column([
                    Row([

                        Text("Registro de Pesos", size=22, weight=FontWeight.BOLD),
                        TextButton("Agregar Peso", on_click=lambda e: add_peso(root, client.pesos.id))
                    ]),
                    Container(
                        content=show_graphic(client.pesos.list_pesos),
                        width=400,
                        padding=10
                    )
                ])
            ], wrap=True)
        ],
        alignment=MainAxisAlignment.CENTER,
    )
