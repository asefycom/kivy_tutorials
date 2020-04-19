'''
App demonstrating a MDTextField which accepts Persian script in KivyMD.
'''

from kivymd.app import MDApp

import arabic_reshaper
from bidi.algorithm import get_display

from kivymd.uix.textfield import MDTextField
from kivy.properties import ObjectProperty, NumericProperty, StringProperty


class MDTextFieldPersian(MDTextField):
    max_chars = NumericProperty(20)  # maximum character allowed
    str = StringProperty()

    def __init__(self, **kwargs):
        super(MDTextFieldPersian, self).__init__(**kwargs)
        self.text = get_display(arabic_reshaper.reshape(""))

    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return
        self.str = self.str+substring
        self.text = get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(MDTextFieldPersian, self).insert_text(substring, from_undo)

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = get_display(arabic_reshaper.reshape(self.str))


class MainApp(MDApp):

    def build(self):
        return MDTextFieldPersian()


if __name__ == '__main__':
    MainApp().run()