from flet import (TextButton, Container, ChartGridLines, Page, Row, Text, FilledButton, Column, AlertDialog, LineChart,
                  LineChartDataPoint, LineChartData, colors, Border, BorderSide, ChartAxis, FontWeight, ChartAxisLabel)

from Model.Progreso import Progreso
from View.EditData import add_progreso


def create_linechartdata_points(datas: list[int]) -> list[LineChartDataPoint]:
    group_points = list()
    i = 0

    for data in datas:
        group_points.append(LineChartDataPoint(i, data))
        i = i + 1

    return group_points


def create_left_chart_axis(datas: list[int]) -> list[ChartAxisLabel]:
    chart_axis = []

    for data in datas:
        chart_axis.append(
            ChartAxisLabel(
                value=data,
                label=Text(f"{data}", size=14, weight=FontWeight.BOLD),
            )
        )

    return chart_axis


def create_bottom_chart_axis(datas: list[int]) -> list[ChartAxisLabel]:
    chart_axis = list()

    for i in range(0, len(datas)):
        chart_axis.append(
            ChartAxisLabel(
                value=i,
                label=Text(f"{i}", size=14, weight=FontWeight.BOLD),
            )
        )

    return chart_axis


def show_graphic(datas: list) -> LineChart:
    group_line_points = [
        LineChartData(
            data_points=create_linechartdata_points(datas),
            stroke_width=8,
            color=colors.LIGHT_BLUE,
            curved=True,
            stroke_cap_round=True,
        )
    ]

    return LineChart(
        data_series=group_line_points,
        border=Border(
            bottom=BorderSide(4, colors.with_opacity(0.5, colors.ON_SURFACE))
        ),
        horizontal_grid_lines=ChartGridLines(
            interval=1, color=colors.with_opacity(0.2, colors.ON_SURFACE), width=1
        ),
        vertical_grid_lines=ChartGridLines(
            interval=1, color=colors.with_opacity(0.2, colors.ON_SURFACE), width=1
        ),
        left_axis=ChartAxis(
            labels=create_left_chart_axis(datas),
            labels_size=32,
        ),
        bottom_axis=ChartAxis(
            labels=create_bottom_chart_axis(datas),
            labels_size=32,
        ),
        tooltip_bgcolor=colors.with_opacity(0.8, colors.BLUE_GREY),
        expand=True,
    )


def open_graphic(root: Page, datas: list[int], text: str):
    graphic_alert = AlertDialog(
        title=Text(text),
        modal=True,
        content=Container(
            show_graphic(datas),
            width=800,
            padding=20
        ),
        actions=[
            TextButton("Cerrar", on_click=lambda e: root.close(graphic_alert))
        ]
    )

    root.open(graphic_alert)


def collection_graphics_view(root: Page, progress: Progreso) -> Column:
    return Column([
        Row([
            Container(
                content=Text("Progresos Registrados", size=22),
                padding=10
            ),
            TextButton("Agregar Progreso", on_click=lambda e: add_progreso(root, progress.id))
        ]),
        Row([
            FilledButton("Pecho", on_click=lambda e: open_graphic(root, progress.pecho, "Progreso de Pecho")),
            FilledButton("Trapecios", on_click=lambda e: open_graphic(root, progress.trapecio, "Progreso de Trapecios")),
            FilledButton("Romboides", on_click=lambda e: open_graphic(root, progress.romboides, "Progreso de Romboides")),
            FilledButton("Dorsal", on_click=lambda e: open_graphic(root, progress.dorsal, "Progreso de Dorsal")),
            FilledButton("Espalda Baja", on_click=lambda e: open_graphic(root, progress.espalda_baja, "Progreso de Espalda Baja")),
            FilledButton("Biceps", on_click=lambda e: open_graphic(root, progress.biceps, "Progreso de Biceps")),
            FilledButton("Triceps", on_click=lambda e: open_graphic(root, progress.triceps, "Progreso de Triceps")),
            FilledButton("AnteBrazo", on_click=lambda e: open_graphic(root, progress.ante_brazo, "Progreso de AnteBrazo")),
            FilledButton("Deltoide Posterior", on_click=lambda e: open_graphic(root, progress.deltoide_posterior, "Progreso de Deltoide Posterior")),
            FilledButton("Deltoide Lateral", on_click=lambda e: open_graphic(root, progress.deltoide_lateral, "Progreso de Pecho")),
            FilledButton("Deltoide Anterior", on_click=lambda e: open_graphic(root, progress.deltoide_anterior, "Progreso de Pecho")),
            FilledButton("Cuádriceps", on_click=lambda e: open_graphic(root, progress.cuadriceps, "Progreso de Pecho")),
            FilledButton("Isquiotibiales", on_click=lambda e: open_graphic(root, progress.isquiotibiales, "Progreso de Pecho")),
            FilledButton("Glúteos", on_click=lambda e: open_graphic(root, progress.gluteos, "Progreso de Pecho")),
            FilledButton("Pantorrillas", on_click=lambda e: open_graphic(root, progress.pantorrillas, "Progreso de Pecho"))
        ], wrap=True)
    ])
