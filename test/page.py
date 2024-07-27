import flet as ft


def main(page: ft.Page):
    page.title = "test"

    def change_view(view: ft.View):
        page.open(view)
        page.update()

    view1 = ft.View()
    view2 = ft.View()

    view1 = ft.View(controls=[
        ft.TextButton("Cambiar al 2", on_click=lambda e: change_view(view=view2))
    ])
    view2 = ft.View(controls=[
        ft.TextButton("Cambiar al 1", on_click=lambda e: change_view(view=view1))
    ])

    page.views.append(view1)

    page.update()


ft.app(target=main)
