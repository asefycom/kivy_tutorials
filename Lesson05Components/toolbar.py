from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast import toast

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "I am a Toolbar!"
        md_bg_color: app.theme_cls.accent_color
        specific_text_color: app.theme_cls.primary_color
        elevation: 10
        left_action_items: [["menu", lambda x: x]]
        right_action_items: [["magnify", lambda x: app.callback_search()], ["share-variant", lambda x: app.callback_share()]]


    MDLabel:
        text: "I am in a boxlayout along with a toolbar."
        halign: "center"
'''


class TestToolbar(MDApp):

    def callback_search(self):
        toast("Searching", 2.0)

    def callback_share(self):
        toast("Share something", 1.0)

    def build(self):
        return Builder.load_string(KV)


TestToolbar().run()