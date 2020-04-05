from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

KV = """
Screen:
    MDRectangleFlatButton:
        text: "[color=#00ffcc]Hello Material[/color]"
        markup: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        text_color: app.theme_cls.accent_color
        md_bg_color: 1, 0, 1, 1
"""

class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark" #"Light"
        self.theme_cls.accent_palette = "Blue"
        self.theme_cls.primary_hue = "900"
        return Builder.load_string(KV)


MainApp().run()