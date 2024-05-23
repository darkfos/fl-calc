import flet
from flet import FloatingActionButton, ElevatedButton, TextField, ButtonStyle, MaterialState
from typing import Optional, Union
from ..texts.error_message import text_error_bottom


def btn_calc(
        text_btn: str,
        color: str,
        colortext: str,
        width: Union[None, int] = None,
        height: Union[None, int] = None,
        on_click_event: TextField = None,
        page: flet.Page = None,
        settings = None
) -> ElevatedButton:

    def set_text(event):
        #On clicked btn

        match (btn.text):
            case "CLEAR":
                on_click_event.value = ""
                on_click_event.label = "Очищено"
                on_click_event.border_color = "white"
                page.update()
            case "=":
                try:
                    on_click_event.value = str(eval(on_click_event.value))
                    on_click_event.border_color = settings.animate_border_color_clear
                except Exception as ex:
                    on_click_event.value = "Ошибка"
                    page.add(text_error_bottom(page=page))
                    on_click_event.border_color = settings.animate_border_color_error
                finally:
                    on_click_event.label = "Подсчет"
                    page.update()
            case _:
                on_click_event.value = on_click_event.value + btn.text
                page.update()

    def on_hover_btn(event):
        #On hover btn

        btn.bgcolor = settings.hover_btn
        page.update()
        btn.bgcolor = color

    btn: ElevatedButton = ElevatedButton(
        text=text_btn,
        bgcolor=color,
        color=colortext,
        width=width,
        height=height,
        on_click=set_text,
        on_hover=on_hover_btn)

    return btn