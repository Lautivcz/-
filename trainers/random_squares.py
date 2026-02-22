import tkinter as tk
import random

class RandomSquaresTrainer:

    # ---------- Константы ----------
    

    def __init__(self):
        # ---------- Переменные состояния ----------
        self.create_numbers()
        self.milliseconds = 0
        self.running = False
        self.timer_started = False

        # ---------- GUI ----------
        self.win = tk.Tk()
        self.win.title("Игра с квадратами")
        self.win.geometry("700x700")
        self.win.resizable(False, False)

        self.win.bind("<Return>", self.combo)

        self.label = tk.Label(
            self.win,
            text=f"{self.numbers[0]} x {self.numbers[0]}",
            bg="gray",
            font=("Arial", 55)
        )
        self.label.place(x=100, y=50, width=500, height=200)

        self.timer_label = tk.Label(
            self.win,
            text="00:00",
            bg="gray",
            font=("Arial", 70)
        )
        self.timer_label.place(x=100, y=500, width=500, height=200)

        self.entry = tk.Entry(self.win, font=("Arial", 100))
        self.entry.place(x=100, y=250, width=350, height=100)
        self.entry.focus()
        self.entry.bind("<Key>", self.key_pressed)

        self.start_btn = tk.Button(
            self.win,
            text="Enter",
            command=self.combo,
            bg="red"
        )
        self.start_btn.place(x=450, y=250, width=150, height=100)

        self.reset_btn = tk.Button(
            self.win,
            text="Reset",
            command=self.reset_game,
            bg="red"
        )
        self.reset_btn.place(x=450, y=350, width=150, height=100)

        self.win.mainloop()

    # ---------- Логика ----------
    def combo(self, event=None):
        if not self.running:
            self.start_timer()
        self.check_number()

    def check_number(self, event=None):
        try:
            if int(self.entry.get()) == self.numbers[0] * self.numbers[0]:
                self.next_number()
        except ValueError:
            pass

        self.label.config(text=f"{self.numbers[0]} x {self.numbers[0]}")
        self.entry.delete(0, tk.END)

    def key_pressed(self, event):
        if event.char.isdigit() or event.keysym in ["BackSpace", "Delete", "Return"]:
            return
        return "break"

    def update_timer(self):
        self.timer_started = True

        if not self.numbers:
            self.stop_timer()
            self.label.config(text="Игра закончена")
            return

        if self.running:
            self.milliseconds += 1
            minutes = self.milliseconds // 60
            seconds = self.milliseconds % 60
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")

            self.win.after(1000, self.update_timer)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop_timer(self):
        self.running = False

    def reset_game(self):
        self.milliseconds = 0
        self.timer_started = False
        self.running = False

        self.timer_label.config(text="00:00")
        self.label.config(text=f"{self.numbers[0]} x {self.numbers[0]}")
        self.entry.delete(0, tk.END)
        self.create_numbers
    def create_numbers(self,start=1,finish=100):
        self.numbers = list(range(start,finish))
        random.shuffle(self.numbers)

    def next_number(self):
        if self.numbers:
          self.numbers.pop(0)
          return self.numbers.pop(0)
        else:
            return None
# Запуск
if __name__ == "__main__":
    RandomSquaresTrainer()