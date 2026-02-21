import tkinter as tk

# ----------------- Константы -----------------
START_NUM = 1
FINISH_NUM = 100

# ----------------- Глобальные переменные -----------------
start_num = START_NUM
milliseconds = 0
running = False
timer_started = False

# ----------------- Функции -----------------

def combo(event=None):
    """Вызывается при нажатии Enter или кнопки"""
    if timer_started:
        check_number()
    else:
        start_timer()
        check_number()


def check_number(event=None):
    """Проверка введенного числа"""
    global start_num
    try:
        if int(entry.get()) == start_num * start_num:
            start_num += 1
    except ValueError:
        pass  # если введено пустое или не число
    label.config(text=f"{start_num} x {start_num}")
    entry.delete(0, tk.END)


def key_pressed(event):
    """Ограничение ввода только цифрами, BackSpace и Delete"""
    if event.char.isdigit() or event.keysym in ["BackSpace", "Delete", "Return"]:
        return
    return "break"


def update_timer():
    """Обновление таймера"""
    global milliseconds, running, timer_started
    timer_started = True

    if start_num > FINISH_NUM:
        stop_timer()
        label.config(text="Игра закончена")
        return

    if running:
        milliseconds += 1  # считаем секунды
        minutes = milliseconds // 60
        seconds = milliseconds % 60
        timer_label.config(text=f"{minutes:02}:{seconds:02}")

        win.after(1000, update_timer)


def start_timer():
    """Запуск таймера"""
    global running
    if not running:
        running = True
        update_timer()


def stop_timer():
    """Остановка таймера"""
    global running
    running = False


def reset_game():
    """Сброс игры"""
    global milliseconds, start_num, timer_started
    milliseconds = 0
    start_num = START_NUM
    timer_started = False
    timer_label.config(text="00:00")
    label.config(text=f"{start_num} x {start_num}")
    entry.delete(0, tk.END)

# ----------------- GUI -----------------

win = tk.Tk()
win.title("Игра с квадратами")
win.geometry("700x700")
win.resizable(width=False, height=False)

# Привязка Enter
win.bind("<Return>", combo)

# Лейблы
label = tk.Label(win, text=f"{start_num} x {start_num}", bg="gray", font=("Arial", 55))
label.place(x=100, y=50, width=500, height=200)

timer_label = tk.Label(win, text="00:00", bg="gray", font=("Arial", 70))
timer_label.place(x=100, y=500, width=500, height=200)

# Entry
entry = tk.Entry(win, font=("Arial", 100))
entry.focus()
entry.bind("<Key>", key_pressed)
entry.place(x=100, y=250, width=350, height=100)

# Кнопка
start_btn = tk.Button(win, text="Enter", command=combo, bg="red", width=20, height=20)
start_btn.place(x=450, y=250, width=150, height=100)

# Кнопка сброса
reset_btn = tk.Button(win, text="Reset", command=reset_game, bg="red", width=20, height=20)
reset_btn.place(x=450, y=350, width=150, height=100)

win.mainloop()