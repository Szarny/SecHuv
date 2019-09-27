from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path


resource_add_path("../font")
LabelBase.register(DEFAULT_FONT, "mplus-2c-regular.ttf")
 

class HeartClient(BoxLayout):
    chat_view: ObjectProperty = ObjectProperty()
    input_form: ObjectProperty = ObjectProperty()
    chat_ref_list: ListProperty = ListProperty()
 
 
    def send_chat(self) -> None:
        self.chat_ref_list.append(self.input_form.text)
        self.input_form.text = ""
        self.chat_view.text = "\n".join(self.chat_ref_list)

 
class HeartApp(App):
    def build(self) -> BoxLayout:
        client: HeartClient = HeartClient()
        return client
 
 
if __name__ == "__main__":
    HeartApp().run()