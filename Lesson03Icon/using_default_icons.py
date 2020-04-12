from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
Screen:
    MDFillRoundFlatIconButton:
        icon: "login"
        text: "Login"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
"""


class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)


MainApp().run()