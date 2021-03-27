from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from src.track_type import get_track_type
from src.audio_manager import AudioManager
from kivy.properties import StringProperty

class MixerScreen(Screen):
	pass

class TracksList(Widget):
	#def tracks_list(self,*args):

	pass


class TrackLayout(BoxLayout):
	def open_tone_popup(self, instance):
		Factory.TonesPopup(self.id).open()
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

class TonesPopup(Popup):
	track_id = StringProperty()
	def __init__(self, track_id, **kwargs):
		super().__init__(**kwargs)
		self.track_id = track_id

	def octave_slider(self, *args):
		value = str((int(("{0}".format(args[1])))))
		self.ids.octaveSliderText.text = "Octave: " + value

	def confirm_tone(self, *args):
		# TODO: add validation
		startNote = str(self.ids.startNote.text)
		octave = int(self.ids.octaveSlider.value)
		duration = float(self.ids.duration.text)
		endNote = str(self.ids.endNote.text)
		AudioManager.instance().ee.emit("add_tone", int(self.track_id), startNote, octave, duration, endNote)
		self.dismiss()


class TonesRecycleView(RecycleView):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.data = []
		AudioManager.instance().ee.on("add_tone", self.on_add_tone)
	def on_add_tone(self, track_id, startNote, octave, duration, endNote):
		tone = AudioManager.instance().add_tone(track_id, startNote, octave, duration, endNote)
		self.data.append({'text': startNote + ' - ' + endNote + '\n' + str(duration) + 's'})
		pass

class TracksRecycleView(RecycleView):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.data = []
		AudioManager.instance().ee.on("add_track", self.on_add_track)

	def on_add_track(self, track_type, vibrato_freq, vibrato_var, attack, decay):
		print(track_type)
		tracK_id = AudioManager.instance().create_track(track_type, vibrato_freq, vibrato_var, attack, decay)
		# self.ids.scroll.add_widget(Label(text="Track id: " + str(tracK_id)))
		# print(self.ids.scroll)
		self.data.append({'id': str(tracK_id)})



class MixerScreenLayout(Widget):
	def preview_audio(self, instance):
		AudioManager.instance().preview_audio()
		pass