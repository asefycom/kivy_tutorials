from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivymd.uix.behaviors.ripplebehavior import CircularRippleBehavior


Builder.load_string("""
<ExampleCustomFloatingButton@FloatLayout>:

    ItemMenuForFitness:
        source: 'leaf.png'
        size_hint: None, None
        size: dp(56), dp(56)
        pos_hint: {'center_x': .5, 'center_y': .5}
        
""")


class ItemMenuForFitness(CircularRippleBehavior, ButtonBehavior, Image):
    pass


class Example(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Factory.ExampleCustomFloatingButton()


Example().run()