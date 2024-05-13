import flet
from flet import Page, app, Column, Row, MainAxisAlignment
from components.buttons.btn_calc import btn_calc
from settings import AppSettings


class Application:

    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Fl-calc"
        self.settings: AppSettings = AppSettings()

        #Page settings
        self.page.window_width = self.settings.weight
        self.page.window_height = self.settings.height
        self.page.window_resizable = self.settings.resize


        #Start application
        self.start_application()

    def set_components(self):
        clmn_btn = Row(
            controls=[
                btn_calc("1"),
                btn_calc("2"),
                btn_calc("3"),
                btn_calc("4"),
                btn_calc("5")
            ],
            spacing=20,
            alignment=MainAxisAlignment.CENTER
        )
        self.page.add(clmn_btn)
    def update(self):
        self.page.update()

    def start_application(self):
        self.set_components()
        self.update()

if __name__ == "__main__":
    calc_app: app = app(target=Application)