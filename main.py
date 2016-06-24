from kivy.app import App

from kivy.uix.pagelayout import PageLayout
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label


class Alertify(App):
    def build(self):
        main_layout = PageLayout()
        logo = Label(text = "Alertify", font_size = 20)
        main_layout.add_widget(logo)
        return main_layout

Alertify().run()
