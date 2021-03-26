from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from src.ui.home_screen import MixerPopup, HomeScreenLayout
from src.ui.mixer_screen import *

class WindowManager(ScreenManager):
	pass

kv = Builder.load_file('src/ui/layouts/screens.kv')

class SonicRevolution(App):
    def build(self):
        return kv


