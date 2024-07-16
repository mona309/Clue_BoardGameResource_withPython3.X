from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time
import os

def logo1():
  logo = tk.Label(root, image=g2, bg = "#f3ba4b")
  logo.place(x=750,y=400,anchor=CENTER)
  root.after(200, logo.destroy)

def logo2():
  logo = tk.Label(root, image=g3, bg = "#f3ba4b")
  logo.place(x=750,y=400,anchor=CENTER)
  root.after(200, logo.destroy)

def logo3():
  logo = tk.Label(root, image=g4, bg = "#f3ba4b")
  logo.place(x=750,y=400,anchor=CENTER)
  root.after(200, logo.destroy)

def logo4():
  logo = tk.Label(root, image=g5, bg = "#f3ba4b")
  logo.place(x=775,y=400,anchor=CENTER)
  root.after(200, logo.destroy)

def logo5():
  logo = tk.Label(root, image=g6, bg = "#f3ba4b")
  logo.place(x=775,y=400,anchor=CENTER)
  root.after(800, logo.destroy)

def displayLabel15():
  label1 = tk.Label(root, image=r2, bg = "#f3ba4b")
  label1.place(x=455,y=480)
  label2 = tk.Label(root, image=r2, bg = "#f3ba4b")
  label2.place(x=588,y=435)
  label3 = tk.Label(root, image=l2, bg = "#f3ba4b")
  label3.place(x=760,y=175)
  label4 = tk.Label(root, image=r2, bg = "#f3ba4b")
  #label4.place(x=740,y=700)
  label4.place(x = 740, y = 600)

  root.after(375,label1.destroy)
  root.after(375,label2.destroy)
  root.after(375,label3.destroy)
  root.after(375,label4.destroy)
  
def displayLabel14():
  label1 = tk.Label(root, image=r1, bg = "#f3ba4b")
  label1.place(x=419,y=480)
  label2 = tk.Label(root, image=r1, bg = "#f3ba4b")
  label2.place(x=552,y=435)
  label3 = tk.Label(root, image=l1, bg = "#f3ba4b")
  label3.place(x=796,y=175)
  label4 = tk.Label(root, image=r1, bg = "#f3ba4b")
  #label4.place(x=704,y=700)
  label4.place(x=704,y=600)

  root.after(375,label1.destroy)
  root.after(375,label2.destroy)
  root.after(375,label3.destroy)
  root.after(375,label4.destroy)

def displayLabel13():
  label1 = tk.Label(root, image=r2, bg = "#f3ba4b")
  label1.place(x=383,y=480)
  label2 = tk.Label(root, image=r2, bg = "#f3ba4b")
  label2.place(x=516,y=435)
  label3 = tk.Label(root, image=l2, bg = "#f3ba4b")
  label3.place(x=832,y=175)
  label4 = tk.Label(root, image=r2, bg = "#f3ba4b")
  #label4.place(x=668,y=700)
  label4.place(x=668,y=600)
  
  root.after(375,label1.destroy)
  root.after(375,label2.destroy)
  root.after(375,label3.destroy)
  root.after(375,label4.destroy)
  
def displayLabel12():
  label1 = tk.Label(root, image=r1, bg = "#f3ba4b")
  label1.place(x=347,y=480)
  label2 = tk.Label(root, image=r1, bg = "#f3ba4b")
  label2.place(x=480,y=435)
  label3 = tk.Label(root, image=l1, bg = "#f3ba4b")
  label3.place(x=868,y=175)
  label4 = tk.Label(root, image=r1, bg = "#f3ba4b")
  #label4.place(x=632,y=700)
  label4.place(x=632,y=600)

  root.after(375,label1.destroy)
  root.after(375,label2.destroy)
  root.after(375,label3.destroy)
  root.after(375,label4.destroy)

def displayLabel11():
  label1 = tk.Label(root, image=r2, bg = "#f3ba4b")
  label1.place(x=311,y=480)
  label2 = tk.Label(root, image=r2, bg = "#f3ba4b")
  label2.place(x=444,y=435)
  label3 = tk.Label(root, image=l2, bg = "#f3ba4b")
  label3.place(x=904,y=175)
  label4 = tk.Label(root, image=r2, bg = "#f3ba4b")
  #label4.place(x=596,y=700)
  label4.place(x=596,y=600)

  root.after(500,label1.destroy)
  root.after(500,label2.destroy)
  root.after(500,label3.destroy)
  root.after(500,label4.destroy)
  
def displayLabel10():
  label1 = tk.Label(root, image=r1, bg = "#f3ba4b")
  label1.place(x=275,y=480)
  label2 = tk.Label(root, image=r1, bg = "#f3ba4b")
  label2.place(x=408,y=435)
  label3 = tk.Label(root, image=l1, bg = "#f3ba4b")
  label3.place(x=940,y=175)
  label4 = tk.Label(root, image=r1, bg = "#f3ba4b")
  #label4.place(x=560,y=700)
  label4.place(x=560,y=600)

  root.after(500,label1.destroy)
  root.after(500,label2.destroy)
  root.after(500,label3.destroy)
  root.after(500,label4.destroy)
  
def displayLabel9():
  label1 = tk.Label(root, image=t1, bg = "#f3ba4b")
  label1.place(x=236,y=480)
  label2 = tk.Label(root, image=r2, bg = "#f3ba4b")
  label2.place(x=372,y=435)
  label3 = tk.Label(root, image=l2, bg = "#f3ba4b")
  label3.place(x=976,y=175)
  label4 = tk.Label(root, image=r2, bg = "#f3ba4b")
  #label4.place(x=524,y=700)
  label4.place(x=524,y=600)
  
  root.after(500,label1.destroy)
  root.after(500,label2.destroy)
  root.after(500,label3.destroy)
  root.after(500,label4.destroy)
  
def displayLabel8():
  label1 = tk.Label(root, image=d1, bg = "#f3ba4b")
  label1.place(x=200,y=463)
  label2 = tk.Label(root, image=t2, bg = "#f3ba4b")
  label2.place(x=336,y=435)
  label3 = tk.Label(root, image=l1, bg = "#f3ba4b")
  label3.place(x=1012,y=175)
  label4 = tk.Label(root, image=r1, bg = "#f3ba4b")
  #label4.place(x=488,y=700)
  label4.place(x=488,y=600)

  root.after(500,label1.destroy)
  root.after(500,label2.destroy)
  root.after(500,label3.destroy)
  root.after(500,label4.destroy)

def displayLabel7():
  label1 = tk.Label(root, image=d2, bg = "#f3ba4b")
  label1.place(x=200,y=427)
  label2 = tk.Label(root, image=d2, bg = "#f3ba4b")
  label2.place(x=300,y=427)
  label3 = tk.Label(root, image=l2, bg = "#f3ba4b")
  label3.place(x=1048,y=175)
  label4 = tk.Label(root, image=r2, bg = "#f3ba4b")
  #label4.place(x=452,y=700)
  label4.place(x=488,y=600)

  root.after(500,label1.destroy)
  root.after(500,label2.destroy)
  root.after(500,label3.destroy)
  root.after(500,label4.destroy)
  
def displayLabel6():
  label1 = tk.Label(root, image=d1, bg = "#f3ba4b")
  label1.place(x=200,y=391)
  label2 = tk.Label(root, image=d1, bg = "#f3ba4b")
  label2.place(x=300,y=391)
  label3 = tk.Label(root, image=l1, bg = "#f3ba4b")
  label3.place(x=1084,y=175)
  label4 = tk.Label(root, image=r1, bg = "#f3ba4b")
  #label4.place(x=416,y=700)
  label4.place(x=416,y=600)
  
  root.after(500,label1.destroy)
  root.after(500,label2.destroy)
  root.after(500,label3.destroy)
  root.after(500,label4.destroy)

def displayLabel5():
  label1 = tk.Label(root, image=d2, bg = "#f3ba4b")
  label1.place(x=200,y=355)
  label2 = tk.Label(root, image=d2, bg = "#f3ba4b")
  label2.place(x=300,y=355)
  label3 = tk.Label(root, image=l2, bg = "#f3ba4b")
  label3.place(x=1120,y=175)
  label4 = tk.Label(root, image=r2, bg = "#f3ba4b")
  #label4.place(x=380,y=700)
  label4.place(x=380,y=600)

  root.after(500,label1.destroy)
  root.after(500,label2.destroy)
  root.after(500,label3.destroy)
  root.after(500,label4.destroy)
  
def displayLabel4():
  label1 = tk.Label(root, image=d1, bg = "#f3ba4b")
  label1.place(x=200,y=319)
  label2 = tk.Label(root, image=d1, bg = "#f3ba4b")
  label2.place(x=300,y=319)
  label3 = tk.Label(root, image=l1, bg = "#f3ba4b")
  label3.place(x=1156,y=175)
  label4 = tk.Label(root, image=r1, bg = "#f3ba4b")
  #label4.place(x=344,y=700)
  label4.place(x=344,y=600)

  root.after(500,label1.destroy)
  root.after(500,label2.destroy)
  root.after(500,label3.destroy)
  root.after(500,label4.destroy)
  
def displayLabel3():
  label1 = tk.Label(root, image=d2, bg = "#f3ba4b")
  label1.place(x=200,y=283)
  label2 = tk.Label(root, image=d2, bg = "#f3ba4b")
  label2.place(x=300,y=283)
  label3 = tk.Label(root, image=l2, bg = "#f3ba4b")
  label3.place(x=1192,y=175)
  label4 = tk.Label(root, image=r2, bg = "#f3ba4b")
  #label4.place(x=308,y=700)
  label4.place(x=308,y=600)

  root.after(500,label1.destroy)
  root.after(500,label2.destroy)
  root.after(500,label3.destroy)
  root.after(500,label4.destroy)
  
def displayLabel2():
  label1 = tk.Label(root, image=d1, bg = "#f3ba4b")
  label1.place(x=200,y=247)
  label2 = tk.Label(root, image=d1, bg = "#f3ba4b")
  label2.place(x=300,y=247)
  label3 = tk.Label(root, image=l1, bg = "#f3ba4b")
  label3.place(x=1228,y=175)
  label4 = tk.Label(root, image=r1, bg = "#f3ba4b")
  #label4.place(x=272,y=700)
  label4.place(x=272,y=600)

  root.after(500,label1.destroy)
  root.after(500,label2.destroy)
  root.after(500,label3.destroy)
  root.after(500,label4.destroy)
  
def displayLabel1():
  label1 = tk.Label(root, image=d2, bg = "#f3ba4b")
  label1.place(x=200,y=211)
  label2 = tk.Label(root, image=d2, bg = "#f3ba4b")
  label2.place(x=300,y=211)
  label3 = tk.Label(root, image=l2, bg = "#f3ba4b")
  label3.place(x=1264,y=175)
  label4 = tk.Label(root, image=r2, bg = "#f3ba4b")
  #label4.place(x=236,y=700)
  label4.place(x=236,y=600)
  
  root.after(500,label1.destroy)
  root.after(500,label2.destroy)
  root.after(500,label3.destroy)
  root.after(500,label4.destroy)

def next_pg():
  root.destroy()
  os.startfile("avatar.py")
  
# Create the main window
root = tk.Tk()
root.title("Loading-Page...")
root.geometry('2000x1000')
root.configure(bg = "black")

Label(text = "", font = ("Calibri 5"), bg = "black").pack()
c = Canvas(root, height = 25, width = 50)
imm=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\map.png")
#rr=imm.resize((1575,900))
rr=imm.resize((1500,750))
filename=ImageTk.PhotoImage(rr)
background_label = Label(root, image = filename,bg = "black").pack()


image_path1 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\steps1.png"
img1 = Image.open(image_path1)
img1 = ImageTk.PhotoImage(img1)

i1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\steps1.png")
u1=ImageTk.PhotoImage(i1)
l1=ImageTk.PhotoImage(i1.rotate(angle=90))
r1=ImageTk.PhotoImage(i1.rotate(angle=270))
d1=ImageTk.PhotoImage(i1.rotate(angle=180))
t1=ImageTk.PhotoImage(i1.rotate(angle=225))

i2=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\steps2.png")
u2=ImageTk.PhotoImage(i2)
l2=ImageTk.PhotoImage(i2.rotate(angle=90))
r2=ImageTk.PhotoImage(i2.rotate(angle=270))
d2=ImageTk.PhotoImage(i2.rotate(angle=180))
t2=ImageTk.PhotoImage(i1.rotate(angle=225))

i3=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\standing.png")
u3=ImageTk.PhotoImage(i3)
l3=ImageTk.PhotoImage(i3.rotate(angle=90))
r3=ImageTk.PhotoImage(i3.rotate(angle=270))
d3=ImageTk.PhotoImage(i3.rotate(angle=180))

i4=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\logo4.png")
lg1=i4.resize((266,200))
lg2=i4.resize((333,250))
lg3=i4.resize((466,350))
lg4=i4.resize((665,500))
#lg5=i4.resize((998,750))
lg5=i4.resize((1000,600))
lg6=i4.resize((1275,700))
g1=ImageTk.PhotoImage(lg1)
g2=ImageTk.PhotoImage(lg2)
g3=ImageTk.PhotoImage(lg3)
g4=ImageTk.PhotoImage(lg4)
g5=ImageTk.PhotoImage(lg5)
g6=ImageTk.PhotoImage(lg6)

c1=Label(root,image=u3,bd=0,highlightthickness=0, relief='ridge')
#c1.place(x=1225,y=725)
c1.place(x=1175,y=600)
c2=Label(root,image=l3,bd=0,highlightthickness=0, relief='ridge')
#c2.place(x=1300,y=650)
c2.place(x=1250,y=525)
c3=Label(root,image=d3,bd=0,highlightthickness=0, relief='ridge')
#c3.place(x=1225,y=575)
c3.place(x=1175,y=450)
c4=Label(root,image=r3,bd=0,highlightthickness=0, relief='ridge')
#c4.place(x = 1150, y=650)
c4.place(x=1100,y=525)

label1 = tk.Label(root, image=d1, bg = "#f3ba4b")
label1.place(x=200,y=175)
label2 = tk.Label(root, image=d1, bg = "#f3ba4b")
label2.place(x=300,y=175)
label3 = tk.Label(root, image=l1, bg = "#f3ba4b")
label3.place(x=1300,y=175)
label4 = tk.Label(root, image=r1, bg = "#f3ba4b")
label4.place(x=200,y=600)

root.after(500, label1.destroy)
root.after(500, label2.destroy)
root.after(500, label3.destroy)
root.after(500, label4.destroy)
root.after(500, displayLabel1)
root.after(1000, displayLabel2)
root.after(1500, displayLabel3)
root.after(2000, displayLabel4)
root.after(2500, displayLabel5)
root.after(3000, displayLabel6)
root.after(3500, displayLabel7)
root.after(4000, displayLabel8)
root.after(4500, displayLabel9)
root.after(5000, displayLabel10)
root.after(5500, displayLabel11)

root.after(6000, c1.destroy)
root.after(6000, c2.destroy)
root.after(6000, c3.destroy)
root.after(6000, c4.destroy)

logo = tk.Label(root, image=g1, bg = "#f3ba4b")
logo.place(x=750,y=400,anchor=CENTER)

root.after(6000, logo.destroy)

root.after(6200, logo1)
root.after(6400, logo2)
root.after(6600, logo3)
root.after(6800, logo4)
root.after(7000, logo5)

root.after(7500, next_pg)
root.mainloop()
