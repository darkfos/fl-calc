
class AppSettings:
    def __init__(self):
        self.weight: int = 500
        self.height: int = 400
        self.resize: bool = False

        #Button settings
        self.weight_btn: int = 80
        self.height_btn: int = 40
        self.hover_btn: str = "green"

        #TextField settings
        self.text_field_w_size: int = 500
        self.text_field_w_label: str = "Результат"
        self.animate_border_color: str = "yellow"
        self.animate_border_color_error: str = "red"
        self.animate_border_color_clear: str = "white"

        #General
        self.bottom: int = 5

        #TextSettings
        self.text_error: str = "Не удалось произвести операцию!"
        self.text_error_color: str = "red"
        self.bottom_top: int = 20
        self.width_error: int = 500