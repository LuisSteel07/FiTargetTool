import flet as ft

from Model.Cliente import Cliente
from Model.Photo import Photo


def info_cliente_view(cliente: Cliente) -> ft.Row:
    return ft.Row([
        ft.Image(
            cliente.foto,
            width=180,
            border_radius=ft.border_radius.all(100),
            error_content=ft.Image(Photo(None,None).photo_path, width=180)
        ),
        ft.Column(
            [
                ft.Text(f"Nombre: {cliente.nombre}", size=26, weight=ft.FontWeight.BOLD),
                ft.Text(f"Edad: {cliente.edad}", size=26, weight=ft.FontWeight.BOLD),
            ]
        )
    ], alignment=ft.MainAxisAlignment.CENTER)