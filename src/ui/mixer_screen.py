from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class MixerScreen(Screen):
	pass

class TracksList(Widget):
	pass

#class TrackButton(Button):
    #pass

class TracksGrid(Widget):
    pass

class TracksPopup(Popup):
    def vibrato_frequency_slider(self, *args):
        value = str((float(("{0:.1f}".format(args[1])))))
        self.ids.vibratoFrequencySlider.text = "Vibrato frequency: " + value 

    def vibrato_variance_slider(self, *args):
        value = str((float(("{0:.1f}".format(args[1])))))
        self.ids.vibratoVarianceSlider.text = "Vibrato variance: " + value 

    def attack_slider(self, *args):
        value = str((float(("{0:.3f}".format(args[1])))))
        self.ids.attackSlider.text = "Attack: " + value 
    
    def decay_slider(self, *args):
        value = str((float(("{0:.2f}".format(args[1])))))
        self.ids.decaySlider.text = "Decay: " + value
    #pass

class GetTrackButton(Button):
    track_number = 1
    def get_tracks(self):
       self.track_number += 1
       self.ids.tracks_grid.add_widget(Button(text='Track' + str(self.track_number)))
       #track_button = Button(text='Track ' + str(self.track_number)
    #pass

class MixerScreenLayout(Widget):
    def buttonPress(self):
        GetTrackButton.get_tracks(self)
	#pass