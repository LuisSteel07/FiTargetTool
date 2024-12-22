from flet import TextButton, AlertDialog, Row, Text, ListView, MainAxisAlignment, FontWeight, Page, DataTable, \
    DataColumn, DataRow, DataCell, CrossAxisAlignment, ElevatedButton

from Controler.Controler import get_list_id_rutines, get_rutine
from Model.Ejercicios import Ejercicios
from Model.Rutina import Rutina


class PanelExercise:
    def __init__(self, ejercicio: Ejercicios, root: Page):
        self.ejercicio = ejercicio
        self.button = ElevatedButton(ejercicio.name[0], on_click=lambda e: self.on_click(root))

    def data_list_columns(self) -> DataTable:
        data_columns = [
            DataColumn(Text("Tanda")),
            DataColumn(Text("Reps")),
            DataColumn(Text("Pesos(lb)"))
        ]
        data_rows = []

        tanda = 0
        for e in range(0, len(self.ejercicio.reps[0])):
            cells = [
                DataCell(Text(f"{tanda + 1}")),
                DataCell(Text(self.ejercicio.reps[0][tanda])),
                DataCell(Text(str(self.ejercicio.weights[tanda]))),
            ]

            data_rows.append(DataRow(cells))
            tanda = tanda + 1

        return DataTable(
            data_columns,
            data_rows
        )

    def on_click(self, root: Page):
        alert = AlertDialog(
            modal=True,
            adaptive=True,
            content=self.data_list_columns(),
            actions=[TextButton("Cerrar", on_click=lambda e: root.close(alert))],
        )

        root.open(alert)


class RowActionRoutine:
    def __init__(self, num, name):
        self.num = num,
        self.name = name,

    def get_datarow(self):
        return DataRow([
            DataCell(Text(f"{self.num[0]}")),
            DataCell(Text(self.name[0])),
        ])


def routine_data(rutine: Rutina, root: Page) -> list[ListView]:
    data_cols = [
        ListView([Text("Lunes", size=22, weight=FontWeight.BOLD)], width=120, spacing=10),
        ListView([Text("Martes", size=22, weight=FontWeight.BOLD)], width=120, spacing=10),
        ListView([Text("Miercoles", size=22, weight=FontWeight.BOLD)], width=120, spacing=10),
        ListView([Text("Jueves", size=22, weight=FontWeight.BOLD)], width=120, spacing=10),
        ListView([Text("Viernes", size=22, weight=FontWeight.BOLD)], width=120, spacing=10),
        ListView([Text("Sabado", size=22, weight=FontWeight.BOLD)], width=120, spacing=10),
        ListView([Text("Domingo", size=22, weight=FontWeight.BOLD)], width=120, spacing=10),
    ]

    for i in range(0, len(data_cols)):
        if i == 0:
            for e in rutine.lunes:
                data_cols[i].controls.append(PanelExercise(e, root).button)
        if i == 1:
            for e in rutine.martes:
                data_cols[i].controls.append(PanelExercise(e, root).button)
        if i == 2:
            for e in rutine.miercoles:
                data_cols[i].controls.append(PanelExercise(e, root).button)
        if i == 3:
            for e in rutine.jueves:
                data_cols[i].controls.append(PanelExercise(e, root).button)
        if i == 4:
            for e in rutine.viernes:
                data_cols[i].controls.append(PanelExercise(e, root).button)
        if i == 5:
            for e in rutine.sabado:
                data_cols[i].controls.append(PanelExercise(e, root).button)
        if i == 6:
            for e in rutine.domingo:
                data_cols[i].controls.append(PanelExercise(e, root).button)

    return data_cols


def routine_view(rutine: Rutina, root: Page) -> Row:
    return Row(
        routine_data(rutine, root),
        alignment=MainAxisAlignment.CENTER,
        vertical_alignment=CrossAxisAlignment.START,
        width=950,
    )


def get_rows_table_view() -> list[DataRow]:
    rutines_id = get_list_id_rutines()
    table_rows: list[DataRow] = []
    rutines: list[Rutina] = []

    for i in rutines_id:
        rutines.append(get_rutine(i))

    for rutine in rutines:
        table_rows.append(RowActionRoutine(rutine.id, rutine.nombre).get_datarow())

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
