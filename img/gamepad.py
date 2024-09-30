from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import button
class NES(Screen):
    def __init__(self, page_number, **kwargs):
        super(NES, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        
        label = Label(text=f'Page {page_number} деньги на карту')
        back_arrow = Button(text='<-', size_hint=(0.05, 0.05))
        back_arrow.bind(on_press=self.go_back)
        
        layout.add_widget(back_arrow)
        layout.add_widget(label)
        self.add_widget(layout)
    
    def go_back(self, instance):
        self.manager.current = 'main'
class SEGA(Screen):
    def __init__(self, page_number, **kwargs):
        super(SEGA, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        
        label = Label(text=f'Page {page_number} SEGA')
        layout.add_widget(label)
        button.back_button(layout)