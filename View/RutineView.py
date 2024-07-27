from flet import Row, Text, ListView, MainAxisAlignment, FontWeight
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
        controls=routine_data(rutine),
        alignment=MainAxisAlignment.CENTER,
        width=200,
    )
