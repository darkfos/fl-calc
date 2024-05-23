from flet import Text, TextAlign, Container, margin, TextThemeStyle, Page
from settings import AppSettings


def text_error_bottom(page: Page) -> Container:
    #Error message

    error_message: Container = Container(
        Text(
            value=AppSettings().text_error,
            color=AppSettings().text_error_color,
            text_align=TextAlign.CENTER,
            width=AppSettings().width_error,
            theme_style=TextThemeStyle.TITLE_MEDIUM
        ),
        margin=margin.only(top=AppSettings().bottom_top),
    )

    return error_message