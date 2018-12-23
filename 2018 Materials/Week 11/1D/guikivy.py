from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder	
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.app import App
from firebase import firebase

url= 'https://digital-world-cohort-11.firebaseio.com/'
token = '5eucPr4baUntEEeJ8RHrkHmYLdwUGLCKF5yQb7Fg' 
firebase=firebase.FirebaseApplication(url,token)


kv_str = """
<GuiKivy>:
	#these set the variables defined within the Gridlayout
	red_button:red
	GridLayout:
		cols: 2
		Label:
			text: 'Yellow LED'
		Button:
			id:yellow
			text: 'off'
			on_press: root.update_yellow() #the root here references the Investment class
		Label:
			text: 'Red LED'
		Button:
			id: red
			text: 'off'
			on_press: root.update_red() #the root here references the Investment class
"""

class GuiKivy(Screen):
	Builder.load_string(kv_str) #this builds the string as a kivy file
	firebase.put('/', 'yellow', False)
	firebase.put('/', 'red', False)

	#the convention is to put graphics and text within kvlang and logic and functions within python
	def update_yellow(self):
		if self.ids.yellow.text == 'off':
			self.ids.yellow.text = 'on'
			firebase.put('/', 'yellow', True)
			self.ids.yellow.background_color = [0,0,1,1]
		elif self.ids.yellow.text == 'on':
			self.ids.yellow.text = 'off'
			firebase.put('/', 'yellow', False)
			self.ids.yellow.background_color = [1,1,1,1]

	def update_red(self):
		if self.red_button.text == 'off':
			self.red_button.text = 'on'
			firebase.put('/', 'red', True)
			self.red_button.background_color = [0,0,1,1]
		elif self.red_button.text == 'on':
			self.red_button.text = 'off'
			firebase.put('/', 'red', False)
			self.red_button.background_color = [1,1,1,1]


class SwitchScreenApp(App):
	def build(self):
		sm=ScreenManager()
		ms=GuiKivy(name='menu')
		sm.add_widget(ms)
		sm.current='menu'
		return sm


if __name__=='__main__':
	SwitchScreenApp().run()