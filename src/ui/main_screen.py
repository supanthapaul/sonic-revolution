from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

Builder.load_file('layouts/first_window_layout.kv')

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

#kv = Builder.load_file('layouts/main_screen.kv')
class main_screen(Widget):
		pass

class SonicRevolution(App):
    def build(self):
        return main_screen()

SonicRevolution().run()