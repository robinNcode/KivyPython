import kivy
from kivy.app import App
from kivy.uix.label import Label

class HelloKivy(App):
    def build(self):
        return Label(text = "This the 1st kivy app \n Hello Kivy",
         font_size = 40,
          color = "blue")

if __name__ == '__main__':
    HelloKivy().run()