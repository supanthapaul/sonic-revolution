from kivymd.app import MDApp
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

#kv = Builder.load_file('src/ui/layouts/screens.kv')
#Red, Pink, Purple, DeepPurple, Indigo
#Blue, LightBlue, Cyan, Teal, Green
#LightGreen, Lime, Yellow, Amber, Orange
#DeepOrange, Brown, Gray, BlueGray

class SonicRevolution(MDApp):
	def build(self):
		#self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "LightBlue"
		self.theme_cls.primary_hue = "400"
		self.theme_cls.accent_palette = "Purple"
		self.root_widget = Builder.load_file('src/ui/layouts/screens.kv')
		return self.root_widget


