import flet as ft

from Controler.Create import create_routine
from Components.AlertPanel import alert_invalid_data


def create_routine_view(root: ft.Page):
    name = ft.TextField(label="Nombre de la Rutina")

    def validate():
        root.close(alert)
        if name.value == "" or name.value == " ":
            alert_invalid_data(root)
        else:
            create_routine(name.value)

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Creando Rutina"),
        content=name,
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Agregar", on_click=lambda e: validate())
        ]
    )

    root.open(alert)