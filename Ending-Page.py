from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import time

# Create the main window
root = tk.Tk()
root.title("Ending-Page...")
root.geometry('2000x1000')
root.configure(bg = "black")

def update_frame1():
  global current_frame1, frames1
  frame1 = frames1[current_frame1]
  label1.configure(image=frame1)
  current_frame1 = (current_frame1 + 1) % len(frames1)
  label1.after(delay, update_frame1)

def update_frame2():
  global current_frame2, frames2
  label2.place(x = 200, y = 110)
  frame2 = frames2[current_frame2]
  label2.configure(image=frame2)
  current_frame2 = (current_frame2 + 1) % len(frames2)
  label2.after(delay, update_frame2)

def update_frame3():
  global current_frame3, frames3
  label3.place(x = 1245, y = 110)
  frame3 = frames3[current_frame3]
  label3.configure(image=frame3)
  current_frame3 = (current_frame3 + 1) % len(frames3)
  label3.after(delay, update_frame3)

def update_frame4():
  global current_frame4, frames4
  label4.place(x = 1175, y = 565)
  frame4 = frames4[current_frame4]
  label4.configure(image=frame4)
  current_frame4 = (current_frame4 + 1) % len(frames4)
  label4.after(delay, update_frame4)

def update_frame5():
  global current_frame5, frames5
  label5.place(x = 675, y = 300)
  frame5 = frames5[current_frame5]
  label5.configure(image=frame5)
  current_frame5 = (current_frame5 + 1) % len(frames5)
  label5.after(delay_steps, update_frame5)

def update_frame6():
  global current_frame6, frames6
  label6.place(x = 500, y = 275)
  frame6 = frames6[current_frame6]
  label6.configure(image=frame6)
  current_frame6 = (current_frame6 + 1) % len(frames6)
  label6.after(delay_logo, update_frame6)

def update_frame7():
  global current_frame7, frames7
  label7.place(x = 525, y = 275)
  frame7 = frames7[current_frame7]
  label7.configure(image=frame7)
  current_frame7 = (current_frame7 + 1) % len(frames7)
  label7.after(delay_end, update_frame7)
 
Label(text = "", font = ("Calibri 5"), bg = "black").pack()
c = Canvas(root, height = 25, width = 50)
img=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\map.png")
res_img=img.resize((1500,750))
filename=ImageTk.PhotoImage(res_img)
background_label = Label(root, image = filename,bg = "black").pack()


gif_path1 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\up.gif"
gif1 = Image.open(gif_path1)
frames1 = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif1)]

current_frame1 = 0
label1 = tk.Label(root, image=frames1[current_frame1],bg = "#f3ba4b")
label1.place(x = 200, y = 500)

delay = 500
update_frame1()
root.after(1505,lambda:label1.destroy())

gif_path2 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\right.gif"
gif2 = Image.open(gif_path2)
frames2 = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif2)]

current_frame2 = 0
label2 = tk.Label(root, image=frames2[current_frame2],bg = "#f3ba4b")
label2.place_forget()
delay = 500

root.after(1510, lambda:update_frame2())
root.after(3001,lambda:label2.destroy())

gif_path3 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\down.gif"
gif3 = Image.open(gif_path3)
frames3 = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif3)]

current_frame3 = 0
label3 = tk.Label(root, image=frames3[current_frame3],bg = "#f3ba4b")
label3.place_forget()
delay = 500

update_frame3()
root.after(1505,lambda:label3.destroy())

gif_path4 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\left.gif"
gif4 = Image.open(gif_path4)
frames4 = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif4)]

current_frame4 = 0
label4 = tk.Label(root, image=frames4[current_frame4],bg = "#f3ba4b")
label4.place_forget()
delay = 500

root.after(1510, lambda:update_frame4())
root.after(3001,lambda:label4.destroy())

gif_path5 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\steps.gif"
gif5 = Image.open(gif_path5)
frames5 = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif5)]

current_frame5 = 0
label5 = tk.Label(root, image=frames5[current_frame5],bg = "#f3ba4b")
label5.place_forget()
delay_steps = 50

root.after(3010, lambda:update_frame5())
root.after(4750,lambda:label5.destroy())

gif_path6 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\ALIBI FORSAKEN.gif"
gif6 = Image.open(gif_path6)
frames6 = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif6)]

current_frame6 = 0
label6 = tk.Label(root, image=frames6[current_frame6],bg = "#f3ba4b")
label6.place_forget()
delay_logo = 25

root.after(4800, lambda:update_frame6())
root.after(6890,lambda:label6.destroy())

gif_path7 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\THE END.gif"
gif7 = Image.open(gif_path7)
frames7 = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif7)]

current_frame7 = 0
label7 = tk.Label(root, image=frames7[current_frame7],bg = "#f3ba4b")
label7.place_forget()
delay_end = 1000

root.after(6895, lambda:update_frame7())
root.after(8000,lambda:label7.destroy())
root.after(8001,lambda:root.destroy())

root.mainloop()
