from twilio.rest import TwilioRestClient
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.button import Button

Builder.load_string("""
<HomeScreen>:
	BoxLayout:
		orientation: "vertical"
		Image:
			size_hint_y: None
			height: root.height/2
			width: root.width/2
			source: "logo.png"
		Button:
			text: "View Contact"
			color: 0,0,0,1
			font_size:35
			pos_hint: {"x":.2, "y":.2}
			size_hint: .6 , .5
			background_color: 250,245,0,0.7
			on_press: root.manager.current = 'contacts'
		Button:
			text: "Alert"
			color: 0,0,0,1
			font_size: 35
			pos_hint: {"x":.2, "y":.2}
			size_hint: .6 , .5
			background_color: 250,245,0,0.7
			on_press: root.send_Alert()
		Button:
			text: "Setting"
			color: 0,0,0,1
			font_size: 35
			pos_hint: {"x":.2, "y":.2}
			size_hint: .6 , .5
			background_color: 250,245,0,0.7
			on_press: root.manager.current = 'settings'
	
<ContactScreen>:
	BoxLayout:
		orientation: "vertical"
		Button:
		Button:
<SettingScreen>:
	BoxLayout:
		Button:
		Button:
""")

# Set up the screens
class HomeScreen(Screen):
    '''
    (From the twilio program)
    function to send out alerts to the destination
    '''
    def send_Alert(self, *args):
        account_sid = "ACbb4b9650631364e99781ded800fa9699" 
        auth_token = "0a068601c149167e134887defd6fc2a9" 
        client = TwilioRestClient("ACbb4b9650631364e99781ded800fa9699", \
                              "0a068601c149167e134887defd6fc2a9")
        client.messages.create(to="+19176671977", from_="+16464193165",
                                         body="Hello Jia~!")
        return

class ContactScreen(Screen):
    pass

class SettingScreen(Screen):
    curr_radius = "0"
    def update_radius(self, *args):
        pass

# Add the screens
sm = ScreenManager()
sm.add_widget(HomeScreen(name = "home"))
sm.add_widget(ContactScreen(name = "contacts"))
sm.add_widget(SettingScreen(name = "setting"))

#The functions to switch screen to "contacts"
def view_Contacts(obj):
    #App proceeds to next page
    pass

# Function to switch screen to "functions"
def to_setting(obj):
    pass


class AlertifyApp(App):
    def build(self):
        return sm

AlertifyApp().run()
