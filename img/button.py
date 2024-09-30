from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import funct
def back_button(layout):
	back_arrow = Button(text='<-', size_hint=(0.05, 0.05))
	back_arrow.bind(on_press=funct.go_main)
	layout.add_widget(back_arrow)