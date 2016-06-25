from twilio.rest import TwilioRestClient
from kivy.app import App

from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.button import Button

def view_Contacts(obj):
    #App proceeds to next page
    pass

'''
(From the twilio program)
function to send out alerts to the destination
'''
def send_Alert(obj):
    account_sid = "ACbb4b9650631364e99781ded800fa9699" 
    auth_token = "0a068601c149167e134887defd6fc2a9" 
    client = TwilioRestClient("ACbb4b9650631364e99781ded800fa9699", \
                          "0a068601c149167e134887defd6fc2a9")
    client.messages.create(to="+19176671977", from_="+16464193165",
                                     body="Hello Jia~!")
    return

def to_setting(obj):
    pass

class AlertifyApp(App):
    def build(self):
        App_header = BoxLayout(orientation = "vertical")
        logo = Label(text = "Alertify", font_size = 80)
        
        add_button = Button(text = "Add")
        add_button.bind(on_press = view_Contacts)
        
        alert_button = Button(text = "Alert")
        alert_button.bind(on_press = send_Alert)
        
        
        setting_button = Button(text = "Setting")
        alert_button.bind(on_press = to_setting)
        
        App_header.add_widget(logo)
        App_header.add_widget(add_button)
        App_header.add_widget(alert_button)
        App_header.add_widget(setting_button)
        return App_header

AlertifyApp().run()
