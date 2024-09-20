from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy .uix.colorpicker import ColorPicker
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class ColorPickerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.color_picker = ColorPicker()
        layout.add_widget(self.color_picker)
        self.label = Label(text='Select a color')
        layout.add_widget(self.label)
        self.color_picker.bind(color=self.on_color)
        return layout

    def on_color(self, instance, value):
        self.label.text = 'Selected color: ' + str(value)
        with self.label.canvas.before:
            Color(*value)
            Rectangle(pos=self.label.pos, size=self.label.size)

if __name__ == '__main__':
    ColorPickerApp().run()