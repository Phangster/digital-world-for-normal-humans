from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 

class MyLabel(Label):
	def __init__(self,**kwargs):
		Label.__init__(self,**kwargs)
		self.bind(size=self.setter('text_size'))
		self.padding=(20,20)

class Investment(App):

	def build(self):
		layout= GridLayout(cols=2)

		l1=MyLabel(text="Investment Ammount",font_size=24,halign='left',valign='middle')
		layout.add_widget(l1)

		self.t1 = TextInput()
		layout.add_widget(self.t1)

		l2=MyLabel(text="Years",font_size=24,halign='left',valign='middle')
		layout.add_widget(l2)

		self.t2 = TextInput()
		layout.add_widget(self.t2)

		l3=MyLabel(text="Annual Interest Rate",font_size=24,halign='left',valign='middle')
		layout.add_widget(l3)

		self.t3 = TextInput()
		layout.add_widget(self.t3)

		self.l4=MyLabel(text="Future Value",font_size=24,halign='left',valign='middle')
		layout.add_widget(self.l4)

		self.txt_future_val=MyLabel(text="",font_size=24,halign='left',valign='middle')
		layout.add_widget(self.txt_future_val)

		btn = Button(text="Calculate", on_press=self.calculate, font_size=24)
		layout.add_widget(btn)

		return layout 

	def calculate(self, instance):
		inv_amt = float(self.t1.text)
		years = float(self.t2.text)
		mth_int_rate = float(self.t3.text) / 12/100
		self.txt_future_val.text= str(round(inv_amt*(1+mth_int_rate)**(years*12), 2))
		print (str(inv_amt*(1+mth_int_rate)**(years*12)))



Investment().run()