import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #initialize infinite keywords
    def __init__(self, **kwargs):
        #call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        #set columns
        self.cols = 1
        # To set main grid height width
        #self.row_force_default = True,
        #self.row_default_height = 40,
        #self.col_force_default = True,
        #self.col_default_width = 200

        # Create a second widget
        self.top_grid = GridLayout(
            row_force_default = True,
            row_default_height = 40,
            col_force_default = True,
            col_default_width = 200
        )
        self.top_grid.cols = 2

        #add widgets
        self.top_grid.add_widget(Label(text = "Name : ",
         color = "yellow",
         font_size = 20
        ))
        #add input inputBox
        self.name = TextInput(multiline = True)
        self.top_grid.add_widget(self.name)

        #Second Input box starts here..........
        self.top_grid.add_widget(Label(text = "Age : ", color = "blue", font_size = 20))
        self.age = TextInput(multiline = False)
        self.top_grid.add_widget(self.age)

        #Second Input box starts here..........
        self.top_grid.add_widget(Label(text = "Favourite Color : ", color = "blue", font_size = 20))
        self.color = TextInput(multiline = True)
        self.top_grid.add_widget(self.color)

        # Add new top grid
        self.add_widget(self.top_grid)

        #Button section starts here
        self.submit = Button(text = "Submit",
         font_size = 32,
         size_hint_y = None,
         height = 50,
         size_hint_x = None,
         width = 200
        )
        # Bind the button
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)

    #Getting data
    def press(self, instance):
        name = self.name.text
        age = self.age.text
        color = self.color.text
        #print(f'Hello {name}, Your are {age} years old')
        #Let;s print the variable into screen
        self.add_widget(Label(text = f'Hello {name}, Your are {age} years old &\n your favourite color is {color}'))

        name = ""
        age = ""
        color = ""


class inputBox(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    inputBox().run()