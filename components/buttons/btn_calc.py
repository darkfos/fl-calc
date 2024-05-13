from flet import FloatingActionButton, ElevatedButton
from typing import Optional, Union

def btn_calc(text_btn: str, color: str, colortext: str, width: Union[None, int] = None) -> ElevatedButton:
    btn: ElevatedButton = ElevatedButton(text=text_btn, bgcolor=color, color=colortext, width=width)
    return btn
