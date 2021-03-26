from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from src.ui.home_screen import HomeScreen,MixerPopup

#define screens
    #pass

class MixerScreen(Screen):  
    pass

class WindowManager(ScreenManager):
    pass

class HomeScreenLayout(Widget):
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
       self.ids.tracks_grid.add_widget(Button(text='Track' + str(track_number)))
       #track_button = Button(text='Track ' + str(self.track_number)
    #pass

class MixerScreenLayout(Widget):
    def buttonPress(self):
        GetTrackButton.get_tracks(self)
	#pass

kv = Builder.load_file('src/ui/layouts/screens.kv')

class SonicRevolution(App):
    def build(self):
        return kv
    
    
