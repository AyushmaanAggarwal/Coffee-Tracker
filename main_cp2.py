from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar, MDBottomAppBar
from kivymd.app import MDApp

class ConverterApp(MDApp):

    # Build Functions necessary for code
    def new(self):
        pass

    def build(self):

        screen = MDScreen()
        
        self.toolbar2 = MDBottomAppBar()
        self.toolbar2.icon = "add"
        self.toolbar2.type = "bottom"
        self.toolbar2.left_action_items= [["menu", lambda x: x]]

        # state
        self.ctof = True
        self.theme_cls.primary_palette = "Indigo"

        # toolbar
        #self.toolbar = MDToolbar(title="Coffee Log")
        #self.toolbar.pos_hint = {"top": 1}
        #self.toolbar.right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
        #screen.add_widget(self.toolbar)

        # logo

        self.logo = Image(source="logo.jpg", pos_hint={"center_x": 0.5, "center_y": 0.7}, width=50, size_hint_y=None)
        screen.add_widget(self.logo)

        # input

        #self._input = MDTextField(
        #    hint_text="Enter temperature in Celsius",
        #    halign="center",
        #    size_hint=(0.8, 1),
        #    pos_hint={"center_x": 0.5, "center_y": 0.5},
        #    font_size=22
        #)
        #screen.add_widget(self._input)

        # labels

        #self.label = MDLabel(
        #    halign="center",
        #    pos_hint={"center_x": 0.5, "center_y": 0.35},
        #    theme_text_color="Secondary"
        #)

        #self.converted_label = MDLabel(
        #    halign="center",
        #    pos_hint={"center_x": 0.5, "center_y": 0.3},
        #    theme_text_color="Primary",
        #    font_style="H5"
        #)

        #screen.add_widget(self.label)
        #screen.add_widget(self.converted_label)

        # convert button

        #self.convert_button = MDFillRoundFlatButton(
        #    text="CONVERT",
        #    font_size=17,
        #    pos_hint={"center_x": 0.5, "center_y": 0.15},
        #    on_press=self.convert
        #)

        #screen.add_widget(self.convert_button)

        return screen


if __name__ == '__main__':

    ConverterApp().run()

