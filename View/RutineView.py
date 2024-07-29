from flet import TextButton, AlertDialog, Row, Text, ListView, MainAxisAlignment, FontWeight, Page, DataTable, \
    DataColumn, DataRow, DataCell

from Controler.Controler import get_list_id_rutines, get_rutine
from Model.Rutina import Rutina


def routine_data(rutine: Rutina) -> list[ListView]:
    data_cols = [
        ListView([Text("Lunes", size=22, weight=FontWeight.BOLD)], width=120),
        ListView([Text("Martes", size=22, weight=FontWeight.BOLD)], width=120),
        ListView([Text("Miercoles", size=22, weight=FontWeight.BOLD)], width=120),
        ListView([Text("Jueves", size=22, weight=FontWeight.BOLD)], width=120),
        ListView([Text("Viernes", size=22, weight=FontWeight.BOLD)], width=120),
        ListView([Text("Sabado", size=22, weight=FontWeight.BOLD)], width=120),
        ListView([Text("Domingo", size=22, weight=FontWeight.BOLD)], width=120),
    ]

    for i in range(0, len(data_cols)):
        if i == 0:
            for e in rutine.lunes:
                data_cols[i].controls.append(Text(e))
        if i == 1:
            for e in rutine.martes:
                data_cols[i].controls.append(Text(e))
        if i == 2:
            for e in rutine.miercoles:
                data_cols[i].controls.append(Text(e))
        if i == 3:
            for e in rutine.jueves:
                data_cols[i].controls.append(Text(e))
        if i == 4:
            for e in rutine.viernes:
                data_cols[i].controls.append(Text(e))
        if i == 5:
            for e in rutine.sabado:
                data_cols[i].controls.append(Text(e))
        if i == 6:
            for e in rutine.domingo:
                data_cols[i].controls.append(Text(e))

    return data_cols


def routine_view(rutine: Rutina) -> Row:
    return Row(
        routine_data(rutine),
        alignment=MainAxisAlignment.CENTER,
        width=200,
    )


def get_rows_table_view() -> list[DataRow]:
    rutines_id = get_list_id_rutines()
    table_rows: list[DataRow] = []
    rutines: list[Rutina] = []

    for i in rutines_id:
        rutines.append(get_rutine(i))

    for rutine in rutines:
        table_rows.append(DataRow([
            DataCell(Text(f"{rutine.id}")),
            DataCell(Text(f"{rutine.nombre}")),
        ]))

    return table_rows


def routine_list_view(page: Page):
    table = DataTable(
        columns=[
            DataColumn(Text("ID")),
            DataColumn(Text("Nombre")),
        ],
        rows=get_rows_table_view()
    )

    alert = AlertDialog(
        modal=True,
        adaptive=True,
        content=table,
        actions=[TextButton("Cerrar", on_click=lambda e: page.close(alert))]
    )

    page.open(alert)
