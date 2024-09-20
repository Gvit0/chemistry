from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.colorpicker import ColorWheel
from kivy.graphics import Color, Rectangle
from DM import DataModule as DatModul

class ColorPickerApp(App):
    def build(self):

        self.colorM = DatModul.load(None,'main.conf','colorBG',[1,1,1,1])
        self.color = self.colorM[0],self.colorM[1],self.colorM[2],self.colorM[3]
        layout = BoxLayout(orientation='vertical')
        self.color_wheel = ColorWheel()
        layout.add_widget(self.color_wheel)
        self.label = Label(text='Выбор цвета')
        layout.add_widget(self.label)
        self.color_wheel.bind(color=self.on_color)
        self.color_wheel.color = self.color
        return layout

    def on_color(self, instance, value):
        with self.label.canvas.before:
            Color(*value)
            Rectangle(pos=self.label.pos, size=self.label.size)
        Window.clearcolor = value  # Set the background color of the entire application
        DatModul.save(None,'main.conf','colorBG',list(value))
if __name__ == '__main__':
    ColorPickerApp().run()