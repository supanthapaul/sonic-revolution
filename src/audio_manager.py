import librosa
from kivy.core.audio import SoundLoader

file_root = 'assets/sounds/'
def play_source_audio(instance):
	sound = SoundLoader.load(file_root + 'coin.wav')
	if sound:
		sound.play()
	pass

def convert_and_play(instance):
	pass