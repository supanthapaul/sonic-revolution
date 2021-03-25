from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MixerPopup(Popup):
    pass

#define screens
class HomeScreen(Screen):

    def mixerPopup(self):
        the_popup = MixerPopup()
        the_popup.open()
    #pass

class MixerScreen(Screen):
    
    def buttonPress(self):
        self.add_widget(
            Button(text='Add tones')
        )
    #pass

class WindowManager(ScreenManager):
    pass

class HomeScreenLayout(Widget):
	pass

class MixerScreenLayout(Widget):
	pass

kv = Builder.load_file('src/ui/layouts/screens.kv')

class SonicRevolution(App):
    def build(self):
        return kv
    
    
