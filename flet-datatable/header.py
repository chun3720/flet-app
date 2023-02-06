# this is the header of the desktop application

# modules

from flet import *
from controls import add_to_control_reference, return_control_reference

# we can set the returned dict as variable at the top of the class

# we'll use this layer in the app

control_map = return_control_reference()

# main class
class AppHeader(UserControl):
    def __init__(self):
        super().__init__()
        
    
    def app_header_instance(self):
        # this function sets the class instance as a key:value pair in the global dict.
        add_to_control_reference("AppHeader", self)
            # so the key -> "AppHeader"
            # and the value => self (which is the instance, e.g. the object location in memory)
            
    # let's create some of the header inner components 
    def app_header_brand(self):
        return Container(
            content = Text("Line Indent", size = 15)
        )
        
    def app_header_search(self):
        return Container(
            width = 320, 
            bgcolor = 'white10',
            border_radius=6,
            padding = 8, 
            opacity = 0,
            animate_opacity= 320,
            content = Row(
                spacing = 10,
                vertical_alignment= CrossAxisAlignment.CENTER,
                controls=[
                    Icon(name = icons.SEARCH_OFF_ROUNDED, size = 17, opacity = 0.85),
                    TextField(
                        # some basic UI from my end
                        border_color = "transparent",
                        height = 20,
                        text_size = 14,
                        content_padding = 0,
                        cursor_color='white',
                        cursor_width=1,
                        color='white',
                        hint_text="Search",
                        # make sure to set the function here
                        # it shoud be on_change
                        on_change = lambda e:self.filter_data_table(e),
                    )
                ]
            )
            
        )
    def app_header_avatar(self):
        return Container(
            content = IconButton(icons.PERSON)
        )
        
    # we want to show the search bar whenever the user hover over th eheader
    def show_search_bar(self, e):
        if e.data == 'true':
            self.controls[0].content.controls[1].opacity = 1
            self.controls[0].content.controls[1].update()
            
        else:
            # we want to remove the text when we make the search bar disappear
            self.controls[0].content.controls[1].content.controls[1].value = ""
            self.controls[0].content.controls[1].opacity = 0
            self.controls[0].content.controls[1].update()
            
    # now for the final part, we want to implement some basic search and filter mechanism.
    
    def filter_data_table(self, e):
        # now the textfield for the search bar has a method that returns the data being written => e.data
        # so we can use this to filter our data table
        # again, we can call our controls map here...
        for key, value in control_map.items():
            if key == "AppDataTable":
                # check if the data rows are not empty
                if len(value.controls[0].controls[0].rows) != 0:
                    for data in value.controls[0].controls[0].rows[:]:
                        # here, we loop through the FIRST COLUMN data cells (not all of them), and we check to see if the written character is in the value of each data cell
                        # if it is, then we keep it, else, we make visibility false
                        # make the e.data to e.data.lowr()
                        if e.data.lower() in data.cells[0].content.controls[0].value.lower():
                            data.visible = True
                            data.update()
                        else:
                            data.visible = False
                            data.update()
                    
                # so the basic search works, except it doesn't take it upper case letter
                # so the search works well now
    
    def build(self):
        self.app_header_instance()
        
        return Container(
            expand = True,
            on_hover = lambda e: self.show_search_bar(e),
            height = 60,
            bgcolor = '#081d33',
            border_radius = border_radius.only(topLeft = 15, topRight = 15),
            padding = padding.only(left = 15, right = 15),
            content = Row(
                expand = True, 
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls = [
                    self.app_header_brand(),
                    self.app_header_search(),
                    self.app_header_avatar(),
                    ],
            )
            
        )
        
            