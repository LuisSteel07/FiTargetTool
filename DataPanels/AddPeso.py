import flet as ft

from Controler.Update import update_peso
from Components.AlertPanel import alert_invalid_data


def add_peso(root: ft.Page, peso_id: int):
    peso = ft.TextField(label="Agrega Peso")

    def validate():
        root.close(alert)
        if peso.value == "" or peso.value == " " or not peso.value.isdigit():
            alert_invalid_data(root)
        else:
            update_peso(peso_id, int(peso.value))

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Agregando Peso: "),
        content=peso,
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Agregar", on_click=lambda e: validate())
        ]
    )

    root.open(alert)