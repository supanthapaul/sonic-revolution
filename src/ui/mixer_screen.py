from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

class MixerScreen(Screen):
	pass

class TracksList(Widget):
	pass

#class TrackButton(Button):
    #pass

class TracksGrid(Widget):
    pass

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