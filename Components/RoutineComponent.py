import flet as ft

from Model.Ejercicios import Ejercicios
from Model.Rutina import Rutina


class PanelExercise:
    def __init__(self, exercise: Ejercicios, root: ft.Page):
        self.exercise = exercise
        self.button = ft.ElevatedButton(exercise.name[0], on_click=lambda e: self.on_click(root))

    def data_list_columns(self) -> ft.DataTable:
        data_columns = [
            ft.DataColumn(ft.Text("Tanda")),
            ft.DataColumn(ft.Text("Reps")),
            ft.DataColumn(ft.Text("Pesos(lb)"))
        ]
        data_rows = []

        tanda = 0
        for e in range(0, len(self.exercise.reps[0])):
            cells = [
                ft.DataCell(ft.Text(f"{tanda + 1}")),
                ft.DataCell(ft.Text(self.exercise.reps[0][tanda])),
                ft.DataCell(ft.Text(str(self.exercise.weights[tanda]))),
            ]

            data_rows.append(ft.DataRow(cells))
            tanda = tanda + 1

        return ft.DataTable(
            data_columns,
            data_rows
        )

    def on_click(self, root: ft.Page):
        alert = ft.AlertDialog(
            modal=True,
            adaptive=True,
            content=self.data_list_columns(),
            actions=[ft.TextButton("Cerrar", on_click=lambda e: root.close(alert))],
        )

        root.open(alert)


def create_list_routine_day(exercises: list[Ejercicios], root: ft.Page) -> list[ft.ElevatedButton]:
    list_panel_exercises: list[ft.ElevatedButton] = []

    for e in exercises:
        list_panel_exercises.append(PanelExercise(e, root).button)

    return list_panel_exercises


def routine_data(routine: Rutina, root: ft.Page) -> list[ft.ListView]:
    data_cols = [
        ft.ListView([ft.Text("Lunes", size=22, weight=ft.FontWeight.BOLD)], width=120, spacing=10),
        ft.ListView([ft.Text("Martes", size=22, weight=ft.FontWeight.BOLD)], width=120, spacing=10),
        ft.ListView([ft.Text("Miercoles", size=22, weight=ft.FontWeight.BOLD)], width=120, spacing=10),
        ft.ListView([ft.Text("Jueves", size=22, weight=ft.FontWeight.BOLD)], width=120, spacing=10),
        ft.ListView([ft.Text("Viernes", size=22, weight=ft.FontWeight.BOLD)], width=120, spacing=10),
        ft.ListView([ft.Text("Sabado", size=22, weight=ft.FontWeight.BOLD)], width=120, spacing=10),
        ft.ListView([ft.Text("Domingo", size=22, weight=ft.FontWeight.BOLD)], width=120, spacing=10),
    ]

    routines_days = [
        routine.lunes,
        routine.martes,
        routine.miercoles,
        routine.jueves,
        routine.viernes,
        routine.sabado,
        routine.domingo,
    ]

    for i in range(len(data_cols)):
        data_cols[i].controls += create_list_routine_day(routines_days[i], root)

    return data_cols


def routine_view(routine: Rutina, root: ft.Page) -> ft.Row:
    return ft.Row(
        routine_data(routine, root),
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
        width=950,
    )

