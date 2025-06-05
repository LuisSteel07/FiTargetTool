import flet as ft

from Controler.Controler import get_list_id_rutines
from Controler.Update import change_rutine
from Components.AlertPanel import alert_invalid_data


def change_rutine_view(root: ft.Page, client_id: int):
    rutine = ft.Dropdown()

    for identifier in get_list_id_rutines():
        rutine.options.append(ft.dropdown.Option(str(identifier)))

    def validate():
        if rutine.value is None:
            alert_invalid_data(root)
        else:
            change_rutine(int(rutine.value), client_id)
        root.close(alert)

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Cambiando Rutina"),
        content=rutine,
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Cambiar", on_click=lambda e: validate()),
        ]
    )

    root.open(alert)