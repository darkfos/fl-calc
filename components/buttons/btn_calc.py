import flet
from flet import FloatingActionButton, ElevatedButton, TextField
from typing import Optional, Union


def btn_calc(
        text_btn: str,
        color: str,
        colortext: str,
        width: Union[None, int] = None,
        height: Union[None, int] = None,
        on_click_event: TextField = None,
        page: flet.Page = None
) -> ElevatedButton:

    def set_text(event):
        #On clicked btn

        match (btn.text):
            case "CLEAR":
                on_click_event.value = ""
                on_click_event.label = "Очищено"
                page.update()
            case "=":
                try:
                    on_click_event.value = str(eval(on_click_event.value))
                except Exception as ex:
                    on_click_event.value = "Ошибка"
                finally:
                    on_click_event.label = "Подсчет"
                    page.update()
            case _:
                on_click_event.value = on_click_event.value + btn.text
                page.update()

    btn: ElevatedButton = ElevatedButton(text=text_btn, bgcolor=color, color=colortext, width=width, height=height, on_click=set_text)

    return btn