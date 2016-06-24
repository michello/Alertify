from kivy.app import App

from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.button import Button


class Alertify(App):
    def build(self):
        App_header = BoxLayout(orientation = "vertical")
        logo = Label(text = "Alertify", font_size = 80)
        add_button = Button(text = "Add")
        alert_button = Button(text = "Alert")
        App_header.add_widget(logo)
        App_header.add_widget(add_button)
        App_header.add_widget(alert_button)
        return App_header

Alertify().run()
