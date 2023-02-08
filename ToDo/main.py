import flet as ft

def main(page: ft.page):
    
    def addTask(p):
        checkBox = ft.Checkbox(value= False)
        checkBoxText = ft.Text(value = textField.value, width = 350, bgcolor="white", size = 24)
        taskRow = ft.Row(controls = [checkBox, checkBoxText], alignment= ft.MainAxisAlignment.START)
        page.add(taskRow)
        
    
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "white"
    textField = ft.TextField(width = 350)
    addBtn = ft.FloatingActionButton(icon = ft.icons.ADD, on_click=addTask)
    # checkBox = ft.Checkbox(value= True)
    # checkBoxText = ft.Text(value = "Task 1", width = 350, bgcolor="white", size = 24)
    
    entriesRow = ft.Row(controls = [textField, addBtn], alignment= ft.MainAxisAlignment.SPACE_BETWEEN)
    
    page.add(entriesRow)

ft.app(target = main)