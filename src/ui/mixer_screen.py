from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

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
        #do shit
        #track_number += 1
        print("track confirm")
        #self.parent.ids.tracks_grid.add_widget(Label(text='asdasd'))
        #MixerScreenLayout.add_widget(Button(text='heallo'))
        self.dismiss()
    #pass

class GetTrackButton(Button):
    #track_number = 1
    #def get_tracks(self):
       #self.track_number += 1
       #self.ids.tracks_grid.add_widget(Button(text='Track' + str(self.track_number)))
       #track_button = Button(text='Track ' + str(self.track_number)
    pass

class MixerScreenLayout(Widget):
    def buttonPress(self):
        GetTrackButton.get_tracks(self)
	#pass