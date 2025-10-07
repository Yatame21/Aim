import random
import tkinter as tk

def hit(event):
    global score
    if not run:
        return

    items = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    if target in items:
        score += 1
        lbl_score.config(text= f"Score: {score}")
        place_target()

def place_target():
    x = random.randint(t_size, w - t_size)
    y = random.randint(t_size, h - t_size)
    canvas.coords(target, x - t_size // 2, y - t_size // 2, x+t_size // 2, y + t_size // 2)

def countdown():
    global t_left, run
    if not run:
        return

    if t_left <= 0:
        run = False
        lbl_time.config(text="Time: 0 - game over")
        return

    t_left -= 1
    lbl_time.config(text=f"Time: {t_left}")
    root.after(1000, countdown)

def start_game():
    global score, t_left, run
    score = 0
    t_left = t_limit
    run = True
    lbl_time.config(text=f"Score: {score}")
    lbl_time.config(text=f"Time: {t_left}")
    place_target()
    countdown()


w, h = 600,400
t_size = 40
t_limit = 30

root = tk.Tk()
root.title("Aim Simulator")

score = 0
t_left = t_limit

run = False

lbl_score = tk.Label(root, text=f"Score: {score}", font=("Arial", 16))
lbl_time = tk.Label(root, text=f"Time: {t_left}", font=("Arial", 16))

lbl_score.pack(side="left", padx=10)
lbl_time.pack(side="right", padx=10)

canvas = tk.Canvas(root, width=w, height=h, background="white")
canvas.pack()

target = canvas.create_oval(0,0, t_size, t_size, fill="blue", tags="target")

btn_start = tk.Button(root, text="Start", command=start_game)
btn_start.pack(pady=6)

canvas.tag_bind("target", "<Button-1>", hit)
root.mainloop()