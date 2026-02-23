from screens.menu import MainMenu
from trainers.spuares import SquaresTrainer
from trainers.random_squares import RandomSquaresTrainer
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1280x720")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.show_menu()

    # ---------- Переключение экранов ----------

    def clear(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_menu(self):
        self.clear()
        MainMenu(self.container, self)

    def show_squares(self):
        self.clear()
        SquaresTrainer(self.container, self)

    def show_randsquares(self):
        self.clear()
        RandomSquaresTrainer(self.container, self)
app = App()
app.mainloop()