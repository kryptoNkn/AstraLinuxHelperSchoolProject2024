import flet as ft
from info_manager import InfoManager

class MenuManager:
    def __init__(self, page: ft.Page, info_manager: InfoManager):
        self.page = page
        self.info_manager = info_manager
        self.menu_container = None
        self.button_width = 250
        self.button_height = 50
        self.buttons = []
        self.search_field = None

    def create_menu(self):
        self.buttons = [
            ft.ElevatedButton("Назначение", on_click=self.show_purpose_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Начало работы", on_click=self.show_startup_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Завершение работы", on_click=self.show_shutdown_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Запуск ОС", on_click=self.show_boot_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Графический вход в систему", on_click=self.show_graphical_login_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Завершение работы в графическом режиме", on_click=self.show_graphical_shutdown_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Консольный вход и выход из системы", on_click=self.show_console_login_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Рабочий стол Fly", on_click=self.show_fly_desktop_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Режимы рабочего стола", on_click=self.show_desktop_modes_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Режим рабочего стола для ЭВМ", on_click=self.show_desktop_for_computer_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Планшетный режим для рабочего стола", on_click=self.show_tablet_mode_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Режим для мобильных устройств", on_click=self.show_mobile_mode_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Настройка рабочего стола пользователя", on_click=self.show_user_desktop_settings_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Панель управления", on_click=self.show_control_panel_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Менеджер файлов", on_click=self.show_file_manager_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Раздел 'Системные'", on_click=self.show_system_section_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Раздел 'Утилиты'", on_click=self.show_utilities_section_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Раздел 'Мобильные'", on_click=self.show_mobile_section_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Раздел 'Научные'", on_click=self.show_scientific_section_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Раздел 'Мультимедиа'", on_click=self.show_multimedia_section_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Камера GUVCView", on_click=self.show_guvcview_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Медиаплеер VLC", on_click=self.show_vlc_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Сеть", on_click=self.network, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Офисный пакет LibreOffice", on_click=self.show_libreoffice_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Веб-браузер Chromium", on_click=self.show_chromium_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Веб-браузер Chromium Gost", on_click=self.show_chromium_gost_info, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Служба передачи файлов FTP", on_click=self.ftp_files, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Печать документов", on_click=self.pe4at_docks, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Программа для 3d моделирования Blender", on_click=self.blender, width=self.button_width,height=self.button_height),
            ft.ElevatedButton("Клиент SSH", on_click=self.ssh, width=self.button_width,height=self.button_height),
            ft.ElevatedButton("Клиентская часть", on_click=self.client, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Команда who", on_click=self.who, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Оптимизация баз данных", on_click=self.optimize_data_bases, width=self.button_width, height=self.button_height),
            ft.ElevatedButton("Общие сведения", on_click=self.general_information, width=self.button_width,height=self.button_height),
        ]

        self.search_field = ft.TextField(label="Поиск", on_change=self.filter_buttons)

        self.menu_container = ft.Container(
            content=ft.Column(
                [self.search_field] + self.buttons,
                spacing=10,
                scroll=True,
            ),
            padding=10,
            margin=10,
            bgcolor=ft.colors.SURFACE_VARIANT,
            border_radius=5,
            width=self.button_width + 20,
            height=1080,
            animate=ft.animation.Animation(100, "ease"),
            offset=ft.transform.Offset(1, 0),
            visible=False,
        )
        self.page.overlay.append(self.menu_container)
        self.page.update()

    def toggle_menu(self, e):
        if self.menu_container.visible:
            self.menu_container.offset = ft.transform.Offset(1, 0)
            self.menu_container.visible = False
        else:
            self.menu_container.offset = ft.transform.Offset(0, 0)
            self.menu_container.visible = True

        self.menu_container.update()
        self.page.update()

    def filter_buttons(self, e):
        search_text = self.search_field.value.lower()
        for button in self.buttons:
            button.visible = search_text in button.text.lower()
        self.menu_container.update()

    def show_commands(self, e):
        commands = (
            "Команды для Astra Linux:\n"
            "1. sudo apt update - Обновление списка пакетов.\n"
            "2. sudo apt upgrade - Обновление установленных пакетов.\n"
            "3. sudo apt install <package_name> - Установка пакета.\n"
            "4. sudo apt remove <package_name> - Удаление пакета.\n"
            "5. sudo apt autoremove - Удаление ненужных пакетов.\n"
            "6. sudo systemctl start <service_name> - Запуск сервиса.\n"
            "7. sudo systemctl stop <service_name> - Остановка сервиса.\n"
            "8. sudo systemctl restart <service_name> - Перезапуск сервиса.\n"
            "9. sudo systemctl status <service_name> - Проверка статуса сервиса.\n"
            "10. sudo reboot - Перезагрузка системы.\n"
            "11. sudo poweroff - Выключение системы.\n"
            "12. ls -l - Вывод списка файлов в текущей директории.\n"
            "13. cd <directory_name> - Переход в указанную директорию.\n"
            "14. pwd - Вывод текущей директории.\n"
            "15. cp <source> <destination> - Копирование файла или директории.\n"
            "16. mv <source> <destination> - Перемещение или переименование файла или директории.\n"
            "17. rm <file_name> - Удаление файла.\n"
            "18. mkdir <directory_name> - Создание директории.\n"
            "19. rmdir <directory_name> - Удаление пустой директории.\n"
            "20. tar -czvf <archive_name>.tar.gz <directory_name> - Архивирование директории.\n"
            "21. tar -xzvf <archive_name>.tar.gz - Распаковка архива.\n"
            "22. ifconfig - Вывод информации о сетевых интерфейсах.\n"
            "23. ping <hostname_or_ip> - Проверка связи с указанным хостом.\n"
            "24. netstat -tuln - Вывод информации о сетевых подключениях.\n"
            "25. df -h - Вывод информации о дисковом пространстве.\n"
            "26. du -sh <directory_name> - Вывод информации о размере директории.\n"
            "27. top - Вывод информации о запущенных процессах.\n"
            "28. ps aux - Вывод информации о запущенных процессах.\n"
            "29. kill <pid> - Завершение процесса по PID.\n"
            "30. killall <process_name> - Завершение всех процессов с указанным именем.\n"
        )
        self.info_manager.show_info("Команды для Astra Linux", commands)

    def show_purpose_info(self, e):
        info = (
            "Astra Linux — это российская операционная система, разработанная для обеспечения высокого уровня безопасности и совместимости с российскими стандартами.\n"
            "Назначение:\n"
            "1. Обеспечение безопасности информационных систем.\n"
            "2. Соответствие российским стандартам и требованиям.\n"
            "3. Поддержка российских приложений и технологий.\n"
            "4. Удобный и интуитивно понятный интерфейс для пользователей."
        )
        self.info_manager.show_info("Назначение Astra Linux", info)

    def general_information(self, e):
        info = (
            "OC предназначена для построения информационных (автоматизированных) систем,\n"
            "обрабатывающих информацию ограниченного доступа, в том числе содержащую сведения,\n"
            "составляющие государственную тайну.\n"
            "с обработкой информации в условиях сохранения государственной тайны. Для этого ОС\n"
            "оснащена защищенной графической оболочкой и, кроме стандартного пакета офисных\n"
            "программ, включает в себя:\n"
            "   - защищенный комплекс программ печати и учета документов;\n"
            "   - защищенную СУБД;\n"
            "   - защищенный комплекс программ гипертекстовой обработки данных;\n"
            "   - защищенный комплекс программ электронной почты.\n"
        )
        self.info_manager.show_info("Общие сведения", info)

    def show_startup_info(self, e):
        info = (
            "Для начала работы:\n"
            "1. Включите компьютер.\n"
            "2. Дождитесь загрузки Astra Linux.\n"
            "3. Введите учетные данные для входа в систему.\n"
            "4. После входа в систему вы сможете начать работу с Astra Linux."
        )
        self.info_manager.show_info("Начало работы", info)

    def show_shutdown_info(self, e):
        info = (
            "Для завершения работы:\n"
            "1. Откройте меню 'Система'.\n"
            "2. Выберите пункт 'Выключение'.\n"
            "3. Подтвердите выключение системы.\n"
            "4. Это безопасный способ завершения работы с Astra Linux."
        )
        self.info_manager.show_info("Завершение работы", info)

    def show_boot_info(self, e):
        info = (
            "Для запуска ОС:\n"
            "1. Включите компьютер.\n"
            "2. Выберите Astra Linux в меню загрузки.\n"
            "3. Дождитесь загрузки системы.\n"
            "4. После загрузки вы сможете войти в систему."
        )
        self.info_manager.show_info("Запуск ОС", info)

    def show_graphical_login_info(self, e):
        info = (
            "Для графического входа в систему:\n"
            "1. Включите компьютер.\n"
            "2. Дождитесь загрузки графического интерфейса.\n"
            "3. Введите учетные данные для входа.\n"
            "4. Графический вход предоставляет удобный интерфейс для входа в систему."
        )
        self.info_manager.show_info("Графический вход в систему", info)

    def show_graphical_shutdown_info(self, e):
        info = (
            "Для завершения работы в графическом режиме:\n"
            "1. Откройте меню 'Система'.\n"
            "2. Выберите пункт 'Выключение'.\n"
            "3. Подтвердите выключение системы.\n"
            "4. Это безопасный способ завершения работы с Astra Linux в графическом режиме."
        )
        self.info_manager.show_info("Завершение работы в графическом режиме", info)

    def show_console_login_info(self, e):
        info = (
            "Для консольного входа и выхода из системы:\n"
            "1. Включите компьютер.\n"
            "2. Дождитесь загрузки консоли.\n"
            "3. Введите учетные данные для входа.\n"
            "4. Для выхода из системы введите команду 'exit'.\n"
            "5. Консольный вход и выход предоставляет доступ к системе через текстовый интерфейс."
        )
        self.info_manager.show_info("Консольный вход и выход из системы", info)

    def show_fly_desktop_info(self, e):
        info = (
            "Рабочий стол Fly:\n"
            "1. Включите компьютер.\n"
            "2. Дождитесь загрузки графического интерфейса.\n"
            "3. Выберите рабочий стол Fly для использования.\n"
            "4. Рабочий стол Fly предоставляет удобный и современный интерфейс с множеством функций."
        )
        self.info_manager.show_info("Рабочий стол Fly", info)

    def show_desktop_modes_info(self, e):
        info = (
            "Режимы рабочего стола:\n"
            "1. Включите компьютер.\n"
            "2. Дождитесь загрузки графического интерфейса.\n"
            "3. Выберите нужный режим рабочего стола (например, Fly, GNOME, KDE).\n"
            "4. Различные режимы рабочего стола предоставляют разные опыты работы с системой.\n"
            "5. Fly — современный и удобный рабочий стол.\n"
            "6. GNOME — классический рабочий стол с богатым набором функций.\n"
            "7. KDE — гибкий и настраиваемый рабочий стол."
        )
        self.info_manager.show_info("Режимы рабочего стола", info)

    def show_desktop_for_computer_info(self, e):
        info = (
            "Режим рабочего стола для ЭВМ:\n"
            "1. Включите компьютер.\n"
            "2. Дождитесь загрузки графического интерфейса.\n"
            "3. Выберите режим рабочего стола, оптимизированный для ЭВМ.\n"
            "4. Этот режим предоставляет оптимизированный интерфейс для работы на настольных компьютерах.\n"
            "5. Оптимизирован для высокой производительности и удобства использования."
        )
        self.info_manager.show_info("Режим рабочего стола для ЭВМ", info)

    def show_tablet_mode_info(self, e):
        info = (
            "Планшетный режим для рабочего стола:\n"
            "1. Включите планшет.\n"
            "2. Дождитесь загрузки графического интерфейса.\n"
            "3. Выберите планшетный режим для удобства использования.\n"
            "4. Планшетный режим оптимизирован для использования на планшетных устройствах.\n"
            "5. Предоставляет удобный интерфейс для сенсорного управления."
        )
        self.info_manager.show_info("Планшетный режим для рабочего стола", info)

    def show_mobile_mode_info(self, e):
        info = (
            "Режим для мобильных устройств:\n"
            "1. Включите мобильное устройство.\n"
            "2. Дождитесь загрузки графического интерфейса.\n"
            "3. Выберите режим, оптимизированный для мобильных устройств.\n"
            "4. Этот режим предоставляет удобный интерфейс для использования на смартфонах.\n"
            "5. Оптимизирован для сенсорного управления и компактного экрана."
        )
        self.info_manager.show_info("Режим для мобильных устройств", info)

    def show_user_desktop_settings_info(self, e):
        info = (
            "Настройка рабочего стола пользователя:\n"
            "1. Откройте 'Параметры'.\n"
            "2. Перейдите в раздел 'Рабочий стол'.\n"
            "3. Настройте внешний вид и функциональность рабочего стола.\n"
            "4. Вы можете изменить тему, обои, иконки и другие параметры рабочего стола.\n"
            "5. Настройка позволяет адаптировать рабочий стол под ваши предпочтения."
        )
        self.info_manager.show_info("Настройка рабочего стола пользователя", info)

    def show_control_panel_info(self, e):
        info = (
            "Панель управления:\n"
            "1. Откройте 'Панель управления'.\n"
            "2. Используйте её для настройки системы и управления устройствами.\n"
            "3. Панель управления предоставляет доступ к различным настройкам и утилитам.\n"
            "4. Здесь вы можете настроить сеть, звук, дисплей и другие параметры системы."
        )
        self.info_manager.show_info("Панель управления", info)

    def show_file_manager_info(self, e):
        info = (
            "Менеджер файлов:\n"
            "1. Откройте 'Менеджер файлов'.\n"
            "2. Используйте его для управления файлами и папками на вашем компьютере.\n"
            "3. Менеджер файлов позволяет просматривать, копировать, перемещать и удалять файлы.\n"
            "4. Удобный интерфейс для работы с файловой системой."
        )
        self.info_manager.show_info("Менеджер файлов", info)

    def show_system_section_info(self, e):
        info = (
            "Раздел 'Системные':\n"
            "1. Откройте 'Панель управления'.\n"
            "2. Перейдите в раздел 'Системные' для настройки системных параметров.\n"
            "3. В этом разделе вы можете настроить параметры ядра, драйверов и других системных компонентов.\n"
            "4. Важно знать, что изменение системных параметров может повлиять на стабильность системы."
        )
        self.info_manager.show_info("Раздел 'Системные'", info)

    def show_utilities_section_info(self, e):
        info = (
            "Раздел 'Утилиты':\n"
            "1. Откройте 'Панель управления'.\n"
            "2. Перейдите в раздел 'Утилиты' для доступа к различным инструментам.\n"
            "3. В этом разделе вы найдете утилиты для оптимизации, обслуживания и диагностики системы.\n"
            "4. Утилиты помогают поддерживать систему в рабочем состоянии."
        )
        self.info_manager.show_info("Раздел 'Утилиты'", info)

    def show_mobile_section_info(self, e):
        info = (
            "Раздел 'Мобильные':\n"
            "1. Откройте 'Панель управления'.\n"
            "2. Перейдите в раздел 'Мобильные' для настройки параметров мобильных устройств.\n"
            "3. В этом разделе вы можете настроить синхронизацию, передачу данных и другие параметры для мобильных устройств.\n"
            "4. Удобный интерфейс для управления мобильными устройствами."
        )
        self.info_manager.show_info("Раздел 'Мобильные'", info)

    def show_scientific_section_info(self, e):
        info = (
            "Раздел 'Научные':\n"
            "1. Откройте 'Панель управления'.\n"
            "2. Перейдите в раздел 'Научные' для доступа к научным приложениям и инструментам.\n"
            "3. В этом разделе вы найдете программы для моделирования, анализа данных и других научных задач.\n"
            "4. Обеспечивает доступ к мощным инструментам для научных исследований."
        )
        self.info_manager.show_info("Раздел 'Научные'", info)

    def show_multimedia_section_info(self, e):
        info = (
            "Раздел 'Мультимедиа':\n"
            "1. Откройте 'Панель управления'.\n"
            "2. Перейдите в раздел 'Мультимедиа' для настройки аудио и видео устройств.\n"
            "3. В этом разделе вы можете настроить параметры звука, видео и других мультимедийных устройств.\n"
            "4. Удобный интерфейс для настройки мультимедийных параметров."
        )
        self.info_manager.show_info("Раздел 'Мультимедиа'", info)

    def show_guvcview_info(self, e):
        info = (
            "Камера GUVCView:\n"
            "1. Откройте 'GUVCView'.\n"
            "2. Настройте параметры камеры.\n"
            "3. Начните запись или снимать фотографии.\n"
            "4. GUVCView — это удобный инструмент для работы с веб-камерами.\n"
            "5. Поддерживает различные форматы видео и фото."
        )
        self.info_manager.show_info("Камера GUVCView", info)

    def show_vlc_info(self, e):
        info = (
            "Медиаплеер VLC:\n"
            "1. Откройте 'VLC'.\n"
            "2. Выберите файл для воспроизведения.\n"
            "3. Настройте параметры воспроизведения.\n"
            "4. VLC — это мощный медиаплеер с поддержкой множества форматов.\n"
            "5. Поддерживает видео, аудио, потоковое вещание и другие медиафайлы."
        )
        self.info_manager.show_info("Медиаплеер VLC", info)

    def network(self, e):
        info = (
            "Подключение к интернету:\n"
            "1. Откройте 'Панель управления'.\n"
            "2. Перейдите в раздел 'Сеть и интернет'.\n"
            "3. Выберите 'Устройства и принтеры'.\n"
            "4. Найдите ваше сетевое устройство и нажмите на него.\n"
            "5. Выберите 'Свойства'.\n"
            "6. В разделе 'Общие' выберите 'Подключв тоение по локальной сети'.\n"
            "7. Нажмите 'Свойства'.\n"
            "8. В разделе 'Протокол Интернета версии 4 (TCP/IPv4)' выберите 'Использовать следующий IP-адрес'.\n"
            "9. Введите IP-адрес, маску подсети и шлюз по умолчанию.\n"
            "10. В разделе 'Протокол Интернета версии 4 (TCP/IPv4)' выберите 'Использовать следующие адреса серверов DNS'.\n"
            "11. Введите предпочтительный и альтернативный DNS-серверы.\n"
            "12. Нажмите 'ОК' для сохранения настроек.\n"
            "13. Перезапустите сетевой интерфейс, если необходимо."
        )
        self.info_manager.show_info("Сеть", info)

    def show_libreoffice_info(self, e):
        info = (
            "LibreOffice — это мощный офисный пакет с открытым исходным кодом, который предоставляет полный набор инструментов для создания и редактирования документов, электронных таблиц, презентаций и других офисных файлов.\n"
            "Основные компоненты LibreOffice:\n"
            "1. Writer — текстовый процессор для создания и редактирования документов.\n"
            "2. Calc — электронная таблица для работы с числовыми данными и создания отчетов.\n"
            "3. Impress — инструмент для создания презентаций с богатыми графическими возможностями.\n"
            "4. Draw — векторный графический редактор для создания и редактирования изображений.\n"
            "5. Base — система управления базами данных для создания и управления базами данных.\n"
            "6. Math — редактор математических формул для создания и редактирования математических выражений.\n"
            "LibreOffice поддерживает широкий спектр форматов файлов, включая форматы Microsoft Office, что делает его совместимым с большинством офисных приложений."
        )
        self.info_manager.show_info("Офисный пакет LibreOffice", info)

    def show_chromium_info(self, e):
        info = (
            "Chromium — это открытый веб-браузер, разработанный Google. Он является основой для браузера Google Chrome, но не включает некоторые коммерческие компоненты и сервисы.\n"
            "Основные особенности Chromium:\n"
            "1. Быстрая и эффективная работа с веб-страницами.\n"
            "2. Поддержка последних веб-стандартов и технологий.\n"
            "3. Гибкость и настраиваемость через расширения.\n"
            "4. Регулярные обновления для обеспечения безопасности и улучшения функциональности."
        )
        self.info_manager.show_info("Веб-браузер Chromium", info)

    def show_chromium_gost_info(self, e):
        info = (
            "Chromium GOST — это модифицированная версия веб-браузера Chromium, адаптированная для использования в российских сетях. Он поддерживает российские криптографические стандарты (ГОСТ) и обеспечивает безопасность при работе с государственными и корпоративными ресурсами.\n"
            "Основные особенности Chromium GOST:\n"
            "1. Поддержка российских криптографических стандартов (ГОСТ).\n"
            "2. Обеспечение безопасности при работе с государственными и корпоративными ресурсами.\n"
            "3. Совместимость с основными функциями и расширениями Chromium.\n"
            "4. Регулярные обновления для поддержания актуальности и безопасности."
        )
        self.info_manager.show_info("Веб-браузер Chromium GOST", info)

    def ftp_files(self, e):
        info = (
            "Служба передачи файлов FTP\n"
            "1. Установка соединения с FTP-сервером по адресу, имени пользователя и паролю.\n"
            "2. Просмотр списка файлов и папок на FTP-сервере.\n"
            "3. Навигация по директориям.\n"
            "4. Скачивание выбранных файлов на локальный компьютер.\n"
        )
        self.info_manager.show_info("Служба передачи файлов FTP", info)

    def pe4at_docks(self, e):
        info = (
            "Возможности печати документов\n"
            "1. Выбор доступного принтера из списка подключенных устройств.\n"
            "2. Возможность добавления нового принтера.\n"
            "3. Поддержка различных форматов документов (PDF, DOCX, TXT и т.д.).\n"
            "4. Выбор размера бумаги (A4, A3, Letter и т.д.).\n"
            "5. Возможность редактирования документа перед печатью.\n"
        )
        self.info_manager.show_info("Печать документов", info)

    def blender(self, e):
        info = (
            "Возможности программы 3D-моделирования Blender\n"
            "1. Создание и редактирование 3D-моделей с использованием примитивов (куб, сфера, цилиндр и т.д.).\n"
            "2. Создание и редактирование анимации объектов.\n"
            "3. Поддержка скелетной анимации и инверсной кинематики.\n"
            "4. Инструменты для создания ключевых кадров и временной шкалы.\n"
            "5. Симуляция физики для объектов (гравитация, столкновения, твердотельная динамика).\n"
            "6. Поддержка рендеринга с использованием встроенного рендерера Eevee и Cycles.\n"
        )
        self.info_manager.show_info("Программа для 3d моделирования Blender", info)

    def ssh(self, e):
        info = (
            "Возможности клиента SSH\n"
            "1. Подключение к удаленному серверу\n"
            "2. Передача файлов\n"
            "3. Управление сессиями\n"
            "4. Перенаправление портов\n"
            "5. Поддержка прокси\n"
            "6. Поддержка различных криптографических алгоритмов\n"
        )
        self.info_manager.show_info("Клиент SSH", info)

    def client(self, e):
        info = (
            "Возможности клиентской части\n"
            "1. Отображение интерфейса\n"
            "2. Взаимодействие с сервером\n"
            "3. Обработка данных\n"
            "4. Управление состоянием\n"
            "5. Оптимизация производительности\n"
            "6. Интеграция с другими системами\n"
        )
        self.info_manager.show_info("Клиентская часть", info)

    def who(self, e):
        info = (
            "Возможности команды who\n"
            "1. Отображение информации о пользователях\n"
            "2. Фильтрация результатов\n"
            "3. Отображение подробной информации\n"
            "4. Обновление информации\n"
            "5. Экспорт результатов\n"
        )
        self.info_manager.show_info("Команда who", info)

    def optimize_data_bases(self, e):
        info = (
            "Возможности оптимизации баз данных\n"
            "1. Индексация\n"
            "2. Оптимизация запросов\n"
            "3. Кеширование\n"
            "4. Оптимизация схемы данных\n"
            "5. Оптимизация операций ввода-вывода\n"
            "6. Оптимизация памяти\n"
        )
        self.info_manager.show_info("Оптимизация баз данных", info)