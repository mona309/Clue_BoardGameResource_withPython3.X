from tkinter import *
from PIL import Image,ImageTk
import os

def b0():
    root0.destroy()
    cardc1()

def b1():
    root1.destroy()
    cardc2()

def b2():
    root2.destroy()
    cardc3()

def b3():
    root3.destroy()
    display()

def a():
    print(123)

def display():
    global root0
    root0=Tk()
    root0.config(bg='black')
    #c=PhotoImage(file="/home/monisha/myprojects/alibiforsaken/card.png")
    root0.geometry('1575x900')
    c1 = Canvas(root0, height = 25, width = 50)
    t=PhotoImage(file="/home/monisha/myprojects/alibiforsaken/table.png")
    image=Image.open("/home/monisha/myprojects/alibiforsaken/card.png")
    ri=image.resize((78,128))
    c=ImageTk.PhotoImage(ri)
    background_label = Label(root0, image = t)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c1.pack()
    h1=130
    w1=80
    h2=1
    w2=1
    y1=230
    y2=380
    y3=530

    C1=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i1=C1.create_image(h2,w2,image=c,anchor=NW)
    C1.place(x=350,y=y1)
    C2=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i2=C2.create_image(h2,w2,image=c,anchor=NW)
    C2.place(x=450,y=y1)
    C3=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i3=C3.create_image(h2,w2,image=c,anchor=NW)
    C3.place(x=550,y=y1)
    C4=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i4=C4.create_image(h2,w2,image=c,anchor=NW)
    C4.place(x=650,y=y1)
    C5=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i5=C5.create_image(h2,w2,image=c,anchor=NW)
    C5.place(x=750,y=y1)
    C6=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i6=C6.create_image(h2,w2,image=c,anchor=NW)
    C6.place(x=850,y=y1)


    C7=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i7=C7.create_image(h2,w2,image=c,anchor=NW)
    C7.place(x=350,y=y2)
    C8=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i8=C8.create_image(h2,w2,image=c,anchor=NW)
    C8.place(x=450,y=y2)
    C9=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i9=C9.create_image(h2,w2,image=c,anchor=NW)
    C9.place(x=550,y=y2)
    C10=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i10=C10.create_image(h2,w2,image=c,anchor=NW)
    C10.place(x=650,y=y2)
    C11=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i11=C11.create_image(h2,w2,image=c,anchor=NW)
    C11.place(x=750,y=y2)
    C12=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i3=C12.create_image(h2,w2,image=c,anchor=NW)
    C12.place(x=850,y=y2)
    C13=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i13=C13.create_image(h2,w2,image=c,anchor=NW)
    C13.place(x=950,y=y2)
    C14=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i14=C14.create_image(h2,w2,image=c,anchor=NW)
    C14.place(x=1050,y=y2)
    C15=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i15=C15.create_image(h2,w2,image=c,anchor=NW)
    C15.place(x=1150,y=y2)


    C16=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i16=C16.create_image(h2,w2,image=c,anchor=NW)
    C16.place(x=350,y=y3)
    C17=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i17=C17.create_image(h2,w2,image=c,anchor=NW)
    C17.place(x=450,y=y3)
    C18=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i18=C18.create_image(h2,w2,image=c,anchor=NW)
    C18.place(x=550,y=y3)
    C19=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i19=C19.create_image(h2,w2,image=c,anchor=NW)
    C19.place(x=650,y=y3)
    C20=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i20=C20.create_image(h2,w2,image=c,anchor=NW)
    C20.place(x=750,y=y3)
    C21=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i21=C21.create_image(h2,w2,image=c,anchor=NW)
    C21.place(x=850,y=y3)
    C22=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i22=C22.create_image(h2,w2,image=c,anchor=NW)
    C22.place(x=950,y=y3)
    C23=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i23=C23.create_image(h2,w2,image=c,anchor=NW)
    C23.place(x=1050,y=y3)
    C24=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i24=C24.create_image(h2,w2,image=c,anchor=NW)
    C24.place(x=1150,y=y3)


    bt=Button(root0,text="back",command=b0).place(x=1500,y=100)
    root0.mainloop()

def cardc1():
    
    global root1
    root1=Tk()
    root1.config(bg='black')
    c=PhotoImage(file="/home/monisha/myprojects/alibiforsaken/card.png")
    root1.geometry('1575x900')
    c1 = Canvas(root1, height = 25, width = 50)
    t=PhotoImage(file="/home/monisha/myprojects/alibiforsaken/tableb.png")
    background_label = Label(root1, image = t)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c1.pack()
    Label(root1,text="Choose the weapon card",background=root1["bg"],foreground='white',font=("Arial",18)).place(x=700,y=130)
    B1=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=a)
    B1.place(x=320,y=190,relheight=0.28)
    B2=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0)
    B2.place(x=520,y=190,relheight=0.28)
    B3=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0)
    B3.place(x=720,y=190,relheight=0.28)
    B4=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0)
    B4.place(x=920,y=190,relheight=0.28)
    B5=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0)
    B5.place(x=1120,y=190,relheight=0.28)
    B6=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0)
    B6.place(x=420,y=460,relheight=0.28)
    B7=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0)
    B7.place(x=620,y=460,relheight=0.28)
    B8=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0)
    B8.place(x=820,y=460,relheight=0.28)
    B9=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0)
    B9.place(x=1020,y=460,relheight=0.28)
    bt=Button(root1,text="back",command=b1).place(x=1500,y=100)
    root1.mainloop()

def cardc2():
    global root2
    root2=Tk()
    root2.geometry('1400x788')
    root2.config(bg='black')
    t=PhotoImage(file="/home/monisha/myprojects/alibiforsaken/tableb.png")
    c=PhotoImage(file="/home/monisha/myprojects/alibiforsaken/card.png")
    Label(root2,image=t).pack()
    Label(root2,text="Choose the place card",background=root2["bg"],foreground='white',font=("Arial",18)).place(x=600,y=70)
    B1=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=220,y=130)
    B2=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=420,y=130)
    B3=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=620,y=130)
    B4=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=820,y=130)
    B5=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=1020,y=130)
    B6=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=320,y=400)
    B7=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=520,y=400)
    B8=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=720,y=400)
    B9=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=920,y=400)
    bt=Button(root2,text="back",command=b2).place(x=1200,y=100)
    root2.mainloop()

def cardc3():
    global root3
    root3=Tk()
    root3.config(bg='black')
    root3.geometry('1400x788')
    t=PhotoImage(file="/home/monisha/myprojects/alibiforsaken/tableb.png")
    c=PhotoImage(file="/home/monisha/myprojects/alibiforsaken/card.png")
    Label(root3,image=t).pack()
    Label(root3,text="Choose the weapon card",background=root3["bg"],foreground='white',font=("Arial",18)).place(x=600,y=70)
    B1=Button(root3,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=420,y=130)
    B2=Button(root3,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=620,y=130)
    B3=Button(root3,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=820,y=130)
    B4=Button(root3,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=420,y=400)
    B5=Button(root3,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=620,y=400)
    B6=Button(root3,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0).place(x=820,y=400)
    bt=Button(root3,text="back",command=b3).place(x=1200,y=100)
    root3.mainloop()

display()