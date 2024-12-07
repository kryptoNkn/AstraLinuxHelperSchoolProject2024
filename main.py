import flet as ft
import webbrowser
from info_manager import InfoManager
from menu_manager import MenuManager

def main(page: ft.Page):
    page.title = "Помощник по Astra Linux"
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

    def open_link(url):
        webbrowser.open(url)

    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU, on_click=menu_manager.toggle_menu),
        title=ft.Text("Помощник по Astra Linux"),
        center_title=False,
        actions=[
            ft.IconButton(ft.icons.CODE, on_click=menu_manager.show_commands),
            ft.IconButton(ft.icons.BRIGHTNESS_4, on_click=toggle_theme)
        ]
    )

    def create_clickable_text(text, url):
        return ft.GestureDetector(
            mouse_cursor=ft.MouseCursor.CLICK,
            on_tap=lambda _: open_link(url),
            content=ft.Text(text, style=ft.TextThemeStyle.BODY_LARGE, color=ft.colors.BLUE),
        )

    main_content = ft.Column(
        [
            ft.Text("Добро пожаловать в помощник по Astra Linux!", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
            ft.Text("Этот помощник предназначен для помощи в использовании Astra Linux.", style=ft.TextThemeStyle.BODY_LARGE),
            ft.Text("Не стесняйтесь использовать этот инструмент для получения дополнительной информации.", style=ft.TextThemeStyle.BODY_LARGE),
            ft.Text("Полезные ссылки:", style=ft.TextThemeStyle.BODY_LARGE),
            create_clickable_text("1. Официальный сайт Astra Linux", "https://www.astralinux.ru/"),
            create_clickable_text("2. Форум Astra Linux в Telegram", "https://t.me/astralinux_chat"),
            create_clickable_text("3. Документация Astra Linux", "https://wiki.astralinux.ru/"),
            create_clickable_text("4. Поддержка Astra Linux", "https://astragroup.ru/support/"),
            ft.Container(height=20),
            ft.Row(
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
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    page.add(
        ft.Column(
            [main_content],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

ft.app(target=main)