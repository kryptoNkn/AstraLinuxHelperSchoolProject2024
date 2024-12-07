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
        webbrowser.open("https://github.com/kryptoNkn/AstraLinuxHelperSchoolProject2024")

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
            ft.Container(
                content=ft.Column(
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
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                ),
                alignment=ft.alignment.center
            ),
            ft.Container(
                content=ft.Row(
                    [
                        ft.FloatingActionButton(
                            content=ft.Image(src="Logos/TelegramLogo.png", width=24, height=24),
                            on_click=open_telegram,
                            tooltip="Мы в Telegram",
                            bgcolor=ft.colors.BLUE_GREY
                        ),
                        ft.FloatingActionButton(
                            content=ft.Image(src="Logos/GitHubLogo.png", width=24, height=24),
                            on_click=open_github,
                            tooltip="Репозиторий GitHub",
                            bgcolor=ft.colors.BLACK
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END
                ),
                alignment=ft.alignment.bottom_right,
                margin=20
            )
        ],
        expand=True
    )

    page.add(stack)

ft.app(target=main)