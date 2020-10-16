import time
class Bot:
    wait = 1
    def __init__(self):
        self.q = ""
        self.a = ""
    def _think(self, s):
        return s
    def run(self):
        time.sleep(Bot.wait)
        print(self.q)
        self.a = input()
        time.sleep(Bot.wait)
        print(self._think(self.a))

class HelloBot(Bot):
    def __init__(self):
        self.q = "Hi, what is your name?"
    def _think(self, s):
        return f'Hello, {s}'

class FeelingBot(Bot):
    def __init__(self):
        self.q = 'how are you today?'
    def _think(self, s):
        if 'good' in s.lower() or 'fine' in s.lower():
            return "I'm feeling good too"
        else:
            return "Sorry to hear that"

import random
class ColorBot(Bot):
    def __init__(self):
        self.q = 'what is your favorite color?'
    
    def _think(self, s):
        choice_color = ['red', 'yellow', 'white', 'green', 'gray']
        return f"your favorite color is {s}, and my favorite color is {random.choice(choice_color)}"

class Garfield:
    
    def __init__(self):
        self.bots = []        
    def add(self, bot):
        self.bots.append(bot)
    def _prompt(self, s):
        print(s)
        print()
    def run(self):
        self._prompt("This is Garfield dialog system. Let's talk.")
        for bot in self.bots:
            bot.run()      
                  
#创建一个聊天延时ls的对话系统
garfield = Garfield()
#向其中加入我们已经定义好的各个对话bot的对象实例
garfield.add(HelloBot())
garfield.add(FeelingBot())
garfield.add(ColorBot())
#运行
garfield.run()