from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import gamepad
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        
        btn1 = Button(text='NES', on_press=self.open_page)
        btn2 = Button(text='SEGA', on_press=self.open_page)
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        
        self.add_widget(layout)
    
    def open_page(self, instance):
        page_number = instance.text
        self.manager.current = page_number


class MyApp(App):
    def build(self):
        sm = ScreenManager()

        main_screen = MainScreen(name='main')
        NES= gamepad.NES('1', name='NES')
        SEGA = gamepad.SEGA('2', name='SEGA')

        sm.add_widget(main_screen)
        sm.add_widget(NES)
        sm.add_widget(SEGA)

        return sm

if __name__ == '__main__':
    MyApp().run()