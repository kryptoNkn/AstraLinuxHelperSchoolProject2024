import flet as ft
import webbrowser
from info_manager import InfoManager
from menu_manager import MenuManager

def main(page: ft.Page):
    page.title = "Помощник по Astra Linux"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_maximized = True

    info_manager = InfoManager(page)
    menu_manager = MenuManager(page, info_manager)
    menu_manager.create_menu()

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            page.update()
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.update()

    def show_useful_links(e):
        links = (
            "Полезные ссылки:\n"
            "1. [Официальный сайт Astra Linux](https://www.astralinux.ru/)\n"
            "2. [Форум Astra Linux](https://forum.astralinux.ru/)\n"
            "3. [Документация Astra Linux](https://wiki.astralinux.ru/)\n"
            "4. [Поддержка Astra Linux](https://support.astralinux.ru/)\n"
        )
        info_manager.show_info("Полезные ссылки", ft.Markdown(links, on_tap_link=lambda e: webbrowser.open(e.data)))

    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU, on_click=menu_manager.toggle_menu),
        title=ft.Text("Помощник по Astra Linux"),
        center_title=False,
        actions=[
            ft.IconButton(ft.icons.CODE, on_click=menu_manager.show_commands),
            ft.IconButton(ft.icons.BRIGHTNESS_4, on_click=toggle_theme)
        ]
    )

    page.add(
        ft.Column(
            [
                ft.Text("Добро пожаловать в помощник по Astra Linux!", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                ft.Markdown(
                    "Полезные ссылки:\n"
                    "1. [Официальный сайт Astra Linux](https://www.astralinux.ru/)\n"
                    "2. [Форум Astra Linux](https://forum.astralinux.ru/)\n"
                    "3. [Документация Astra Linux](https://wiki.astralinux.ru/)\n"
                    "4. [Поддержка Astra Linux](https://support.astralinux.ru/)\n",
                    on_tap_link=lambda e: webbrowser.open(e.data)
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)