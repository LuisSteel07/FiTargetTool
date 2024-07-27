import flet as ft
from Controler.Controler import get_all_data
from Controler.Create import create_client
from Controler.Delete import delete_client
from Model.Cliente import Cliente
from View.AutoCompleteSuggestionData import auto_complete_suggestion_id_rutines


def list_edit_clients() -> ft.DataTable:
    list_clients: list[Cliente] = get_all_data()
    table_clients = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Edad")),
            ft.DataColumn(ft.Text("ID Rutina")),
            ft.DataColumn(ft.Text("Foto Path")),
            ft.DataColumn(ft.Text("Eliminar")),
            ft.DataColumn(ft.Text("Actualizar")),
        ]
    )

    for client in list_clients:
        table_clients.rows.append(
            ft.DataRow([
                ft.DataCell(ft.Text(f"{client.nombre}")),
                ft.DataCell(ft.Text(f"{client.edad}")),
                ft.DataCell(ft.Text(f"{client.rutina.id}")),
                ft.DataCell(ft.Text(f"{client.foto}")),
                ft.DataCell(ft.IconButton(ft.icons.DELETE,
                                          icon_color=ft.colors.RED,
                                          on_click=lambda e: delete_client(client))),
                ft.DataCell(ft.IconButton(ft.icons.UPDATE, icon_color=ft.colors.BLUE)),
            ])
        )
        print(client.id)

    return table_clients


def create_client_view(page: ft.Page):
    nombre = ft.TextField(tooltip="Nombre de el Cliente", label="Nombre: ")
    edad = ft.TextField(tooltip="Edad de el Cliente", label="Edad: ")
    rutina = ft.AutoComplete(suggestions=auto_complete_suggestion_id_rutines())
    foto = ft.TextField(tooltip="Ruta de la Foto", label="Foto: ")

    pecho = ft.TextField(tooltip="Valor", label="Valor Pecho: ")
    trapecio = ft.TextField(tooltip="Valor", label="Valor Trapecio: ")
    romboides = ft.TextField(tooltip="Valor", label="Valor Romboides: ")
    dorsal = ft.TextField(tooltip="Valor", label="Valor Dorsal: ")
    espalda_baja = ft.TextField(tooltip="Valor", label="Valor Espalda Baja: ")
    biceps = ft.TextField(tooltip="Valor", label="Valor Biceps: ")
    triceps = ft.TextField(tooltip="Valor", label="Valor Triceps: ")
    ante_brazo = ft.TextField(tooltip="Valor", label="Valor AnteBrazo: ")
    del_posterior = ft.TextField(tooltip="Valor", label="Valor Deltoides posterior: ")
    del_lateral = ft.TextField(tooltip="Valor", label="Valor Deltoides lateral: ")
    del_anterior = ft.TextField(tooltip="Valor", label="Valor Deltoides anterior: ")
    cuadriceps = ft.TextField(tooltip="Valor", label="Valor Cuádriceps: ")
    isq = ft.TextField(tooltip="Valor", label="Valor Isquiotibiales: ")
    gluteos = ft.TextField(tooltip="Valor", label="Valor Glúteos: ")
    pantorrillas = ft.TextField(tooltip="Valor", label="Valor Pantorrillas: ")

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Creando Cliente: "),
        content=ft.Column([
            ft.Row([nombre, edad]),
            ft.Row([ft.Text("ID de Rutina", size=18), rutina]), foto,
            ft.Container(
                ft.Column([
                    ft.Row([pecho, trapecio, romboides]),
                    ft.Row([dorsal, espalda_baja, biceps]),
                    ft.Row([triceps, ante_brazo, del_posterior]),
                    ft.Row([del_lateral, del_anterior, cuadriceps]),
                    ft.Row([isq, gluteos, pantorrillas]),
                ]),
                width=900
            )
        ]),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: page.close(alert)),
            ft.TextButton("Crear", on_click=lambda e: create_client(nombre.value, 1, 1, foto.value,
                                                                    [pecho.value, trapecio.value, romboides.value,
                                                                     dorsal.value, espalda_baja.value, biceps.value,
                                                                     triceps.value, ante_brazo.value,
                                                                     del_posterior.value, del_lateral.value,
                                                                     del_anterior.value, cuadriceps.value, isq.value,
                                                                     gluteos.value, pantorrillas.value, ]))
        ]
    )

    page.open(alert)
