from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import arabic_reshaper
from bidi.algorithm import get_display


class TestApp(App):
    def build(self):
        # return Label(text="English")
        text = "پارسی"
        arabic_txt = arabic_reshaper.reshape(text)
        bidi_text = get_display(arabic_txt)

        label = Label(text=bidi_text, font_name="iransans.ttf")
        btn = Button(text=bidi_text, font_name="iransans.ttf")

        box = BoxLayout(orientation="vertical")
        box.add_widget(label)
        box.add_widget(btn)

        return box


TestApp().run()