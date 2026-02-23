import tkinter as tk

class MainMenu:
  def __init__(self, parent, app):
    self.app = app

    self.frame = tk.Frame(parent)
    self.frame.pack(fill="both",expand=True)

    self.squares_btn = tk.Button(self.frame, command=self.open_squares, text="Квадраты")
    self.squares_btn.place(x=100,y=100,width=50,height=50)

    self.random_squares_btn = tk.Button(self.frame, command=self.open_randsquares, text="Рандом")
    self.random_squares_btn.place(x=150,y=100,width=50,height=50) 
  
  def open_squares(self):
    self.app.show_squares()
  def open_randsquares(self):
    self.app.show_randsquares()