from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
FloatLayout:
    orientation: "vertical"

    MDBottomAppBar:

        MDToolbar:
            icon: "plus"
            type: "bottom"
            mode: "free-end"
            elevation: 10
            left_action_items: [["menu", lambda x: x]]


    MDLabel:
        text: "I am in a boxlayout along with a toolbar."
        halign: "center"
'''


class TestToolbar(MDApp):

    def build(self):
        return Builder.load_string(KV)


TestToolbar().run()