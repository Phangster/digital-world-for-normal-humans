from kivy.app import App
from kivy.uix.label import Label 

class SlideDetectApp(App):
    def build(self):
        self.mylabel = Label(text = 'slide me', font_size = 100)
        self.mylabel.bind(on_touch_move = self.detect)
        return self.mylabel
    def detect(self, instance, touch):
		#if not instance.collide_point(touch.x, touch.y):
		#	return False
        if touch.dx<-40:
            self.mylabel.text = 'slide left'
        if touch.dx>40:
            self.mylabel.text = 'slide right'
        if touch.dy<-40:
            self.mylabel.text = 'slide down'
        if touch.dy>40:
            self.mylabel.text = 'slide up'

if __name__=='__main__':
	SlideDetectApp().run()