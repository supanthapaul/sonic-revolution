import enum
from tones import SINE_WAVE, SAWTOOTH_WAVE, SQUARE_WAVE, TRIANGLE_WAVE

class TrackType(enum.Enum):
	SineWave = SINE_WAVE
	SawtoothWave = SAWTOOTH_WAVE
	SquareWave = SQUARE_WAVE
	TriangleWave = TRIANGLE_WAVE