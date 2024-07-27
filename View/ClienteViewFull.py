from flet import TextButton, colors, AutoCompleteSuggestion, Column, MainAxisAlignment, Page, Row, Text, Container, FontWeight
from View.InfoClienteView import info_cliente_view
from View.ProgressGraphics import collection_graphics_view, show_graphic
from Controler.Controler import get_client
from View.RutineView import routine_view


def show_client_view(root: Page, data: AutoCompleteSuggestion) -> Column:
    client = get_client(data.value)
    return Column(
        [
            info_cliente_view(client),
            Container(
                content=routine_view(client.rutina),
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
                        TextButton("Agregar Peso")
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
