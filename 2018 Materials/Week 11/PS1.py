from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class PS1(App):
    def build(self):
        self.mylabel = Label(text = 'Programming is fun')
        self.mylabel.bind(on_touch_down = self.alternate)
        return self.mylabel

    def alternate(self, instance, touch):
        if self.mylabel.text == 'It is fun to program':
            self.mylabel.text = 'Programming is fun'
        else:
            self.mylabel.text = 'It is fun to program'
        
        return self.mylabel


if __name__== "__main__":
    PS1().run()
