import librosa
from tones.mixer import Mixer
from tones import SINE_WAVE, SAWTOOTH_WAVE, SQUARE_WAVE, TRIANGLE_WAVE
from kivy.core.audio import SoundLoader
import enum

class AudioManager:
	__instance__ = None

	def __init__(self):
		if AudioManager.__instance__ is None:
			AudioManager.__instance__ = self
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

	def create_track(self, track_type, vibrato_freq, vibrato_variance, attack, decay):
		if not self.mixer:
			print("You need to create a Mixer first")
			return

		if not isinstance(track_type, TrackType):
			raise TypeError('track_type must be an instance of TrackType Enum')
		# create track
		self.mixer.create_track(self.curr_track_id, track_type, vibrato_frequency=vibrato_freq, vibrato_variance=vibrato_variance, attack=attack, decay=decay)
		# increment current track id
		self.curr_track_id += 1


class TrackType(enum.Enum):
	SineWave = SINE_WAVE
	SawtoothWave = SAWTOOTH_WAVE
	SquareWave = SQUARE_WAVE
	TriangleWave = TRIANGLE_WAVE

file_root = 'assets/sounds/'
def play_source_audio(instance):
	sound = SoundLoader.load(file_root + 'coin.wav')
	if sound:
		sound.play()
	pass

def convert_and_play(instance):
	pass