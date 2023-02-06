import flet as ft
from pdf2docx import Converter
import os


def main(page: ft.Page):
    name_file = ft.TextField(label="Rename File")

    def my_func_process(e: ft.FilePickerResultEvent):
        path = os.getcwd()

        # Get you file on picket
        for x in e.files:
            print("Your path", x.path)
            pdf_file = x.path
            docx_file = path + f"/{name_file.value}.docx"

            try:
                res = Converter(pdf_file)
                res.convert(docx_file)
                res.close()
            except:
                print("fail!!")
            else:
                print("successfuly converted!")
                page.snack_bar = ft.SnackBar(
                    ft.Text("Successfully converted", size=30), bgcolor="green"
                )
                page.snack_bar.open = True

    filepicker = ft.FilePicker(on_result=my_func_process)
    page.overlay.append(filepicker)
    page.add(
        ft.Column(
            [
                ft.Text("Convert pdf to docx", size=30),
                name_file,
                ft.ElevatedButton(
                    "Convert Now",
                    bgcolor="blue",
                    color="white",
                    on_click=lambda _: filepicker.pick_files(),
                ),
            ]
        )
    )


ft.app(target=main, assets_dir="flet-convertor")
