# main class for data table UI
from flet import *
from controls import add_to_control_reference


class AppDataTable(UserControl):
    def __init__(self):
        super().__init__()

    # need to send the instance of data table to the dict
    def app_data_table_instance(self):
        add_to_control_reference("AppDataTable", self)

    def build(self):
        self.app_data_table_instance()
        return Row(
            # in order to make thr data table control scroll, we need to configure it in a special way, since the control doesn't have a parameter for scrolling.
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, "#ebebeb"),
                    horizontal_lines=border.BorderSide(1, "#ebebeb"),
                    # the columns args will set the number of columns to be displayed
                    columns=[
                        DataColumn(
                            Text("Column One", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Column Two", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Column Three", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Column Four", size=12, color="black", weight="bold")
                        ),
                    ],
                    # here, we will configure the form button to append the data rows
                    rows=[],
                )
            ],
        )
