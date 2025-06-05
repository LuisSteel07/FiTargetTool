import flet as ft

from Controler.Controler import get_client
from Controler.Update import update_client_data
from Model.Photo import Photo
from Components.AlertPanel import alert_invalid_data
from Components.PhotoComponent import PhotoComponent


def change_client_view(root: ft.Page, client_id: int):
    old_client = get_client(client_id=client_id)
    name = ft.TextField(label="Nuevo Nombre", tooltip="Nombre", value=old_client.nombre)
    age = ft.TextField(label="Nuevo Edad", tooltip="Edad", value=f"{old_client.edad}")
    photo = PhotoComponent(root)
    photo.path_text.value = old_client.foto

    def validacion():
        if name.value == "" or name.value == " " or age.value == "" or age.value == " " or not age.value.isdigit() or photo.path_text.value == "":
            alert_invalid_data(root)
        else:
            if old_client.foto == photo.path_text.value:
                update_client_data(client_id, name.value, int(age.value),old_client.foto)
            update_client_data(client_id, name.value, int(age.value), Photo(photo.path_text.value, client_id).photo_path)
        root.close(alert)
        root.go("/")
        root.go(f"/client/{name.value}")

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Actualizando Cliente"),
        content=ft.Column([
            name,
            age,
            photo.show()
        ], width=480, height=480),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Actualizar", on_click=lambda e: validacion())
        ]
    )

    root.open(alert)