from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'
			on_press: app.stop()

<SettingsScreen>:
    BoxLayout:
        Label:
            text: 'Settings Screen'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

class MenuScreen(Screen):
	pass


class SettingsScreen(Screen):
	pass



class SwitchScreenApp(App):
	def build(self):
		sm=ScreenManager()
		ms=MenuScreen(name='menu')
		st=SettingsScreen(name='settings')
		sm.add_widget(ms)
		sm.add_widget(st)
		sm.current='menu'
		return sm

if __name__=='__main__':
	SwitchScreenApp().run()
