from kivy.app import App
from kivy.uix.label import Label

class ShopApp(App):
    def build(self):
        return Label(text="Hello Kivy Shop!", font_size=40)

if __name__ == '__main__':
    ShopApp().run()
