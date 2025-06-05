import flet as ft

from Controler.Update import update_progress
from Model.Progreso import Progreso
from Components.AlertPanel import alert_invalid_data


def add_progress(root: ft.Page, progress_id: int):
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
            update_progress(progress_id, list_progress)
        except ValueError:
            root.open(alert_invalid_data(root))

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Agregar progreso"),
        content=ft.Container(
            ft.Row(list_textfield, wrap=True),
            width=900
        ),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Agregar", on_click=lambda e: validate())
        ]

    )

    root.open(alert)


def create_linechartdata_points(datas: list[int]) -> list[ft.LineChartDataPoint]:
    group_points = list()
    i = 0

    for data in datas:
        group_points.append(ft.LineChartDataPoint(i, data))
        i = i + 1

    return group_points


def create_left_chart_axis(datas: list[int]) -> list[ft.ChartAxisLabel]:
    chart_axis = []

    for data in datas:
        chart_axis.append(
            ft.ChartAxisLabel(
                value=data,
                label=ft.Text(f"{data}", size=14, weight=ft.FontWeight.BOLD),
            )
        )

    return chart_axis


def create_bottom_chart_axis(datas: list[int]) -> list[ft.ChartAxisLabel]:
    chart_axis = list()

    for i in range(0, len(datas)):
        chart_axis.append(
            ft.ChartAxisLabel(
                value=i,
                label=ft.Text(f"{i}", size=14, weight=ft.FontWeight.BOLD),
            )
        )

    return chart_axis


def show_graphic(datas: list) -> ft.LineChart:
    group_line_points = [
        ft.LineChartData(
            data_points=create_linechartdata_points(datas),
            stroke_width=8,
            color=ft.colors.LIGHT_BLUE,
            curved=True,
            stroke_cap_round=True,
        )
    ]

    return ft.LineChart(
        data_series=group_line_points,
        border=ft.Border(
            bottom=ft.BorderSide(4, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE))
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        vertical_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        left_axis=ft.ChartAxis(
            labels=create_left_chart_axis(datas),
            labels_size=32,
        ),
        bottom_axis=ft.ChartAxis(
            labels=create_bottom_chart_axis(datas),
            labels_size=32,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        expand=True,
    )


def open_graphic(root: ft.Page, datas: list[int], text: str):
    graphic_alert = ft.AlertDialog(
        title=ft.Text(text),
        modal=True,
        content=ft.Container(
            show_graphic(datas),
            width=800,
            padding=20
        ),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(graphic_alert))
        ]
    )

    root.open(graphic_alert)


def collection_graphics_view(root: ft.Page, progress: Progreso) -> ft.Column:
    return ft.Column([
        ft.Row([
            ft.Container(
                content=ft.Text("Progresos Registrados", size=22),
                padding=10
            ),
            ft.TextButton("Agregar Progreso", on_click=lambda e: add_progress(root, progress.id))
        ]),
        ft.Row([
            ft.FilledButton("Pecho", on_click=lambda e: open_graphic(root, progress.pecho, "Progreso de Pecho")),
            ft.FilledButton("Trapecios", on_click=lambda e: open_graphic(root, progress.trapecio, "Progreso de Trapecios")),
            ft.FilledButton("Romboides", on_click=lambda e: open_graphic(root, progress.romboides, "Progreso de Romboides")),
            ft.FilledButton("Dorsal", on_click=lambda e: open_graphic(root, progress.dorsal, "Progreso de Dorsal")),
            ft.FilledButton("Espalda Baja", on_click=lambda e: open_graphic(root, progress.espalda_baja, "Progreso de Espalda Baja")),
            ft.FilledButton("Biceps", on_click=lambda e: open_graphic(root, progress.biceps, "Progreso de Biceps")),
            ft.FilledButton("Triceps", on_click=lambda e: open_graphic(root, progress.triceps, "Progreso de Triceps")),
            ft.FilledButton("AnteBrazo", on_click=lambda e: open_graphic(root, progress.ante_brazo, "Progreso de AnteBrazo")),
            ft.FilledButton("Deltoide Posterior", on_click=lambda e: open_graphic(root, progress.deltoide_posterior, "Progreso de Deltoide Posterior")),
            ft.FilledButton("Deltoide Lateral", on_click=lambda e: open_graphic(root, progress.deltoide_lateral, "Progreso de Pecho")),
            ft.FilledButton("Deltoide Anterior", on_click=lambda e: open_graphic(root, progress.deltoide_anterior, "Progreso de Pecho")),
            ft.FilledButton("Cuádriceps", on_click=lambda e: open_graphic(root, progress.cuadriceps, "Progreso de Pecho")),
            ft.FilledButton("Isquiotibiales", on_click=lambda e: open_graphic(root, progress.isquiotibiales, "Progreso de Pecho")),
            ft.FilledButton("Glúteos", on_click=lambda e: open_graphic(root, progress.gluteos, "Progreso de Pecho")),
            ft.FilledButton("Pantorrillas", on_click=lambda e: open_graphic(root, progress.pantorrillas, "Progreso de Pecho"))
        ], wrap=True)
    ])
