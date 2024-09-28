import flet as ft

from Model.Dia import Dia
from View.AutoCompleteSuggestionData import auto_complete_suggestion_data
from View.ClienteViewFull import show_client_view
from View.EditData import create_client_view, create_routine_view, add_rutine
from View.InfoClienteView import show_full_datatable
from View.RutineView import routine_list_view


def main(page: ft.Page):
    page.title = "FiTargetTool"
    page.scroll = ft.ScrollMode.ALWAYS

    data_view = ft.Column()
    client_view = ft.Row(alignment=ft.MainAxisAlignment.CENTER)

    page.overlay.append(
        ft.SnackBar(
            ft.Text("Contenido guardado...")
        )
    )

    list_values_reps = []
    list_values_weights = []

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

    cant_tandas = ft.TextField(
        label="Cantidad de Tandas",
        tooltip="Diga la cantidad de tandas del ejercicio",
        value="0",
        input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-8]*$", replacement_string="0"),
        on_change=lambda e: on_change_tandas()
    )

    def on_change_tandas():
        try:
            if int(cant_tandas.value) > 0:
                print("perro")
                list_values_reps.clear()
                list_values_weights.clear()
                for e in range(0, int(cant_tandas.value)):
                    list_values_reps.append(ft.TextField(
                        label="Cantidad de Reps.",
                        tooltip="Diga la cantidad de reps del ejercicio",
                        value="0",
                        width=100,
                        input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-9999]*$", replacement_string="0")
                    ))
                    list_values_weights.append(ft.TextField(
                        label="Cantidad de Peso.",
                        tooltip="Diga la cantidad de peso del ejercicio",
                        value="0",
                        width=100,
                        input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-99999999]*$", replacement_string="0")
                    ))
        except ValueError as e:
            print(f"Excepcion asegurada ((ValueError)) --> {e}")
        page.go(page.route)

    def route_change(route):
        page.update()
        page.views.clear()

        troute = ft.TemplateRoute(page.route)

        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.Row([
                        ft.IconButton(
                            ft.icons.REFRESH,
                            tooltip="Actualiza los valores guardados",
                            on_click=lambda e: refresh_view()
                        ),
                        ft.TextButton(
                            "Crear Cliente",
                            on_click=lambda e: create_client_view(page)
                        ),
                        ft.TextButton(
                            "Crear Rutina",
                            on_click=lambda e: create_routine_view(page)
                        ),
                        ft.TextButton(
                            "Ver Clientes",
                            tooltip="Muestra una lista de todos los clientes",
                            on_click=lambda e: show_full_datatable(page)
                        ),
                        ft.TextButton(
                            "Ver Rutina",
                            tooltip="Muestra una lista de las Rutinas creadas",
                            on_click=lambda e: routine_list_view(page)
                        ),
                    ]),
                    data_view,
                    client_view
                ],
                adaptive=True, scroll=ft.ScrollMode.ALWAYS
            )
        )
        if troute.match("/routine/:id"):
            page.views.append(
                ft.View(
                    route="/routine",
                    controls=[
                        ft.Row([
                            ft.IconButton(ft.icons.ARROW_BACK, icon_size=25, on_click=lambda e: page.views.pop())
                        ]),
                        ft.Row([
                            ft.Column([
                                ft.Text("Wassaaaaaaa")
                            ]),
                            ft.Column([
                                new_ejercicio,
                                dia_control,
                                cant_tandas,
                                ft.Row(list_values_reps),
                                ft.Row(list_values_weights),
                                ft.FilledButton("Guardar", ft.icons.CREATE)
                            ])
                        ])
                    ]
                )
            )
        page.update()

    def view_change(data: ft.AutoCompleteSuggestion):
        client_view.controls.clear()
        client_view.controls.append(show_client_view(page, data))
        page.update()

    def refresh_view():
        client_view.controls.clear()
        input_search.suggestions = auto_complete_suggestion_data()
        page.update()

    input_search = ft.AutoComplete(
        suggestions=auto_complete_suggestion_data(),
        on_select=lambda e: view_change(e.selection),
    )

    data_view.controls = [
        ft.Row(
            [
                ft.Column([
                    ft.Text("Nombre de Cliente: ", size=22, weight=ft.FontWeight.BOLD),
                    ft.Container(
                        content=input_search,
                        bgcolor=ft.colors.BLUE_GREY,
                        width=400,
                        padding=10,
                        border_radius=20
                    )
                ])

            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    ]

    def view_pop(view):
        page.views.pop()
        page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.update()


ft.app(main)
