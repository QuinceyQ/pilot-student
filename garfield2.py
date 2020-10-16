from time import sleep
from termcolor import colored

class Bot():
    wait = 1
    def __init__(self):
        self.q = ""
        self.a = ""
    def _think(self, s):
        return s
    def _format(self, s):
        return colored(s, 'blue')
    def run(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        self.a = input()
        sleep(Bot.wait)
        print(self._format(self._think(self.a)))

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

class HelloBot(Bot):
    def __init__(self):
        self.q = "Hi, what is your name?"
    def _think(self, s):
        return f'Hello, {s}'

from simpleeval import simple_eval
class ComputBot(Bot):
    def __init__(self):
        self.q = 'Through recent upgrade I can do calculation now. Input some arithmetic expression to try:'
    def _think(self, s):
        result = simple_eval(s)
        return f'Done. Result is {result}'

garfield = Garfield()
garfield.add(HelloBot())
garfield.add(ComputBot())
garfield.run()        