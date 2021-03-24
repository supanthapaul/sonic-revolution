from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from src import audio_manager
from kivy.lang import Builder

class MainScreen(GridLayout):
	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(Label(text='Play Audio'))
		self.playBtn = Button(text="Play")
		self.playBtn.bind(on_release=audio_manager.play_source_audio)
		self.add_widget(self.playBtn)
		self.add_widget(Label(text='Convert Audio'))
		self.convertBtn = Button(text="Convert")
		self.convertBtn.bind(on_press=audio_manager.convert_and_play)
		self.add_widget(self.convertBtn)

Builder.load_file('src/testone.kv')

class Hello(Widget):
	pass
class Hey(Widget):
	pass

class TestApp(App):
	def build(self):
		return Hello()


TestApp().run()
