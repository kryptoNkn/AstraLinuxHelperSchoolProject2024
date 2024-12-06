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

    def open_telegram(e):
        webbrowser.open("https://t.me/krypton_alp")

    def open_github(e):
        webbrowser.open("https://github.com/kryptoNkn")

    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU, on_click=menu_manager.toggle_menu),
        title=ft.Text("Помощник по Astra Linux"),
        center_title=False,
        actions=[
            ft.IconButton(ft.icons.CODE, on_click=menu_manager.show_commands),
            ft.IconButton(ft.icons.BRIGHTNESS_4, on_click=toggle_theme)
        ]
    )

    stack = ft.Stack(
        [
            ft.Column(
                [
                    ft.Text("Добро пожаловать в помощник по Astra Linux!", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    ft.Text("Этот помощник предназначен для помощи в использовании Astra Linux.", style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text("Не стесняйтесь использовать этот инструмент для получения дополнительной информации.", style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Markdown(
                        "Полезные ссылки:\n"
                        "1. [Официальный сайт Astra Linux](https://www.astralinux.ru/)\n"
                        "2. [Форум Astra Linux](https://forum.astralinux.ru/)\n"
                        "3. [Документация Astra Linux](https://wiki.astralinux.ru/)\n"
                        "4. [Поддержка Astra Linux](https://support.astralinux.ru/)\n"
                        "5. [GitHub Astra Linux](https://github.com/astralinuxos)\n",
                        on_tap_link=lambda e: webbrowser.open(e.data)
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.FloatingActionButton(
                icon=ft.icons.TELEGRAM,
                on_click=open_telegram,
                tooltip="Telegram",
                bgcolor=ft.colors.BLUE_GREY,
                right=20,
                bottom=20
            ),
            ft.FloatingActionButton(
                content=ft.Icon(name="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z", color=ft.colors.WHITE),
                on_click=open_github,
                tooltip="GitHub",
                bgcolor=ft.colors.BLACK,
                right=80,
                bottom=20
            )
        ],
        expand=True
    )

    page.add(stack)

ft.app(target=main)