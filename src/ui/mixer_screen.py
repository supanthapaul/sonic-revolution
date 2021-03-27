from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from src.track_type import get_track_type
from src.audio_manager import AudioManager

class MixerScreen(Screen):
	pass

class TracksList(Widget):
	#def tracks_list(self,*args):

	pass

#class TrackButton(Button):
    #pass

class TracksGrid(Widget):
	pass

class TracksPopup(Popup):
	#track_number = 1
	def vibrato_frequency_slider(self, *args):
		value = str((float(("{0:.1f}".format(args[1])))))
		self.ids.vibratoFrequencySliderText.text = "Vibrato frequency: " + value

	def vibrato_variance_slider(self, *args):
		value = str((float(("{0:.1f}".format(args[1])))))
		self.ids.vibratoVarianceSliderText.text = "Vibrato variance: " + value

	def attack_slider(self, *args):
		value = str((float(("{0:.3f}".format(args[1])))))
		self.ids.attackSliderText.text = "Attack: " + value

	def decay_slider(self, *args):
		value = str((float(("{0:.2f}".format(args[1])))))
		self.ids.decaySliderText.text = "Decay: " + value

	def confirm_track(self, *args):
		track_type = get_track_type(self.ids.trackType.text)
		vibrato_freq = float(self.ids.vibratoFrequencySlider.value)
		vibrato_var = float(self.ids.vibratoVarianceSlider.value)
		attack = float(self.ids.attackSlider.value)
		decay = float(self.ids.decaySlider.value)
		# Emit add track event
		AudioManager.instance().ee.emit("add_track", track_type, vibrato_freq, vibrato_var, attack, decay)
		print("track confirm")
		self.dismiss()
    #pass

class GetTrackButton(Button):
	#track_number = 1
	#def get_tracks(self):
			#self.track_number += 1
			#self.ids.tracks_grid.add_widget(Button(text='Track' + str(self.track_number)))
			#track_button = Button(text='Track ' + str(self.track_number)
	pass

class TracksRecycleView(RecycleView):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		print("RECYCLEVIEW INITIALIZED")
		self.data = []
		AudioManager.instance().ee.on("add_track", self.on_add_track)

	def on_add_track(self, track_type, vibrato_freq, vibrato_var, attack, decay):
		print(track_type)
		tracK_id = AudioManager.instance().create_track(track_type, vibrato_freq, vibrato_var, attack, decay)
		# self.ids.scroll.add_widget(Label(text="Track id: " + str(tracK_id)))
		# print(self.ids.scroll)
		self.data.append({'text': "Track id:" + str(tracK_id)})



class MixerScreenLayout(Widget):


	def buttonPress(self):
			GetTrackButton.get_tracks(self)
	#pass