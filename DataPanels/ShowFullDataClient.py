import flet as ft

from Controler.Controler import get_all_data


def rows_table_clients() -> list[ft.DataRow]:
    data_rows_table: list[ft.DataRow] = []
    list_clients = get_all_data()

    for client in list_clients:
        data_rows_table.append(ft.DataRow([
            ft.DataCell(ft.Text(f"{client.id}")),
            ft.DataCell(ft.Text(f"{client.nombre}")),
            ft.DataCell(ft.Text(f"{client.edad}")),
            ft.DataCell(ft.Text(f"{client.progreso}")),
            ft.DataCell(ft.Text(f"{client.rutina}")),
            ft.DataCell(ft.Text(f"{client.pesos}")),
            ft.DataCell(ft.Text(f"{client.foto}")),
        ]))

    return data_rows_table

def create_datatable_clients() -> ft.DataTable:
    return ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Edad")),
            ft.DataColumn(ft.Text("Rutina")),
            ft.DataColumn(ft.Text("Progreso")),
            ft.DataColumn(ft.Text("Pesos")),
            ft.DataColumn(ft.Text("Foto")),
        ],
        rows=rows_table_clients()
    )

def show_full_datatable(root: ft.Page):
    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Información General"),
        content=create_datatable_clients(),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert))
        ]
    )

    root.open(alert)