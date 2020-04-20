from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

KV = """
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: header.height
         
        Image:
            id: header
            source:"hamruyesh.png"
            size_hint: None, None
            size: "64dp","64dp"
            
    MDLabel:
        text: "HamRuyesh"
        size_hint_y: None
        font_style:"H6"
        height: self.texture_size[1]
        
    ScrollView:
        MDList:
            OneLineIconListItem:
                text: "Go to Screen 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "screen 1"
                IconLeftWidget:
                    icon:"folder"
                
            OneLineIconListItem:
                text: "Go to Screen 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "screen 2"
                IconLeftWidget:
                    icon:"folder"

Screen:
    MDToolbar:
        title: "HamRuyesh"
        pos_hint: {"top": 1}
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        
    MDBottomAppBar:

        MDToolbar:
            icon: "plus"
            type: "bottom"
            elevation: 10
            left_action_items: [["home", lambda x: x]]
            right_action_items: [["magnify", lambda x: x]]
            
    NavigationLayout:
        ScreenManager:
            id: screen_manager
            Screen:
                name: "screen 1"
                MDLabel:
                    text: "Screen 1"
                    halign: "center"


            Screen:
                name: "screen 2"
                MDLabel:
                    text: "Screen 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer
            
            ContentNavigationDrawer:
                nav_drawer: nav_drawer
                screen_manager: screen_manager
                
                
    
"""


class ContentNavigationDrawer(BoxLayout):
    nav_drawer = ObjectProperty()
    screen_manager = ObjectProperty()


class TestNavDraw(MDApp):
    def build(self):
        return Builder.load_string(KV)

TestNavDraw().run()