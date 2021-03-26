from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget

class HomeScreen(Screen):
	pass

class MixerPopup(Popup):
	def confirm(self, instance):
		# TODO : Fucking create an actual Mixer
		self.dismiss()
		app = App.get_running_app()
		app.root.current = "MixerScreen"



class HomeScreenLayout(Widget):
	pass