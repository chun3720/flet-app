# this is the main file where we handle user input data
from flet import *
from controls import return_control_reference

from form_helper import FormHelper

# get the global map dict

control_map = return_control_reference()


def update_text(e):
    # here, if the user double clicks the cells, it can become editable by turning off the read_only parameter
    e.control.content.controls[0].read_only = False
    e.control.content.controls[0].update()


# this method will handle the main data from the user.
# but before we can start taking in data, we need a place to store it
# now that the data table is set, we can start taking the data from the form field and displaying it
def get_input_data(e):
    # recall that the form instance is saved in the dictionary
    # we can access this now ...
    for key, value in control_map.items():
        # get the key called AppForm since it's where the values are
        if key == "AppForm":
            # once we're in the key, we need to create a DataRow
            data = DataRow(cells=[])
            # once we have the key, we can now loop over the textfields and get the values
            # first for loop is the first row
            for user_input in value.controls[0].content.controls[0].controls[:]:
                # here, we can no append that DataRow..
                data.cells.append(
                    # call the FormHelp calss..
                    # make sure to wrap the class in a DataCell@@
                    DataCell(
                        FormHelper(user_input.content.controls[1].value),
                        # the data cells can now take in some important events, namely tap events/cluck events
                        on_double_tap=lambda e: update_text(e),
                    )
                    # now these data
                )

            # second for loop is the second row
            for user_input in value.controls[0].content.controls[1].controls[:]:
                data.cells.append(
                    # call the FormHelp calss..
                    DataCell(FormHelper(user_input.content.controls[1].value))
                )

            # now that we have access to the values, we shoud create a data row + cell to insert it into the data table

        # we need to update the data table after we append
        if key == "AppDataTable":
            value.controls[0].controls[0].rows.append(data)
            value.controls[0].controls[0].update()

    pass


# for the button UI, this can be changed to fit the application theme
def return_from_button():
    # this UI was covered in previous tutorials, so you can check it out in previous videous
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: get_input_data(e),
            bgcolor="#081d33",
            color="white",
            content=Row(
                controls=[
                    Icon(
                        name=icons.ADD_ROUNDED,
                        size=12,
                    ),
                    Text("Add Input Field To Table", size=11, weight="bold"),
                ]
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6),
                },
                color={
                    "": "white",
                },
            ),
            height=42,
            width=220,
        ),
    )
