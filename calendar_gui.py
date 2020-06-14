from tkinter import Tk, Frame, Label, Button
import sys
import subprocess
from pymouse import PyMouse

LIGHT_BROWN_COLOR = "#ebdbb2"   # Gruvbox color

window_width = 200
window_height = 150

mouse = PyMouse()
mouse_position = mouse.position()

mouse_x = mouse_position[0]
mouse_y = mouse_position[1]

calendar = subprocess.check_output(["cal", "-m"])
calendar = calendar.decode("utf-8")
calendar = calendar.split("\n")
calendar = [x.split() for x in calendar]

today = subprocess.check_output(["date", "+\"%d\""])
today = today.decode("utf-8")[:-1]
today = today.strip("\"")

month_year = calendar[0]
calendar_fields = [calendar[1], calendar[2], calendar[3], calendar[4], calendar[5], calendar[6]]

WINDOW_SIZE_POSITION = str(window_width) + "x" + str(window_height) + "+" + str(mouse_x - int(window_width / 2)) + "+" + str(mouse_y - window_height)

root = Tk()
root.overrideredirect(True)
root.geometry(WINDOW_SIZE_POSITION)
root.attributes("-type", "dialog")

date_label = Label(root, text=month_year, fg=LIGHT_BROWN_COLOR)
date_label.pack(side="top")

frame = Frame(root)
frame.pack()

row_count = 0
column_count = 0
for r in calendar_fields:
    for c in r:
        if c == today:
            label = Label(frame, text=c, bg=LIGHT_BROWN_COLOR, fg="black")
            label.grid(row=row_count, column=column_count)
        else:
            label = Label(frame, text=c, fg=LIGHT_BROWN_COLOR)
            label.grid(row=row_count, column=column_count)
        column_count += 1
    column_count = 0
    row_count += 1

def exit():
    sys.exit()

exit_button = Button(root, text="X", command=exit, activebackground=LIGHT_BROWN_COLOR, highlightthickness=0, highlightbackground=LIGHT_BROWN_COLOR, highlightcolor=LIGHT_BROWN_COLOR)
exit_button.pack()

root.mainloop()

