import tkinter as tk
from trainers.spuares import SquaresTrainer

class MainMenu:
  def __init__(self):
    self.menu = tk.Tk()
    self.menu.geometry("500x500")

    self.squares_btn = tk.Button(self.menu, command=SquaresTrainer, text="Квадраты")
    self.squares_btn.place(x=100,y=100,width=50,height=50)

    self.menu.mainloop()
  