from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time

def des():
    c51=Label(root,image=d1,bd=0,highlightthickness=0, relief='ridge')
    c51.place(x=200,y=275)
    c61=Label(root,image=d1,bd=0,highlightthickness=0, relief='ridge')
    c61.place(x=300,y=275)

    c71=Label(root,image=l1,bd=0,highlightthickness=0, relief='ridge')
    c71.place(x=1300,y=275)

    c81=Label(root,image=r1,bd=0,highlightthickness=0, relief='ridge')
    c81.place(x=300,y=700)

    root.after(1500,c51.destroy)
    root.after(1500,c61.destroy)
    root.after(1500,c71.destroy)
    root.after(1500,c81.destroy)
def des1():
    c2=Label(root,image=d1,bd=0,highlightthickness=0, relief='ridge')
    c2.place(x=200,y=250)
    c2=Label(root,image=d1,bd=0,highlightthickness=0, relief='ridge')
    c2.place(x=300,y=250)

    c2=Label(root,image=l1,bd=0,highlightthickness=0, relief='ridge')
    c2.place(x=1225,y=175)

    c2=Label(root,image=u1,bd=0,highlightthickness=0, relief='ridge')
    c2.place(x=1225,y=700)
    c2=Label(root,image=l1,bd=0,highlightthickness=0, relief='ridge')
    c2.place(x=1300,y=650)
    c2=Label(root,image=d1,bd=0,highlightthickness=0, relief='ridge')
    c2.place(x=1225,y=600)
    c2=Label(root,image=r1,bd=0,highlightthickness=0, relief='ridge')
    c2.place(x=1175,y=650)

    c2=Label(root,image=r1,bd=0,highlightthickness=0, relief='ridge')
    c2.place(x=275,y=700)
    root.after(500,c2.destroy())

def one():

    
    root.after(500,root.destroy)
    root.mainloop()
    two()
    
def two():
    root = tk.Tk()
    root.title("Loading...")
    root.geometry('1575x900')
    root.configure(bg = "black")
    imm=Image.open("/home/monisha/myprojects/alibiforsaken/map.png")
    rr=imm.resize((1575,900))
    filename=ImageTk.PhotoImage(rr)
    background_label = Label(root, image = filename,bg = "black")
    background_label.pack()
    h1=50
    w1=50
    i1=Image.open("/home/monisha/myprojects/alibiforsaken/steps1.png")
    u1=ImageTk.PhotoImage(i1)
    l1=ImageTk.PhotoImage(i1.rotate(angle=90))
    r1=ImageTk.PhotoImage(i1.rotate(angle=270))
    d1=ImageTk.PhotoImage(i1.rotate(angle=180))
    img2=ImageTk.PhotoImage(Image.open("/home/monisha/myprojects/alibiforsaken/steps2.png"))
    img3=ImageTk.PhotoImage(Image.open("/home/monisha/myprojects/alibiforsaken/standing.png"))

    c1=Label(root,image=u1,bd=0,highlightthickness=0, relief='ridge')
    c1.place(x=1225,y=700)
    c1=Label(root,image=l1,bd=0,highlightthickness=0, relief='ridge')
    c1.place(x=1300,y=650)
    c1=Label(root,image=d1,bd=0,highlightthickness=0, relief='ridge')
    c1.place(x=1225,y=600)
    c1=Label(root,image=r1,bd=0,highlightthickness=0, relief='ridge')
    c1.place(x=1175,y=650)

    c1=Label(root,image=d1,bd=0,highlightthickness=0, relief='ridge')
    c1.place(x=200,y=275)
    c2=Label(root,image=d1,bd=0,highlightthickness=0, relief='ridge')
    c2.place(x=300,y=275)

    c1=Label(root,image=l1,bd=0,highlightthickness=0, relief='ridge')
    c1.place(x=1300,y=275)

    c1=Label(root,image=r1,bd=0,highlightthickness=0, relief='ridge')
    c1.place(x=200,y=800)

    root.mainloop()

global filename,u1,l1,r1,d1,img2,img3
root = tk.Tk()
root.title("Loading...")
root.geometry('1575x900')
root.configure(bg = "black")
imm=Image.open("/home/monisha/myprojects/alibiforsaken/map.png")
rr=imm.resize((1575,900))
filename=ImageTk.PhotoImage(rr)
background_label = Label(root, image = filename,bg = "black")
background_label.pack()
h1=50
w1=50
i1=Image.open("/home/monisha/myprojects/alibiforsaken/steps1.png")
u1=ImageTk.PhotoImage(i1)
l1=ImageTk.PhotoImage(i1.rotate(angle=90))
r1=ImageTk.PhotoImage(i1.rotate(angle=270))
d1=ImageTk.PhotoImage(i1.rotate(angle=180))
img2=ImageTk.PhotoImage(Image.open("/home/monisha/myprojects/alibiforsaken/steps2.png"))
img3=ImageTk.PhotoImage(Image.open("/home/monisha/myprojects/alibiforsaken/standing.png"))

c1=Label(root,image=u1,bd=0,highlightthickness=0, relief='ridge')
c1.place(x=1225,y=700)
c2=Label(root,image=l1,bd=0,highlightthickness=0, relief='ridge')
c2.place(x=1300,y=650)
c3=Label(root,image=d1,bd=0,highlightthickness=0, relief='ridge')
c3.place(x=1225,y=600)
c4=Label(root,image=r1,bd=0,highlightthickness=0, relief='ridge')
c4.place(x=1175,y=650)

c5=Label(root,image=d1,bd=0,highlightthickness=0, relief='ridge')
c5.place(x=200,y=175)
c6=Label(root,image=d1,bd=0,highlightthickness=0, relief='ridge')
c6.place(x=300,y=175)

c7=Label(root,image=l1,bd=0,highlightthickness=0, relief='ridge')
c7.place(x=1300,y=175)

c8=Label(root,image=r1,bd=0,highlightthickness=0, relief='ridge')
c8.place(x=200,y=700)

root.after(1000,c5.destroy)
root.after(1000,c6.destroy)
root.after(1000,c7.destroy)
root.after(1000,c8.destroy)
root.after(500,des())





root.mainloop()

