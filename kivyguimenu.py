import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
buttons = [
    {'name': "Меню1", 'class': 'menu1'},
    {'name': "Меню2", 'class': 'menu2'},
]
class MenuPage(Screen):
    def __init__(self, name, **kwargs):
        super(MenuPage, self).__init__(**kwargs)
        self.name = name
        layout = BoxLayout(orientation='vertical')
        button = Button(text=name, size_hint=(1, 0.2))
        layout.add_widget(button)
        self.add_widget(layout)

class MyApp1(App):
    def build(self):
        sm = ScreenManager()
        
        for button in buttons:
            page = MenuPage(button['class'])
            sm.add_widget(page)
            btn = Button(text=button['name'], size_hint=(1, 0.1))

            btn.bind(on_press=lambda _:exec(f"sm.current_screen={button['class']}"))
            layout = BoxLayout(orientation='vertical')
            layout.add_widget(btn)
            root = Screen()
            root.add_widget(layout)
            sm.add_widget(root)
        return sm
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        layout = BoxLayout(orientation='vertical')
        for button in buttons:
            #page = MenuPage(button['class'])
            #sm.add_widget(page)
            btn = Button(text=button['name'], size_hint=(1, 0.1))

            btn.bind(on_press=lambda btn, button=button: print(button['class']))
            
            layout.add_widget(btn)
        root = Screen()
        root.add_widget(layout)
        sm.add_widget(root)
        return sm
if __name__ == '__main__':
    MyApp().run()