from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.utils import get_hex_from_color

from kivymd.uix.dialog import MDInputDialog, MDDialog
from kivymd.theming import ThemeManager


Builder.load_string('''
<ExampleDialogs@BoxLayout>
    orientation: 'vertical'
    spacing: dp(5)

    MDToolbar:
        id: toolbar
        title: app.title
        left_action_items: [['menu', lambda x: None]]
        elevation: 10
        md_bg_color: app.theme_cls.primary_color

    FloatLayout:
        MDRectangleFlatButton:
            text: "Open input dialog"
            pos_hint: {'center_x': .5, 'center_y': .7}
            opposite_colors: True
            on_release: app.show_example_input_dialog()

        MDRectangleFlatButton:
            text: "Open Ok Cancel dialog"
            pos_hint: {'center_x': .5, 'center_y': .5}
            opposite_colors: True
            on_release: app.show_example_okcancel_dialog()
''')


class Example(MDApp):
    title = "Dialogs"

    def build(self):
        return Factory.ExampleDialogs()

    def callback_for_menu_items(self, *args):
        from kivymd.toast.kivytoast import toast
        toast(args[0])

    def show_example_input_dialog(self):
        dialog = MDInputDialog(
            title='Title', size_hint=(.5, .4),
            text_button_ok='Yes',
            events_callback=self.callback_for_menu_items)
        dialog.open()

    def show_example_okcancel_dialog(self):
        dialog = MDDialog(
            title='Title', size_hint=(.8, .3), text_button_ok='Yes',
            text="Your [color=%s][b]text[/b][/color] dialog" % get_hex_from_color(
                self.theme_cls.primary_color),
            text_button_cancel='Cancel',
            events_callback=self.callback_for_menu_items)
        dialog.open()


Example().run()