import flet as ft

from Views.ClientView import ClientView
from Views.RoutineEdit import RoutineEdit
from Views.RoutineDelete import RoutineDelete
from Views.RoutineAdd import RoutineAdd
from Views.PrincipalView import PrincipalView
from Views.RoutineOrder import RoutineOrder
from Views.RoutineUpdate import RoutineUpdate
from Views.RoutineView import RoutineView


def main(page: ft.Page):
    page.title = "FiTargetTool"
    page.scroll = ft.ScrollMode.ALWAYS

    def route_change(route):
        page.views.clear()
        page.update()

        troute = ft.TemplateRoute(page.route)

        page.views.append(PrincipalView(page))

        if troute.match("/client/:name"):
            page.views.append(ClientView(page, troute.name))
        if troute.match("/routines"):
            page.views.append(RoutineView(page))
        if troute.match("/routine/:id"):
            page.views.append(RoutineUpdate(page, troute.id))
        if troute.match("/routine/add/:id"):
            page.views.append(RoutineAdd(page, troute.id))
        if troute.match("/routine/update/:id"):
            page.views.append(RoutineEdit(page, troute.id))
        if troute.match("/routine/delete/:id"):
            page.views.append(RoutineDelete(page, troute.id))
        if troute.match("/routine/order/:id"):
            page.views.append(RoutineOrder(page, troute.id))

        page.update()

    def view_pop(view):
        page.views.clear()
        page.go("/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.update()


ft.app(main)
