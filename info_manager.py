import flet as ft

class InfoManager:
    def __init__(self, page: ft.Page):
        self.page = page

    def show_info(self, title, content):
        self.page.dialog = ft.AlertDialog(
            title=ft.Text(title),
            content=ft.Text(content),
            actions=[ft.TextButton("Закрыть", on_click=self.close_dlg)]
        )
        self.page.dialog.open = True
        self.page.update()

    def close_dlg(self, e):
        self.page.dialog.open = False
        self.page.update()