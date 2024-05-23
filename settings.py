
class AppSettings:
    def __init__(self):
        self.weight: int = 500
        self.height: int = 400
        self.resize: bool = False

        #Button settings
        self.weight_btn: int = 80
        self.height_btn: int = 40

        #TextField settings
        self.text_field_w_size: int = 500
        self.text_field_w_label: str = "Результат"

        self.bottom: int = 5