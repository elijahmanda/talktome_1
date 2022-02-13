from kivy.lang import Builder
from kivymd.app import MDApp
from plyer import tts
import random




class TalkToMe(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

    def talk(self, *args):
        speach_list = ["hello i'm your personal AI assistant", "Elijah made me", "you can count on me", "i got you"]
        tts.speak(speach_list[random.randint(0,2)])
        
TalkToMe().run()
