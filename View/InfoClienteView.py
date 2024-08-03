from flet import DataTable, DataRow, DataColumn, DataCell, TextButton, Page, Row, Image, Column, Text, \
    MainAxisAlignment, FontWeight, AlertDialog, Container

from Controler.Controler import get_all_data
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


def rows_table_clients() -> list[DataRow]:
    data_rows_table: list[DataRow] = []
    list_clients = get_all_data()

    for client in list_clients:
        data_rows_table.append(DataRow([
            DataCell(Text(f"{client.id}")),
            DataCell(Text(f"{client.nombre}")),
            DataCell(Text(f"{client.edad}")),
            DataCell(Text(f"{client.progreso}")),
            DataCell(Text(f"{client.rutina}")),
            DataCell(Text(f"{client.pesos}")),
            DataCell(Text(f"{client.foto}")),
        ]))

    return data_rows_table


def create_datatable_clients() -> DataTable:
    return DataTable(
        columns=[
            DataColumn(Text("ID")),
            DataColumn(Text("Nombre")),
            DataColumn(Text("Edad")),
            DataColumn(Text("Rutina")),
            DataColumn(Text("Progreso")),
            DataColumn(Text("Pesos")),
            DataColumn(Text("Foto")),
        ],
        rows=rows_table_clients()
    )


def show_full_datatable(root: Page):
    alert = AlertDialog(
        modal=True,
        adaptive=True,
        title=Text("Información General"),
        content=create_datatable_clients(),
        actions=[
            TextButton("Cerrar", on_click=lambda e: root.close(alert))
        ]
    )

    root.open(alert)
