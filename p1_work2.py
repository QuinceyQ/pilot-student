#作业一：改进最后这个 CalcBot，让它可以反复执行，用户可以一直输入算术表达式求值，直到用户输入 x q exit 或者 quit 为止，才跳到下一个 bot 执行。
#提示：这个需求改变了 run() 方法的基本流程，所以需要在 CalcBot 中重新实现一个 run() 方法，覆盖掉父类中 run() 的实现；
# 也可以通过修改父类 Bot 实现，但要注意，不要影响已经完成的功能。

from time import sleep
from termcolor import colored

class Bot():
    wait = 1
    def __init__(self):
        self.q = ""
        self.a = ""
        self.runtype = "once"
        self.term = ""
    def _think(self, s):
        return s
    def _format(self, s):
        return colored(s, 'blue')

    def _once_run(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        self.a = input()
        sleep(Bot.wait)
        print(self._format(self._think(self.a)))

    def _loop_run(self):
        while True:
            sleep(Bot.wait)
            print(self._format(self.q))
            self.a = input()
            if self.a.lower() in self.term:
                break
            sleep(Bot.wait)
            print(self._format(self._think(self.a)))

    def run(self):
        if 'once' in self.runtype.lower():
            self._once_run()
        else:
            self._loop_run()



class HelloBot(Bot):
    def __init__(self):
        self.q = "Hi, what is your name?"
        self.runtype = 'once'
    def _think(self, s):
        return f'Hello, {s}'


import random
class ColorBot(Bot):
    def __init__(self):
        self.q = 'what is your favorite color?'
        self.runtype = 'once'
    def _think(self, s):
        choice_color = ['red', 'yellow', 'white', 'green', 'gray']
        return f"your favorite color is {s}, and my favorite color is {random.choice(choice_color)}"


from simpleeval import simple_eval
class CalcBot(Bot):
    def __init__(self):
        self.q = 'Through recent upgrade I can do calculation now. Input some arithmetic expression to try:'
        self.runtype = 'loop'
        self.term = ['quit', 'x q exit']
    def _think(self, s):
        if  isinstance(s, str):
            result = simple_eval(s)
            return f'Done. Result is {result}'
        else:
            return 'please input valid equation'

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



garfield = Garfield()
garfield.add(HelloBot())
garfield.add(CalcBot())
garfield.add(ColorBot())
garfield.run()

