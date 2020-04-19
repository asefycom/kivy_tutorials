from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
#:import arabic_reshaper arabic_reshaper
#:import get_display bidi.algorithm.get_display
#:import MDTextFieldPersian persianuix.MDTextFieldPersian

Screen:
    BoxLayout:
        orientation: "vertical"
        padding: [0,100,0,100]
        
        MDLabel:
            text: get_display(arabic_reshaper.reshape("English پارسی"))
            halign:"center"
        
        MDRaisedButton:
            text:get_display(arabic_reshaper.reshape("دکمه پارسی"))
            pos_hint: {"center_x":0.5, "center_y":0.5}
            
        MDTextFieldPersian:
            text:get_display(arabic_reshaper.reshape("ورودی متن پارسی"))
"""


class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

TestApp().run()