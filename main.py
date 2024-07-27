import flet as ft

from View.AutoCompleteSuggestionData import auto_complete_suggestion_data
from View.ClienteViewFull import show_client_view
from View.EditData import create_client_view, list_edit_clients
from View.change_view import change_view


def main(page: ft.Page):
    page.title = "FiTargetTool"
    page.scroll = ft.ScrollMode.ALWAYS

    main_view = ft.View()
    edit_view = ft.View()

    data_view = ft.Column()
    client_view = ft.Row(alignment=ft.MainAxisAlignment.CENTER)

    main_view = ft.View(
        controls=[
            ft.TextButton("Editar Datos", on_click=lambda e: change_view(page, edit_view)),
            data_view,
            client_view
        ],
        adaptive=True, scroll=ft.ScrollMode.ALWAYS
    )

    edit_view = ft.View(
        controls=[
            ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda e: change_view(page, main_view)),
            ft.Row(
                controls=[
                    ft.Text("Crear Nuevo: ", size=24),
                    ft.TextButton("Cliente", on_click=lambda e: create_client_view(page)),
                    ft.TextButton("Rutina")
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            list_edit_clients()
        ],
        adaptive=True, scroll=ft.ScrollMode.ALWAYS
    )

    def view_change(data: ft.AutoCompleteSuggestion):
        client_view.controls.clear()
        client_view.controls.append(show_client_view(page, data))
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

    page.views.append(main_view)

    page.update()


ft.app(main)
