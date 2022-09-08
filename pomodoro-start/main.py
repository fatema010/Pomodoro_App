from tkinter import *
import math
# CONSTANTS#

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
time = 0
timer = None

def time_reset():
    window.after_cancel(timer)
    canvas.itemconfig(add_time,text="00:00")
    top_one.config(text="Timer")
    check_mark.config(text="")
    global time
    time = 0




def time_configure():
    global time
    time += 1
    time_sec = WORK_MIN*60
    short_time_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if time%8 ==0:
        count_down(long_break_sec)
        top_one.config(text="Break",fg=RED)
    elif time%2 ==0:
        count_down(short_time_sec)
        top_one.config(text="Break",fg=PINK)
    else:
        count_down(time_sec)
        top_one.config(text="Work", fg=YELLOW)



def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec =f"0{count_sec}"

    canvas.itemconfig(add_time,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        time_configure()
        mark = ""
        mark_sessions = math.floor(time/2)
        for _ in range(mark_sessions):
            mark += "✔"
        check_mark.config(text=mark)



# UI setup:
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=GREEN)
canvas = Canvas(width=200,height=224,bg=GREEN,highlightthickness=0)
t_img = PhotoImage(file="tomato.png")

canvas.create_image(100,112,image=t_img)
add_time = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,40,"bold"))
canvas.grid(column=1,row=1)
top_one = Label(text="Timer",fg=RED,bg=GREEN,font=(FONT_NAME,50))
top_one.grid(column=1,row=0)
time_start = Button(text="Start",highlightthickness=0,command=time_configure)
time_start.grid(column=0,row=2)
time_reset =Button(text="Reset",highlightthickness=0,command=time_reset)
time_reset.grid(column=2,row=2)
check_mark = Label(fg=PINK,bg=GREEN)
check_mark.grid(column=1,row=3)






window.mainloop()