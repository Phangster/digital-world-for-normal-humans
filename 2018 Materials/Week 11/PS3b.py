from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder	
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.app import App

kv_str = """
<Investment>: #investment class
	#these set the variables defined within the Gridlayout
	inv_amt: inv_amt
	years: years
	mth_int_rate: mth_int_rate
	txt_future_val: txt_future_val

	GridLayout:
		cols: 2
		Label:
			text: 'Investment Amount'
		TextInput:
			id: inv_amt
		Label:
			text: 'Years'
		TextInput:
			id: years
		Label:
			text: 'Annual Interest Rate'
		TextInput:
			id: mth_int_rate
		Label:
			text: 'Future Value'
		Label:
			id: txt_future_val
			text: '-'
		Button:
			id:cbut
			text: 'Calculate'
			on_press: root.calculate() #the root here references the Investment class
		Button:
			text: 'Quit'
			on_press: app.stop()
"""



class Investment(Screen):
	Builder.load_string(kv_str) #this builds the string as a kivy file
	
	#the convention is to put graphics and text within kvlang and logic and functions within python
	def calculate(self):
		inv_amt = float(self.inv_amt.text)
		years = float(self.years.text)
		mth_int_rate = float(self.mth_int_rate.text) / 12/100
		self.txt_future_val.text= str(round(inv_amt*(1+mth_int_rate)**(years*12), 2))
		print (str(inv_amt*(1+mth_int_rate)**(years*12)))


class SwitchScreenApp(App):
	def build(self):
		sm=ScreenManager()
		ms=Investment(name='menu')
		sm.add_widget(ms)
		sm.current='menu'
		return sm


if __name__=='__main__':
	SwitchScreenApp().run()
