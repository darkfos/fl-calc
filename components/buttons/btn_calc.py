from flet import FloatingActionButton


def btn_calc(text_btn: str) -> FloatingActionButton:
    btn: FloatingActionButton = FloatingActionButton(text=text_btn)
    return btn
