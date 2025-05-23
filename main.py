import flet as ft

from View.AutoCompleteSuggestionData import auto_complete_suggestion_data
from View.ClienteViewFull import show_client_view
from View.EditData import create_client_view, create_routine_view
from View.InfoClienteView import show_full_datatable
from View.RoutineRouteUpdateView import RoutineRouteUpdateView
from View.RutineView import routine_list_view
from View.RoutineRouteView import RoutineRouteView


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

    def route_change(route):
        page.views.clear()
        page.update()

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
            page.views.append(RoutineRouteView(page, troute.id).show_view())
        if troute.match("/routine_update/:id"):
            page.views.append(RoutineRouteUpdateView(page, troute.id).show_view())

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
        page.views.clear()
        page.go("/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.update()


ft.app(main)
