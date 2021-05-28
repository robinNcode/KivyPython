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
        self.cols = 2

        #add widgets
        self.add_widget(Label(text = "Name : ", color = "yellow", font_size = 20))
        #add input inputBox
        self.name = TextInput(multiline = True)
        self.add_widget(self.name)

        #Second Input box starts here..........
        self.add_widget(Label(text = "Age : ", color = "blue", font_size = 20))
        self.age = TextInput(multiline = False)
        self.add_widget(self.age)

        #Button section starts here
        self.submit = Button(text = "Submit", font_size = 40)
        # Bind the button
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)

    #Getting data
    def press(self, instance):
        name = self.name.text
        age = self.age.text
        #print(f'Hello {name}, Your are {age} years old')
        #Let;s print the variable into screen
        self.add_widget(Label(text = f'Hello {name}, Your are {age} years old'))

        name = ""
        age = ""


class inputBox(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    inputBox().run()