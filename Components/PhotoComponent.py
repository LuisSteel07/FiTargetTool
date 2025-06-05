import flet as ft


class PhotoComponent(ft.View):
    def __init__(self, root: ft.Page):
        super().__init__()
        self.root = root
        self.photo_path = ft.FilePicker(on_result=self.set_photo)
        self.root.overlay.append(self.photo_path)
        self.photo_selector = ft.FilledButton("Buscar Foto", on_click=lambda _: self.photo_path.pick_files())
        self.path_text = ft.Text(value="")

    def set_photo(self, file: ft.FilePickerResultEvent):
        self.path_text.value = file.files[0].path
        self.root.update()

    def show(self) -> ft.Row:
        return ft.Row([
            self.photo_selector,
            self.path_text
        ])

