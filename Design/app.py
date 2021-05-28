import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    #Getting data
    def info(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        #Let's print the variable into console
        print(f'Hello {name},you like {pizza}.\nYour favourite color is {color}')


class Design(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    Design().run()