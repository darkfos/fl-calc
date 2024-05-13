import flet
from flet import Page, app, Column, Row, MainAxisAlignment, Container, margin
from components.buttons.btn_calc import btn_calc
from components.textfield.input_text_field import text_result
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

        header_app = Container(
            Row(
                controls=[
                    btn_calc("(", color="purple", colortext="black", width=80),
                    btn_calc(")", color="purple", colortext="black", width=80),
                    btn_calc("CLEAR", color="purple", colortext="black", width=200),
                ],
            ),
        )


        row_btn_1 = Row(
            controls=[
                btn_calc("1", color="orange", colortext="black"),
                btn_calc("2", color="orange", colortext="black"),
                btn_calc("3", color="orange", colortext="black"),
                btn_calc("4", color="orange", colortext="black"),
                btn_calc("5", color="orange", colortext="black")
            ],
            spacing=20,
            alignment=MainAxisAlignment.CENTER
        )
        row_btn_2 = Row(
            controls=[
                btn_calc("6", color="orange", colortext="black"),
                btn_calc("7", color="orange", colortext="black"),
                btn_calc("8", color="orange", colortext="black"),
                btn_calc("9", color="orange", colortext="black"),
                btn_calc("0", color="orange", colortext="black")
            ],
            spacing=20,
            alignment=MainAxisAlignment.CENTER
        )
        row_btn_3 = Row(
            controls=[
                btn_calc("+", color="blue", colortext="black"),
                btn_calc("-", color="blue", colortext="black"),
                btn_calc("*", color="blue", colortext="black"),
                btn_calc("/", color="blue", colortext="black"),
                btn_calc("=", color="red", colortext="black")
            ],
            spacing=20,
            alignment=MainAxisAlignment.CENTER
        )

        self.page.add(text_result(label=self.settings.text_field_w_label, w=self.settings.text_field_w_size))
        self.page.add(header_app, row_btn_1, row_btn_2, row_btn_3)

    def update(self):
        self.page.update()

    def start_application(self):
        self.set_components()
        self.update()

if __name__ == "__main__":
    calc_app: app = app(target=Application)