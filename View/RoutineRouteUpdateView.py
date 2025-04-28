import flet as ft

from Controler.Controler import get_rutine
from Controler.Update import update_routine_full_day
from Model.Ejercicios import Ejercicios
from Model.Dia import Dia

class RoutineRouteUpdateView:
    def __init__(self, page: ft.Page, ident):
        self.page = page
        self.rutina = get_rutine(ident)
        self.dia_control = ft.Dropdown(
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
            on_change= lambda e: self.create_checklist()
        )
        self.deleted_exercises_list: list[Ejercicios] = []
        self.exercises_list: list[Ejercicios] = []

        self.checklist_options: list[ft.Checkbox] = []
        self.checklist_options_view = ft.Column()

    def show_view(self):
        return ft.View(
            route="/routine_update",
            controls=[
                ft.Row([
                    ft.IconButton(ft.icons.ARROW_BACK, icon_size=25, on_click=lambda e: self.page.go("/"))
                ]),
                ft.Row([
                    self.dia_control,
                    self.checklist_options_view,
                    ft.FilledButton("Guardar", ft.icons.CREATE, on_click=lambda e: self.save_changes())
                ])
            ]
        )

    def create_checklist(self):
        self.checklist_options.clear()
        self.checklist_options_view.controls.clear()

        if self.dia_control.value == Dia.LUNES.value:
            self.exercises_list = self.rutina.lunes
        elif self.dia_control.value == Dia.MARTES.value:
            self.exercises_list = self.rutina.martes
        elif self.dia_control.value == Dia.MIERCOLES.value:
            self.exercises_list = self.rutina.miercoles
        elif self.dia_control.value == Dia.JUEVES.value:
            self.exercises_list = self.rutina.jueves
        elif self.dia_control.value == Dia.VIERNES.value:
            self.exercises_list = self.rutina.viernes
        elif self.dia_control.value == Dia.SABADO.value:
            self.exercises_list = self.rutina.sabado
        elif self.dia_control.value == Dia.DOMINGO.value:
            self.exercises_list = self.rutina.domingo

        for exercise in self.exercises_list:
            self.checklist_options.append(ft.Checkbox(exercise.name[0]))

        self.checklist_options_view.controls = self.checklist_options

        self.page.update()

    def save_changes(self):
        list_ejercices_save: list[Ejercicios] = self.exercises_list

        for ejercice in list_ejercices_save:
            for ejercice_for_delete in self.checklist_options:
                if ejercice_for_delete.value:
                    self.exercises_list.remove(ejercice)
                break

        update_routine_full_day(self.rutina.id, self.dia_control.value, list_ejercices_save)

        self.page.update()
