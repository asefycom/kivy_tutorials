from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast import toast

KV = """
Screen:
    MDRectangleFlatButton:
        text: "Toaster"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        on_release:
            app.show_toast()
"""


class TestToast(MDApp):
    def show_toast(self):
        toast("HamRuyesh.com", 3.0)

    def build(self):
        self.theme_cls.primary_palette="Indigo"
        return Builder.load_string(KV)


TestToast().run()