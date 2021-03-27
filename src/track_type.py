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
		"Sine": TrackType.SineWave,
		"Sawtooth": TrackType.SawtoothWave,
		"Square": TrackType.SquareWave,
		"Triangle": TrackType.TriangleWave
	}
	return switcher.get(track)