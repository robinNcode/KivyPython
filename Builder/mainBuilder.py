import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('Design/style.kv')
#Builder.load_file('builder.kv')
#Builder.load_string(""" Here we can write design code """)

class KivyBuilder(Widget):
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

class Awesome(App):
    def build(self):
        return KivyBuilder()

if __name__ == '__main__':
    Awesome().run()
