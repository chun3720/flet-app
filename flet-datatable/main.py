import flet
from flet import *
from header import AppHeader
from form import AppForm
from data_table import AppDataTable


def main(page: Page):
    page.bgcolor = "#fdfdfd"
    page.padding = 20
    page.add(
        # main column where each app component will be replaced and displayed
        Column(
            expand=True,
            controls=[
                # class instances go here ...
                AppHeader(),
                Divider(height=2, color="transparent"),
                AppForm(),
                # we call the data table class inside this column
                Column(scroll="hidden", expand=True, controls=[AppDataTable()]),
            ],
        )
    )
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
