from flet import TextField, TextAlign
from settings import AppSettings


def text_result(label, w) -> TextField:
    main_text_field: TextField = TextField(
        label=label,
        width=w,
        text_align=TextAlign.RIGHT,
    )

    return main_text_field