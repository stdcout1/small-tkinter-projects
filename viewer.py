from tkinter import *
from PIL import ImageTk, Image
import os
images = []
cur = 0
root = Tk()
directory = r'C:\Users\nasir\Downloads'
for entry in os.scandir(directory):
    if (entry.path.endswith(".jpg")
            or entry.path.endswith(".png")) and entry.is_file():
        images.append(ImageTk.PhotoImage(Image.open(entry.path)))

label = Label(image = images[cur])
label.grid(row = 0, column = 0, columnspan = 3)

def foward():
    global label
    global cur
    global progress
    if cur+1 == len(images):
        cur = 0
    else:
        cur += 1
    label.grid_forget()
    progress.grid_forget()
    label = Label(image=images[cur])
    label.grid(row=0, column=0, columnspan=3)
    progress = Label(root, text=str(cur + 1) + " out of " + str(len(images)))
    progress.grid(row=2, column=2)
    return
def back():
    global label
    global progress
    global cur
    if cur - 1 < 0:
        cur = len(images)-1
    else:
        cur -= 1
    progress.grid_forget()
    label.grid_forget()
    progress = Label(root, text=str(cur + 1) + " out of " + str(len(images)))
    progress.grid(row=2, column=2)
    label = Label(image=images[cur])
    label.grid(row=0, column=0, columnspan=3)
    return


back = Button(root, text = "<<", command = back)
exit = Button(root, text = "CLOSE", command = root.quit)
fwd = Button(root, text = ">>", command = foward)
progress = Label(root, text = str(cur+1) + " out of " +str(len(images)))



back.grid(row = 1, column = 0)
exit.grid(row = 1, column = 1)
fwd.grid(row = 1, column = 2)
progress.grid(row = 2, column = 2 )


root.mainloop()