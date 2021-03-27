import librosa
from tones.mixer import Mixer
from kivy.core.audio import SoundLoader
from pymitter import EventEmitter
from src.track_type import TrackType

class AudioManager:
	__instance__ = None

	def __init__(self):
		if AudioManager.__instance__ is None:
			AudioManager.__instance__ = self
			# create event emitter
			self.ee = EventEmitter()
		else:
			raise Exception("You cannot create another AudioManager class")

	# method to access sigleton
	@staticmethod
	def instance():
		if not AudioManager.__instance__:
			AudioManager()
		return AudioManager.__instance__

	def create_mixer(self, sample_rate, amplitude):
		self.mixer = Mixer(sample_rate, amplitude)
		self.curr_track_id = 0
		return self.mixer

	def create_track(self, track_type, vibrato_freq, vibrato_variance, attack, decay):
		if not self.mixer:
			print("You need to create a Mixer first")
			return

		# if not isinstance(track_type, TrackType):
		# 	raise TypeError('track_type must be an instance of TrackType Enum')
		# create track
		self.mixer.create_track(self.curr_track_id, track_type, vibrato_frequency=vibrato_freq, vibrato_variance=vibrato_variance, attack=attack, decay=decay)
		# increment current track id
		self.curr_track_id += 1
		# return id of this track
		return self.curr_track_id - 1
	def add_tone(self, track_id, startNote, octave, duration, endNote):
		self.mixer.add_note(track_id, note=startNote, octave=octave, duration=duration, endnote=endNote)
		return (startNote, octave, duration, endNote)
	def preview_audio(self):
		self.mixer.write_wav('temp.wav')
		sound = SoundLoader.load('temp.wav')
		if sound:
			sound.play()



file_root = 'assets/sounds/'
def play_source_audio(instance):
	sound = SoundLoader.load(file_root + 'coin.wav')
	if sound:
		sound.play()
	pass

def convert_and_play(instance):
	pass