from flet import TextField, TextAlign
from settings import AppSettings


def text_result(label, w) -> TextField:
    def event_reaction(event):
        main_text_field.border_color = AppSettings().animate_border_color

    main_text_field: TextField = TextField(
        label=label,
        width=w,
        text_align=TextAlign.RIGHT,
        on_change=event_reaction
    )

    return main_text_field