from flet import Row, Image, Column, Text, MainAxisAlignment, FontWeight
from Model.Cliente import Cliente


def info_cliente_view(cliente: Cliente) -> Row:
    return Row([
        Image(cliente.foto),
        Column(
            [
                Text(f"Nombre: {cliente.nombre}", size=26, weight=FontWeight.BOLD),
                Text(f"Edad: {cliente.edad}", size=26, weight=FontWeight.BOLD),
            ]
        )
    ], alignment=MainAxisAlignment.CENTER)
