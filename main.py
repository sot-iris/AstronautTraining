from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
import threading
import time
import random


sound = SoundLoader.load('beep_short_on.wav')
vals_list = [4]

class Game(Screen):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.answer = "random"
        self.lst = ["askdjahk", 'kajsdhka']

    def numbs(self):
        self.lst = []
        self.ids.ti.disabled = True
        while len(self.lst) < vals_list[len(vals_list)-1]:
            xy = (random.randrange(0, 9, 1))
            if str(xy) not in self.lst:
                self.lst.append(str(xy))
        self.ids.but1.disabled = True
        for i in self.lst:
            self.ids.numb.text = str(i)
            sound.play()
            time.sleep(1)
            self.ids.numb.text = " "
            time.sleep(0.2)
        self.ids.but1.disabled = False
        self.ids.ti.disabled = False

    def num_thr(self):
        threading.Thread(target=self.numbs).start()

    def check(self, text):
        self.answer = ''.join(self.lst)
        if text == self.answer[::-1]:
            self.ids.numb.text = "Correct!"
        elif len(text) == 0:
            self.ids.numb.text = "Nothing Entered"
        else:
            self.ids.numb.text = "Wrong, the answer is " + self.answer[::-1]

class Ast(Screen):
    pass

class Instructions(Screen):
    pass

class Settings_1(Screen):
    def val(self, val):
        vals_list.append(val)

class MyScreenManager(ScreenManager):
    pass


root_widget = Builder.load_string(''' 
MyScreenManager:
    Ast:
    Game:
    Settings_1:
    Instructions:

<Ast>
    name: 'first'
    BoxLayout:
        canvas.before:
            Rectangle: 
                pos: self.pos 
                size: self.size
                source: 'astron.jpg'
        orientation: "vertical"
        BoxLayout:
            orientation: "vertical"
            Label:
                text: "AstroTraining"
                color: 0, 1, 0, 1
                font_size: 100
                pos_hint: {"x": 0, "top": 1}
        Button:
            text: "Start Game"
            color: 0, 1, 0, 1
            font_size: 40
            size_hint_y: None
            height: self.parent.height * 0.111
            on_release: 
                root.manager.current = 'third'
                root.manager.transition.direction = 'left'
        Button:
            text: "Settings"
            color: 0, 1, 0, 1
            font_size: 30
            size_hint_y: None
            height: self.parent.height * 0.08
            on_release: 
                root.manager.current = 'second'
                root.manager.transition.direction = 'right'
        Button:
            text: "How to play"
            color: 0, 1, 0, 1
            font_size: 30
            size_hint_y: None
            height: self.parent.height * 0.08
            on_release: 
                root.manager.current = 'fourth'
                root.manager.transition.direction = 'right'

<Game>
    name: 'third'
    BoxLayout:
        orientation: "vertical"
        Label:
            id: numb
            font_size: 100
            text:''
        Button:
            id: but1
            text: "Generate Numbers"
            color: 0, 1, 0, 1
            font_size: 60
            size_hint_y: None
            height: self.parent.height * 0.111
            on_release: root.num_thr()
            
        BoxLayout:
            size_hint_y: None
            height: self.parent.height * 0.111
            TextInput:
                id: ti
                hint_text: "Guess here"
                font_size: 60
                input_filter: 'int'
                
            Button:
                text: "Check"
                font_size: 60
                on_press: root.check(ti.text)
        Button:
            text: "Return to main menu"
            color: 1, 1, 0, 1
            font_size: 40
            size_hint_y: None
            height: self.parent.height * 0.111
            on_release: 
                root.manager.current = 'first'
                root.manager.transition.direction = 'right' 
                
<Settings_1>
    name: 'second'
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Pick the amount of numbers to remember..."     
        Button:
            id: b4
            text: "4"
            font_size: 80
            on_release: root.val(4)
        Button:
            id: b5
            text: "5"
            font_size: 80
            on_release: root.val(5)
        Button:
            id: b6
            text: "6"
            font_size: 80
            on_release: root.val(6)
        Button:
            id: b7
            text: "7"
            font_size: 80
            on_release: root.val(7)
        Button:
            id: b8
            text: "8"
            font_size: 80
            on_release: root.val(8)
        Button:
            text: "Return to main menu"
            color: 0, 1, 0, 1
            font_size: 40
            on_release: 
                root.manager.current = 'first'
                root.manager.transition.direction = 'left'        

<Instructions>
    name: 'fourth'
    Label:
        text: "Based on [I]BBC Two - Astronauts: Do You Have What It Takes?[/I] The aim of the game is to memorise the generated numbers and recall them in reverse order. Most people can do 5. How many can you do?"
        color: 1, 1, 0, 1
        font_size: 30
        text_size: root.width, None
        size: self.texture_size               
    Button:
        text: "Return to main menu"
        color: 1, 1, 0, 1
        font_size: 40
        size_hint_y: None
        height: self.parent.height * 0.111
        on_release: 
            root.manager.current = 'first'
            root.manager.transition.direction = 'left' 
                
                ''')

class AstroApp(App):
    def build(self):
        return root_widget

if __name__ == '__main__':
    AstroApp().run()