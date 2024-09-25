import flet as ft
from Controler.Controler import get_all_data, get_list_id_rutines
from Controler.Create import create_client, create_routine
from Controler.Delete import delete_client
from Controler.Update import update_peso, update_progress, update_rutina, change_rutine, update_client_data, \
    update_full_routine
from Model.Cliente import Cliente
from Model.Rutina import Rutina
from Model.Dia import Dia


def alert_invalid_data(root: ft.Page) -> ft.AlertDialog:
    alert = ft.AlertDialog(
        modal=True,
        title=ft.Text("Error"),
        content=ft.Text("Valores Invalidados"),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert))
        ]
    )

    return alert


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

    return table_clients


def create_client_view(root: ft.Page):
    nombre = ft.TextField(tooltip="Nombre del Cliente", label="Nombre: ")
    edad = ft.TextField(tooltip="Edad del Cliente", label="Edad: ")
    peso = ft.TextField(tooltip="Peso del Cliente (lb)", label="Peso: ")
    rutina = ft.TextField(tooltip="ID Rutina", label="Rutina: ")
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

    def validate():
        root.close(alert)
        if pecho.value == "" or trapecio.value == "" or romboides.value == "" or dorsal.value == "" or espalda_baja.value == "" or biceps.value == "" or triceps.value == "" or ante_brazo.value == "" or del_posterior.value == "" or del_lateral.value == "" or del_anterior.value == "" or cuadriceps.value == "" or isq.value == "" or gluteos.value == "" or pantorrillas.value == "" or pecho.value == " " or trapecio.value == " " or romboides.value == " " or dorsal.value == " " or espalda_baja.value == " " or biceps.value == " " or triceps.value == " " or ante_brazo.value == " " or del_posterior.value == " " or del_lateral.value == " " or del_anterior.value == " " or cuadriceps.value == " " or isq.value == " " or gluteos.value == " " or pantorrillas.value == " " or nombre.value == "" or nombre.value == " " or edad.value == "" or edad.value == " " or peso.value == "" or peso.value == " " or rutina.value == "" or rutina.value == " " or foto.value == "" or foto.value == " ":
            alert_invalid_data(root)
        else:
            create_client(nombre.value, int(edad.value), int(peso.value),
                          int(rutina.value), foto.value,
                          [int(pecho.value), int(trapecio.value),
                           int(romboides.value),
                           int(dorsal.value), int(espalda_baja.value),
                           int(biceps.value),
                           int(triceps.value), int(ante_brazo.value),
                           int(del_posterior.value), int(del_lateral.value),
                           int(del_anterior.value), int(cuadriceps.value),
                           int(isq.value),
                           int(gluteos.value), int(pantorrillas.value), ])

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Creando Cliente: "),
        content=ft.Column([
            ft.Row([nombre, edad]),
            ft.Row([rutina, peso]), foto,
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
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Crear", on_click=lambda e: validate())
        ]
    )

    root.open(alert)


def add_peso(root: ft.Page, peso_id: int):
    peso = ft.TextField(label="Agrega Peso")

    def validate():
        root.close(alert)
        if peso.value == "" or peso.value == " " or not peso.value.isdigit():
            alert_invalid_data(root)
        else:
            update_peso(peso_id, int(peso.value))

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Agregando Peso: "),
        content=peso,
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Agregar", on_click=lambda e: validate())
        ]
    )

    root.open(alert)


def add_progreso(root: ft.Page, progress_id: int):
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

    def validate():
        root.close(alert)
        if pecho.value == "" or trapecio.value == "" or romboides.value == "" or dorsal.value == "" or espalda_baja.value == "" or biceps.value == "" or triceps.value == "" or ante_brazo.value == "" or del_posterior.value == "" or del_lateral.value == "" or del_anterior.value == "" or cuadriceps.value == "" or isq.value == "" or gluteos.value == "" or pantorrillas.value == "" or pecho.value == " " or trapecio.value == " " or romboides.value == " " or dorsal.value == " " or espalda_baja.value == " " or biceps.value == " " or triceps.value == " " or ante_brazo.value == " " or del_posterior.value == " " or del_lateral.value == " " or del_anterior.value == " " or cuadriceps.value == " " or isq.value == " " or gluteos.value == " " or pantorrillas.value == " ":
            alert_invalid_data(root)
        else:
            update_progress(progress_id, [
                int(pecho.value),
                int(trapecio.value),
                int(romboides.value),
                int(dorsal.value),
                int(espalda_baja.value),
                int(biceps.value),
                int(triceps.value),
                int(ante_brazo.value),
                int(del_posterior.value),
                int(del_lateral.value),
                int(del_anterior.value),
                int(cuadriceps.value),
                int(isq.value),
                int(gluteos.value),
                int(pantorrillas.value),
            ])

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Agregar progreso"),
        content=ft.Container(
            ft.Column([
                ft.Row([pecho, trapecio, romboides]),
                ft.Row([dorsal, espalda_baja, biceps]),
                ft.Row([triceps, ante_brazo, del_posterior]),
                ft.Row([del_lateral, del_anterior, cuadriceps]),
                ft.Row([isq, gluteos, pantorrillas]),
            ]),
            width=900
        ),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Agregar", on_click=lambda e: validate())
        ]

    )

    root.open(alert)


def add_rutine(root: ft.Page, routine_id: int):
    root.snack_bar = ft.SnackBar(
        ft.Text("Contenido guardado...")
    )

    dia_control = ft.Dropdown(
        options=[
            ft.dropdown.Option(Dia.LUNES.value),
            ft.dropdown.Option(Dia.MARTES.value),
            ft.dropdown.Option(Dia.MIERCOLES.value),
            ft.dropdown.Option(Dia.JUEVES.value),
            ft.dropdown.Option(Dia.VIERNES.value),
            ft.dropdown.Option(Dia.SABADO.value),
            ft.dropdown.Option(Dia.DOMINGO.value),
        ],
        width=140,

    )
    new_ejercicio = ft.TextField(label="Nuevo Ejercicio", tooltip="Diga el nuevo ejercicio a agregar")

    def validate():
        if new_ejercicio.value == "" or new_ejercicio.value == " " or dia_control.value is None:
            root.close(alert)
            root.open(alert_invalid_data(root))
        else:
            update_rutina(routine_id, dia_control.value, new_ejercicio.value)
            root.snack_bar.open = True
            root.update()

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Agregando Ejercicio"),
        content=ft.Column([
            new_ejercicio,
            dia_control
        ]),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Agregar", on_click=lambda e: validate())
        ]
    )

    root.open(alert)
    root.update()


def create_routine_view(root: ft.Page):
    name = ft.TextField(label="Nombre de la Rutina")

    def validate():
        root.close(alert)
        if name.value == "" or name.value == " ":
            alert_invalid_data(root)
        else:
            create_routine(name.value)

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Creando Rutina"),
        content=name,
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Agregar", on_click=lambda e: validate())
        ]
    )

    root.open(alert)


def change_rutine_view(root: ft.Page, client_id: int):
    rutine = ft.Dropdown()

    for identifier in get_list_id_rutines():
        rutine.options.append(ft.dropdown.Option(str(identifier)))

    def validate():
        root.close(alert)
        if rutine.value is None:
            alert_invalid_data(root)
        else:
            change_rutine(int(rutine.value), client_id)

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Cambiando Rutina"),
        content=rutine,
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Cambiar", on_click=lambda e: validate()),
        ]
    )

    root.open(alert)


def change_client_view(root: ft.Page, client_id: int):
    name = ft.TextField(label="Nuevo Nombre", tooltip="Nombre")
    age = ft.TextField(label="Nuevo Edad", tooltip="Edad")

    def validacion():
        root.close(alert)
        if name.value == "" or name.value == " " or age.value == "" or age.value == " " or not age.value.isdigit():
            alert_invalid_data(root)
        else:
            update_client_data(client_id, name.value, int(age.value))

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Actualizando Cliente"),
        content=ft.Column([
            name,
            age
        ]),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Actualizar", on_click=lambda e: validacion())
        ]
    )

    root.open(alert)


def list_textfields_rutine(list_exercises, dia: str) -> list:
    list_textfields = [ft.Text(value=dia, size=18, color=ft.colors.BLUE)]

    if len(list_exercises) == 0:
        list_textfields.append(ft.Text("Vacío", size=18, color=ft.colors.RED))
    else:
        for ejer in list_exercises:
            list_textfields.append(ft.TextField(value=ejer, width=120))

    return list_textfields


def extract_routine_values(list_textfield: list[list[ft.TextField]], routine_id: int) -> Rutina:
    routine: Rutina = Rutina(routine_id, "", [], [], [], [], [], [], [])
    for day in range(0, 6):
        for ejers in list_textfield[day]:
            if ejers.value == "Vacío" or ejers.value == "" or ejers.value == " " or ejers.value == "Lunes" or ejers.value == "Martes" or ejers.value == "Miércoles" or ejers.value == "Jueves" or ejers.value == "Viernes" or ejers.value == "Sábado" or ejers.value == "Domingo":
                continue
            elif day == 0:
                routine.lunes.append(ejers.value)
            elif day == 1:
                routine.martes.append(ejers.value)
            elif day == 2:
                routine.miercoles.append(ejers.value)
            elif day == 3:
                routine.jueves.append(ejers.value)
            elif day == 4:
                routine.viernes.append(ejers.value)
            elif day == 5:
                routine.sabado.append(ejers.value)
            elif day == 6:
                routine.domingo.append(ejers.value)

    return routine


def modify_rutine(root: ft.Page, rutine: Rutina, routine_id: int):
    list_lunes = list_textfields_rutine(rutine.lunes, "Lunes")
    list_martes: list[ft.TextField] = list_textfields_rutine(rutine.martes, "Martes")
    list_miercoles: list[ft.TextField] = list_textfields_rutine(rutine.miercoles, "Miércoles")
    list_jueves: list[ft.TextField] = list_textfields_rutine(rutine.jueves, "Jueves")
    list_viernes: list[ft.TextField] = list_textfields_rutine(rutine.viernes, "Viernes")
    list_sabado: list[ft.TextField] = list_textfields_rutine(rutine.sabado, "Sábado")
    list_domingo: list[ft.TextField] = list_textfields_rutine(rutine.domingo, "Domingo")

    content = ft.Container(
        content=ft.Row([
            ft.Column(list_lunes, width=130),
            ft.Column(list_martes, width=130),
            ft.Column(list_miercoles, width=130),
            ft.Column(list_jueves, width=130),
            ft.Column(list_viernes, width=130),
            ft.Column(list_sabado, width=130),
            ft.Column(list_domingo, width=130),
        ]),
        width=1000,
        height=800
    )

    def validacion():
        routine = extract_routine_values([list_lunes, list_martes, list_miercoles, list_jueves, list_viernes, list_sabado, list_domingo], routine_id)
        update_full_routine(routine_id, routine)
        root.close(alert)

    alert = ft.AlertDialog(
        modal=True,
        adaptive=True,
        title=ft.Text("Modificando Rutina Actual"),
        content=content,
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert)),
            ft.TextButton("Guardar", on_click=lambda e: validacion()),
        ]
    )

    root.open(alert)
