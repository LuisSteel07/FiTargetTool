import flet as ft

from Controler.Create import create_client
from Components.AlertPanel import alert_invalid_data
from Components.PhotoComponent import PhotoComponent


def create_client_view(root: ft.Page):
    nombre = ft.TextField(tooltip="Nombre del Cliente", label="Nombre: ")
    foto = PhotoComponent(root)
    edad = ft.TextField(tooltip="Edad del Cliente", label="Edad: ")
    peso = ft.TextField(tooltip="Peso del Cliente (lb)", label="Peso: ")
    rutina = ft.TextField(tooltip="ID Rutina", label="Rutina: ")

    list_textfield: list[ft.TextField] = [
        ft.TextField(tooltip="Valor", label="Valor Pecho: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor Trapecio: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor Romboides: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor Dorsal: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor Espalda Baja: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor Biceps: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor Triceps: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor AnteBrazo: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor Deltoides posterior: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor Deltoides lateral: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor Deltoides anterior: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor Cuádriceps: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor Isquiotibiales: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor Glúteos: ", width=220),
        ft.TextField(tooltip="Valor", label="Valor Pantorrillas: ", width=220)
    ]

    list_progress: list[int] = []

    def validate():
        root.close(alert)
        list_progress.clear()

        try:
            list_progress.extend(int(tf.value) for tf in list_textfield)
            if foto.path_text == "":
                raise ValueError

            create_client(
                nombre.value,
                int(edad.value),
                int(peso.value),
                int(rutina.value),
                foto.path_text.value,
                list_textfield
            )
        except ValueError:
            root.open(alert_invalid_data(root))
        except TypeError:
            root.open(alert_invalid_data(root, "Debe de seleccionar una foto"))

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Creando Cliente: "),
        content=ft.Column([
            ft.Row([nombre, edad]),
            ft.Row([rutina, peso]), foto.show(),
            ft.Container(
                ft.Row(list_textfield, wrap=True),
                width=900
            )
        ]),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Crear", on_click=lambda e: validate())
        ]
    )

    root.open(alert)