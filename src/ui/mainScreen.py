from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.popup import Popup

class MixerPopup(Popup):
    pass

#define screens
class FirstWindow(Screen):
    
    def mixerPopup(self):
        the_popup = MixerPopup()
        the_popup.open()
    #pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('layouts/layout.kv')

class SonicRevolution(App):
    def build(self):
        return kv

SonicRevolution().run()