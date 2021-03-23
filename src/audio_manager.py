from pysndfx import AudioEffectsChain
import librosa
from kivy.core.audio import SoundLoader

fx = (
    AudioEffectsChain().reverb()
)
file_root = 'assets/sounds/'
def play_source_audio(instance):
	sound = SoundLoader.load(file_root + 'coin.wav')
	if sound:
		sound.play()
	pass

def convert_and_play(instance):
	y, sr = librosa.load(file_root + 'coin.wav', sr=None)
	x = fx(y)
	# new_audio = fx(y)
	# librosa.output.write_wav(file_root + 'coin_2.wav', new_audio, sr)
	# sound = SoundLoader.load(file_root + 'coin_proc.ogg')
	# if sound:
	# 	sound.play()
	pass