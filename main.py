from kivy.app import App

from kivy.uix.pagelayout import PageLayout
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label

from kivy.uix.widget import Widget


class Alertify(App):
    def build(self):
        main_layout = PageLayout()
        logo = Label(text = "Alertify", font_size = 20)
        main_layout.add_widget(logo)
        '''layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='Hello')
        btn2 = Button(text='World')
        layout.add_widget(btn1)
        layout.add_widget(btn2)'''
        return main_layout

Alertify().run()
