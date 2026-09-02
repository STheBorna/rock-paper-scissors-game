class Player:
    def __init__(self):
        self.player_choose=None
    def get_choose(self,choose)->None:
        self.player_choose = choose

class Computer:
    def __init__(self):
        self.choose=None
    def select_choose(self,RPS_lst)->None:
        import random
        new_choice = random.choice(RPS_lst)
        self.choose=new_choice

class Score:
    def __init__(self):
        self.scores={
            "player_score":0,
            "computer_score":0
        }
        self.draw_counts=0
    def increase_points(self,which_player_point)->None:
        self.scores[which_player_point]+=1

class Game:
    def __init__(self):
        self.player= Player()
        self.computer=Computer()
        self.score=Score()
    def start(self):
        self.computer.select_choose()
        computer_choice=self.computer.choose

import tkinter as tk
class Game_UI:
    def __init__(self, title, w, h):
        self.title = title
        self.w = w
        self.h = h
        self.window = tk.Tk()
        self.setup_window()
    def setup_window(self):
        self.window.title(self.title)
        self.window.geometry(f"{self.w}x{self.h}")
    def run(self):
        self.window.mainloop()
