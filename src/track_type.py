import enum
from tones import SINE_WAVE, SAWTOOTH_WAVE, SQUARE_WAVE, TRIANGLE_WAVE

class TrackType(enum.Enum):
	SineWave = SINE_WAVE
	SawtoothWave = SAWTOOTH_WAVE
	SquareWave = SQUARE_WAVE
	TriangleWave = TRIANGLE_WAVE

# takes a track type string and returns TrackType
def get_track_type(track):
	switcher = {
		"Sine": SINE_WAVE,
		"Sawtooth": SAWTOOTH_WAVE,
		"Square": SQUARE_WAVE,
		"Triangle": TRIANGLE_WAVE
	}
	return switcher.get(track)