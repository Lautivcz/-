import tkinter as tk


class SquaresTrainer:

    # ---------- Константы ----------
    START_NUM = 1
    FINISH_NUM = 100

    def __init__(self):
        # ---------- Переменные состояния ----------
        self.start_num = self.START_NUM
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
            text=f"{self.start_num} x {self.start_num}",
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
        if self.timer_started:
            self.check_number()
        else:
            self.start_timer()
            self.check_number()

    def check_number(self, event=None):
        try:
            if int(self.entry.get()) == self.start_num * self.start_num:
                self.start_num += 1
        except ValueError:
            pass

        self.label.config(text=f"{self.start_num} x {self.start_num}")
        self.entry.delete(0, tk.END)

    def key_pressed(self, event):
        if event.char.isdigit() or event.keysym in ["BackSpace", "Delete", "Return"]:
            return
        return "break"

    def update_timer(self):
        self.timer_started = True

        if self.start_num > self.FINISH_NUM:
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
        self.start_num = self.START_NUM
        self.timer_started = False
        self.running = False

        self.timer_label.config(text="00:00")
        self.label.config(text=f"{self.start_num} x {self.start_num}")
        self.entry.delete(0, tk.END)


# Запуск
if __name__ == "__main__":
    SquaresTrainer()