from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

import time

resource_add_path("../font")
LabelBase.register(DEFAULT_FONT, "mplus-2c-regular.ttf")
 

class HeartClient(BoxLayout):
    chat_view: ObjectProperty = ObjectProperty()
    input_form: ObjectProperty = ObjectProperty()
    chat_history: ListProperty = ListProperty()
    phase: int = 0


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
        if self.phase == 0:
            self.add_master_chat("フィッシングサイトのチェックですね．")
            self.add_master_chat("対象のWebサイトのURLを教えてください．")
            self.phase += 1
            return

        if self.phase == 1:
            self.add_master_chat("データを取得しています")
            self.add_master_chat("データを解析しています")
            self.add_master_chat("対象のWebサイトからフィッシングサイトと思わしき以下の特徴が発見されました．")
            self.add_master_chat("~~~~")
            self.add_master_chat("~~~~")
            self.add_master_chat("このサイトをデータベースに登録しますか？")
            self.phase += 1
            return

        if self.phase == 2:
            self.add_master_chat("対象のサイトをデータベースに登録しました．")



    
    def welcome(self) -> None:
        self.add_master_chat("こんにちは．何かお困りのことはありますか？")


 
class HeartApp(App):
    def build(self) -> BoxLayout:
        client: HeartClient = HeartClient()
        client.welcome()
        return client
 
 
if __name__ == "__main__":
    HeartApp().run()