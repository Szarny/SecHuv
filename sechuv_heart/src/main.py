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
    chat_history: ListProperty = ListProperty()


    def add_chat(self, chat: str) -> None:
        self.chat_history.append(chat)
        self.chat_view.text = "\n".join(self.chat_history)


    def add_master_chat(self, chat_raw: str) -> None:
        chat: str = "BOT | {}".format(chat_raw)
        self.add_chat(chat)

    
    def add_client_chat(self) -> None:
        chat_raw: str = self.input_form.text
        
        # 入力済みの内容を削除
        self.input_form.text = ""

        chat: str = "YOU | {}".format(chat_raw)
        self.add_chat(chat)

        self.generate_reply(chat_raw)

    
    def generate_reply(self, chat_raw: str) -> None:
        # TODO: 現在の状態とユーザの入力をもとにした返信を行うエンジンを実装する
        self.add_master_chat("{}なんですね．".format(chat_raw))

    
    def welcome(self) -> None:
        self.add_master_chat("こんにちは．何かお困りのことはありますか？")


 
class HeartApp(App):
    def build(self) -> BoxLayout:
        client: HeartClient = HeartClient()
        client.welcome()
        return client
 
 
if __name__ == "__main__":
    HeartApp().run()