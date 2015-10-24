__author__ = 'benjamin'

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from ideagen import make_idea
import os

Window.size = (100, 60)

class AppThingy(GridLayout):
    def __init__(self, **kwargs):
        super(AppThingy, self).__init__(**kwargs)
        def bob(self):
            idea = make_idea()
            os.system("espeak -v mb-us1 -s 130 '" + idea + "'")
            os.system("zenity --info --title=Your\ Idea --text='" + idea + "'")

        wimg = Image(source='button.png')
        button = Button(text='', font_size=100, background_color=[1, 1, 1, 0])
        button.bind(on_press=bob)
        self.add_widget(button)
        self.add_widget(wimg)


class IdeaGenerator(App):
    def build(self):
        return AppThingy()

if __name__ == '__main__':
    IdeaGenerator().run()
