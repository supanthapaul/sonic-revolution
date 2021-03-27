from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from src.audio_manager import AudioManager

class HomeScreen(Screen):
	pass

class MixerPopup(Popup):
	def confirm(self, instance):
		# Create a Mixer
		try:
			sampleRate = int(self.ids.sampleRate.text)
			amplitude = float(self.ids.amplitude.text)
			if sampleRate > 0 and amplitude > 0:
				mixer = AudioManager.instance().create_mixer(sampleRate, amplitude)
				print(AudioManager.instance().mixer)
		except:
			print("Failed to create Mixer, please provide valid inputs")
			return

		self.dismiss()
		app = App.get_running_app()
		app.root.change_screen("MixerScreen")



class HomeScreenLayout(Widget):
	pass