from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from src.ui.home_screen import *
from src.ui.mixer_screen import *

class WindowManager(ScreenManager):
	def change_screen(self, screen_name):
		self.current = screen_name
	pass

kv = Builder.load_file('src/ui/layouts/screens.kv')

class SonicRevolution(App):
    def build(self):
        return kv


