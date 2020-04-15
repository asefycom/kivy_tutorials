from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles

KV = """
<MyTitleLabel@MDLabel>:
    halign: "center"
    font_style: "MyTitleStyle"

Screen:
    BoxLayout:
        orientation: "vertical"
        padding: dp(75)
        
        MyTitleLabel:
            text: "MDLabel"
            
        MyTitleLabel:
            text: "MDLabel"

            
        MDRectangleFlatButton:
            text: "MDRectangleFlatButton"
            font_name: "shown.ttf"
            font_size: "25sp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
"""

class MainApp(MDApp):

    def build(self):
        LabelBase.register("MyTitleFont", fn_regular="shown.ttf")
        theme_font_styles.append("MyTitleStyle")
        self.theme_cls.font_styles["MyTitleStyle"] = [
            "MyTitleFont",
            50,
            False,
            0.5,
        ]
        return Builder.load_string(KV)


MainApp().run()