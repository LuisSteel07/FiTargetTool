import flet as ft

def alert_invalid_data(root: ft.Page, message: str = "Valores Invalidados") -> ft.AlertDialog:
    alert = ft.AlertDialog(
        modal=True,
        title=ft.Text("Error"),
        content=ft.Text(message),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: root.close(alert))
        ]
    )

    return alert