from tkinter import *
from PIL import Image,ImageTk
import os
import random

def b0():
    root0.destroy()
    cardc1() 

def b2():
    root2.destroy()
    cardc3()

def b3():
    root3.destroy()
    display()

def shuffle(a):
    random.shuffle(a)
    return a

'''def an(x,b,c):
    global murder_weapon
    murder_weapon=x.cget('textvariable')
    print(murder_weapon)
    root1.destroy()
    cardc2(b,c)'''

def a(x=0):
    murder_set.append(x)
    root1.destroy()
    cardc2()

def b(x=0):
    murder_set.append(x)
    root2.destroy()
    cardc3()

def d(x=0):
    murder_set.append(x)
    print(murder_set)
    root3.destroy()
    disp()

def display():
    global root0
    root0=Tk()
    root0.config(bg='black')
    #c=PhotoImage(file="/home/monisha/myprojects/alibiforsaken/card.png")
    #root0.geometry('1575x900')
    root0.geometry('2000x1000')
    root0.title('Selection Page')
    c = Canvas(root0, height = 25, width = 50)
    t=PhotoImage(file="C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\table.png")

    image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\19.png")
    ri1=image1.resize((78,128))
    c1=ImageTk.PhotoImage(ri1)
    image2=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\20.png")
    ri2=image2.resize((78,128))
    c2=ImageTk.PhotoImage(ri2)
    image3=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\21.png")
    ri3=image3.resize((78,128))
    c3=ImageTk.PhotoImage(ri3)
    image4=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\22.png")
    ri4=image4.resize((78,128))
    c4=ImageTk.PhotoImage(ri4)
    image5=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\23.png")
    ri5=image5.resize((78,128))
    c5=ImageTk.PhotoImage(ri5)
    image6=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\24.png")
    ri6=image6.resize((78,128))
    c6=ImageTk.PhotoImage(ri6)

    image7=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\1.png")
    ri7=image7.resize((78,128))
    c7=ImageTk.PhotoImage(ri7)
    image8=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\2.png")
    ri8=image8.resize((78,128))
    c8=ImageTk.PhotoImage(ri8)
    image9=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\3.png")
    ri9=image9.resize((78,128))
    c9=ImageTk.PhotoImage(ri9)
    image10=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\4.png")
    ri10=image10.resize((78,128))
    c10=ImageTk.PhotoImage(ri10)
    image11=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\5.png")
    ri11=image11.resize((78,128))
    c11=ImageTk.PhotoImage(ri11)
    image12=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\6.png")
    ri12=image12.resize((78,128))
    c12=ImageTk.PhotoImage(ri12)
    image13=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\7.png")
    ri13=image13.resize((78,128))
    c13=ImageTk.PhotoImage(ri13)
    image14=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\8.png")
    ri14=image14.resize((78,128))
    c14=ImageTk.PhotoImage(ri14)
    image15=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\9.png")
    ri15=image15.resize((78,128))
    c15=ImageTk.PhotoImage(ri15)
    
    image16=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\10.png")
    ri16=image16.resize((78,128))
    c16=ImageTk.PhotoImage(ri16)
    image17=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\11.png")
    ri17=image17.resize((78,128))
    c17=ImageTk.PhotoImage(ri17)
    image18=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\12.png")
    ri18=image18.resize((78,128))
    c18=ImageTk.PhotoImage(ri18)
    image19=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\13.png")
    ri19=image19.resize((78,128))
    c19=ImageTk.PhotoImage(ri19)
    image20=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\14.png")
    ri20=image20.resize((78,128))
    c20=ImageTk.PhotoImage(ri20)
    image21=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\15.png")
    ri21=image21.resize((78,128))
    c21=ImageTk.PhotoImage(ri21)
    image22=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\16.png")
    ri22=image22.resize((78,128))
    c22=ImageTk.PhotoImage(ri22)
    image23=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\17.png")
    ri23=image23.resize((78,128))
    c23=ImageTk.PhotoImage(ri23)
    image24=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\18.png")
    ri24=image24.resize((78,128))
    c24=ImageTk.PhotoImage(ri24)

    background_label = Label(root0, image = t)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()
    h1=130
    w1=80
    h2=1
    w2=1
    y1=230
    y2=380
    y3=530

    C1=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i1=C1.create_image(h2,w2,image=c1,anchor=NW)
    C1.place(x=350,y=y1)
    C2=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i2=C2.create_image(h2,w2,image=c2,anchor=NW)
    C2.place(x=450,y=y1)
    C3=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i3=C3.create_image(h2,w2,image=c3,anchor=NW)
    C3.place(x=550,y=y1)
    C4=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i4=C4.create_image(h2,w2,image=c4,anchor=NW)
    C4.place(x=650,y=y1)
    C5=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i5=C5.create_image(h2,w2,image=c5,anchor=NW)
    C5.place(x=750,y=y1)
    C6=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i6=C6.create_image(h2,w2,image=c6,anchor=NW)
    C6.place(x=850,y=y1)


    C7=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i7=C7.create_image(h2,w2,image=c7,anchor=NW)
    C7.place(x=350,y=y2)
    C8=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i8=C8.create_image(h2,w2,image=c8,anchor=NW)
    C8.place(x=450,y=y2)
    C9=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i9=C9.create_image(h2,w2,image=c9,anchor=NW)
    C9.place(x=550,y=y2)
    C10=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i10=C10.create_image(h2,w2,image=c10,anchor=NW)
    C10.place(x=650,y=y2)
    C11=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i11=C11.create_image(h2,w2,image=c11,anchor=NW)
    C11.place(x=750,y=y2)
    C12=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i3=C12.create_image(h2,w2,image=c12,anchor=NW)
    C12.place(x=850,y=y2)
    C13=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i13=C13.create_image(h2,w2,image=c13,anchor=NW)
    C13.place(x=950,y=y2)
    C14=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i14=C14.create_image(h2,w2,image=c14,anchor=NW)
    C14.place(x=1050,y=y2)
    C15=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i15=C15.create_image(h2,w2,image=c15,anchor=NW)
    C15.place(x=1150,y=y2)


    C16=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i16=C16.create_image(h2,w2,image=c16,anchor=NW)
    C16.place(x=350,y=y3)
    C17=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i17=C17.create_image(h2,w2,image=c17,anchor=NW)
    C17.place(x=450,y=y3)
    C18=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i18=C18.create_image(h2,w2,image=c18,anchor=NW)
    C18.place(x=550,y=y3)
    C19=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i19=C19.create_image(h2,w2,image=c19,anchor=NW)
    C19.place(x=650,y=y3)
    C20=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i20=C20.create_image(h2,w2,image=c20,anchor=NW)
    C20.place(x=750,y=y3)
    C21=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i21=C21.create_image(h2,w2,image=c21,anchor=NW)
    C21.place(x=850,y=y3)
    C22=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i22=C22.create_image(h2,w2,image=c22,anchor=NW)
    C22.place(x=950,y=y3)
    C23=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i23=C23.create_image(h2,w2,image=c23,anchor=NW)
    C23.place(x=1050,y=y3)
    C24=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
    i24=C24.create_image(h2,w2,image=c24,anchor=NW)
    C24.place(x=1150,y=y3)

    bt=Button(root0,text="Start Selection",command=b0,font=('Arial',16),bg='burlywood4',fg='lemonchiffon1').place(x=715,y=700)
    root0.mainloop()

def cardc1():
    global root1,weapon,murder_set
    x=shuffle(weapon)
    root1=Tk()
    root1.config(bg='black')
    c=PhotoImage(file="C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\cards.png")
    #root1.geometry('1575x900')
    root1.geometry('2000x1000')
    root1.title('Weapon Card Page')
    c1 = Canvas(root1, height = 25, width = 50)
    t=PhotoImage(file="C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\tableb.png")
    background_label = Label(root1, image = t)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c1.pack()
    Label(root1,text="Choose the weapon card",background=root1["bg"],foreground='white',font=("Arial",18)).place(x=675,y=130)
    B1=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda :a(B1.cget('textvariable')),textvariable=x[0])
    B1.place(x=320,y=190,relheight=0.28)
    B2=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:a(B2.cget('textvariable')),textvariable=x[1])
    B2.place(x=520,y=190,relheight=0.28)
    B3=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:a(B3.cget('textvariable')),textvariable=x[2])
    B3.place(x=720,y=190,relheight=0.28)
    B4=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:a(B4.cget('textvariable')),textvariable=x[3])
    B4.place(x=920,y=190,relheight=0.28)
    B5=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:a(B5.cget('textvariable')),textvariable=x[4])
    B5.place(x=1120,y=190,relheight=0.28)
    B6=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:a(B6.cget('textvariable')),textvariable=x[5])
    B6.place(x=420,y=460,relheight=0.28)
    B7=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:a(B7.cget('textvariable')),textvariable=x[6])
    B7.place(x=620,y=460,relheight=0.28)
    B8=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:a(B8.cget('textvariable')),textvariable=x[7])
    B8.place(x=820,y=460,relheight=0.28)
    B9=Button(root1,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:a(B9.cget('textvariable')),textvariable=x[8])
    B9.place(x=1020,y=460,relheight=0.28)
    #bt=Button(root1,text="back",command=b1).place(x=1500,y=100)
    root1.mainloop()

def cardc2():
    global root2,place
    x=shuffle(place)
    root2=Tk()
    #root2.geometry('1575x900')
    root2.geometry('2000x1000')
    root2.title('Place Card Weapon')
    root2.config(bg='black')
    c1 = Canvas(root2, height = 25, width = 50)
    t=PhotoImage(file="C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\tableb.png")
    background_label = Label(root2, image = t)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c1.pack()
    c=PhotoImage(file="C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\cards.png")
    Label(root2,text="Choose the place card",background=root2["bg"],foreground='white',font=("Arial",18)).place(x=675,y=130)
    B1=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda :b(B1.cget('textvariable')),textvariable=x[0])
    B1.place(x=320,y=190,relheight=0.28)
    B2=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:b(B2.cget('textvariable')),textvariable=x[1])
    B2.place(x=520,y=190,relheight=0.28)
    B3=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:b(B3.cget('textvariable')),textvariable=x[2])
    B3.place(x=720,y=190,relheight=0.28)
    B4=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:b(B4.cget('textvariable')),textvariable=x[3])
    B4.place(x=920,y=190,relheight=0.28)
    B5=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:b(B5.cget('textvariable')),textvariable=x[4])
    B5.place(x=1120,y=190,relheight=0.28)
    B6=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:b(B6.cget('textvariable')),textvariable=x[5])
    B6.place(x=420,y=460,relheight=0.28)
    B7=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:b(B7.cget('textvariable')),textvariable=x[6])
    B7.place(x=620,y=460,relheight=0.28)
    B8=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:b(B8.cget('textvariable')),textvariable=x[7])
    B8.place(x=820,y=460,relheight=0.28)
    B9=Button(root2,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda:b(B9.cget('textvariable')),textvariable=x[8])
    B9.place(x=1020,y=460,relheight=0.28)
    #bt=Button(root2,text="back",command=b2).place(x=1200,y=100)
    root2.mainloop()

def cardc3():
    global root3
    x=shuffle(person)
    root3=Tk()
    #root3.geometry('1575x900')
    root3.geometry('2000x1000')
    root3.title('Murder Suspect Card Page')
    root3.config(bg='black')
    c1 = Canvas(root3, height = 25, width = 50)
    t=PhotoImage(file="C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\tableb.png")
    background_label = Label(root3, image = t)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c1.pack()
    c=PhotoImage(file="C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\cards.png")
    Label(root3,text="Choose the suspect card",background=root3["bg"],foreground='white',font=("Arial",18)).place(x=675,y=130)
    B1=Button(root3,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda :d(B1.cget('textvariable')),textvariable=x[0])
    B1.place(x=520,y=190,relheight=0.28)
    B2=Button(root3,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda :d(B2.cget('textvariable')),textvariable=x[1])
    B2.place(x=720,y=190,relheight=0.28)
    B3=Button(root3,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda :d(B3.cget('textvariable')),textvariable=x[2])
    B3.place(x=920,y=190,relheight=0.28)
    B4=Button(root3,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda :d(B4.cget('textvariable')),textvariable=x[3])
    B4.place(x=520,y=460,relheight=0.28)
    B5=Button(root3,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda :d(B5.cget('textvariable')),textvariable=x[4])
    B5.place(x=720,y=460,relheight=0.28)
    B6=Button(root3,height=250,width=155,background='black',highlightthickness=0,image=c,borderwidth=0,command=lambda :d(B6.cget('textvariable')),textvariable=x[5])
    B6.place(x=920,y=460,relheight=0.28)
    root3.mainloop()

def disp():
    def aaa():
        global roota
        roota=Tk()
        #roota.geometry('1575x900')
        roota.geometry('2000x1000')
        roota.config(bg='black')
        roota.title('PLAYER 1')
        c = Canvas(roota, height = 25, width = 50)
        t=PhotoImage(file="C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\table.png")
        background_label = Label(roota, image = t)
        background_label.place(x=0,y=0,relwidth=1,relheight=1)
        c.pack()
        xxx=(155,250)
        image1=Image.open(dict[w[0]])
        image2=Image.open(dict[w[1]])
        image3=Image.open(dict[w[2]])
        image4=Image.open(dict[w[3]])
        ri1=image1.resize(xxx)
        ri2=image2.resize(xxx)
        ri3=image3.resize(xxx)
        ri4=image4.resize(xxx)
        a1=ImageTk.PhotoImage(ri1)
        a2=ImageTk.PhotoImage(ri2)
        a3=ImageTk.PhotoImage(ri3)
        a4=ImageTk.PhotoImage(ri4)
        image5=Image.open(dict[w[4]])
        ri5=image5.resize(xxx)
        a5=ImageTk.PhotoImage(ri5)
        B6=Button(roota,height=250,width=155,background='black',highlightthickness=0,image=a5,borderwidth=0,command=None)
        B6.place(x=1120,y=300,relheight=0.28)
        B1=Button(roota,height=250,width=155,background='black',highlightthickness=0,image=a1,borderwidth=0,command=None)
        B1.place(x=320,y=300,relheight=0.28)
        B2=Button(roota,height=250,width=155,background='black',highlightthickness=0,image=a2,borderwidth=0,command=None)
        B2.place(x=520,y=300,relheight=0.28)
        B3=Button(roota,height=250,width=155,background='black',highlightthickness=0,image=a3,borderwidth=0,command=None)
        B3.place(x=720,y=300,relheight=0.28)
        B4=Button(roota,height=250,width=155,background='black',highlightthickness=0,image=a4,borderwidth=0,command=None)
        B4.place(x=920,y=300,relheight=0.28)
        B5=Button(roota,text="NEXT PLAYER 2",font=('Arial',16),bg='burlywood4',fg='lemonchiffon1',command=bbb)
        B5.place(x=715,y=700)
        roota.mainloop()

    def bbb():
        roota.destroy()
        global rootb
        rootb=Tk()
        #rootb.geometry('1575x900')
        rootb.geometry('2000x1000')
        rootb.config(bg='black')
        rootb.title('PLAYER 2')
        c = Canvas(rootb, height = 25, width = 50)
        t=PhotoImage(file="C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\table.png")
        background_label = Label(rootb, image = t)
        background_label.place(x=0,y=0,relwidth=1,relheight=1)
        c.pack()
        xxx=(155,250)
        image1=Image.open(dict[x[0]])
        image2=Image.open(dict[x[1]])
        image3=Image.open(dict[x[2]])
        image4=Image.open(dict[x[3]])
        ri1=image1.resize(xxx)
        ri2=image2.resize(xxx)
        ri3=image3.resize(xxx)
        ri4=image4.resize(xxx)
        a1=ImageTk.PhotoImage(ri1)
        a2=ImageTk.PhotoImage(ri2)
        a3=ImageTk.PhotoImage(ri3)
        a4=ImageTk.PhotoImage(ri4)
        image5=Image.open(dict[x[4]])
        ri5=image5.resize(xxx)
        a5=ImageTk.PhotoImage(ri5)
        B6=Button(rootb,height=250,width=155,background='black',highlightthickness=0,image=a5,borderwidth=0,command=None)
        B6.place(x=1120,y=300,relheight=0.28)
        B1=Button(rootb,height=250,width=155,background='black',highlightthickness=0,image=a1,borderwidth=0,command=None)
        B1.place(x=320,y=300,relheight=0.28)
        B2=Button(rootb,height=250,width=155,background='black',highlightthickness=0,image=a2,borderwidth=0,command=None)
        B2.place(x=520,y=300,relheight=0.28)
        B3=Button(rootb,height=250,width=155,background='black',highlightthickness=0,image=a3,borderwidth=0,command=None)
        B3.place(x=720,y=300,relheight=0.28)
        B4=Button(rootb,height=250,width=155,background='black',highlightthickness=0,image=a4,borderwidth=0,command=None)
        B4.place(x=920,y=300,relheight=0.28)
        B5=Button(rootb,text="NEXT PLAYER 3",font=('Arial',16),bg='burlywood4',fg='lemonchiffon1',command=ccc)
        B5.place(x=715,y=700)
        rootb.mainloop()

    def ccc():
        rootb.destroy()
        global rootc
        rootc=Tk()
        #rootc.geometry('1575x900')
        rootc.geometry('2000x1000')
        rootc.config(bg='black')
        rootc.title('PLAYER 3')
        c = Canvas(rootc, height = 25, width = 50)
        t=PhotoImage(file="C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\table.png")
        background_label = Label(rootc, image = t)
        background_label.place(x=0,y=0,relwidth=1,relheight=1)
        c.pack()
        xxx=(155,250)
        image1=Image.open(dict[y[0]])
        image2=Image.open(dict[y[1]])
        image3=Image.open(dict[y[2]])
        image4=Image.open(dict[y[3]])
        ri1=image1.resize(xxx)
        ri2=image2.resize(xxx)
        ri3=image3.resize(xxx)
        ri4=image4.resize(xxx)
        a1=ImageTk.PhotoImage(ri1)
        a2=ImageTk.PhotoImage(ri2)
        a3=ImageTk.PhotoImage(ri3)
        a4=ImageTk.PhotoImage(ri4)
        image5=Image.open(dict[y[4]])
        ri5=image5.resize(xxx)
        a5=ImageTk.PhotoImage(ri5)
        B6=Button(rootc,height=250,width=155,background='black',highlightthickness=0,image=a5,borderwidth=0,command=None)
        B6.place(x=1120,y=300,relheight=0.28)
        B1=Button(rootc,height=250,width=155,background='black',highlightthickness=0,image=a1,borderwidth=0,command=None)
        B1.place(x=320,y=300,relheight=0.28)
        B2=Button(rootc,height=250,width=155,background='black',highlightthickness=0,image=a2,borderwidth=0,command=None)
        B2.place(x=520,y=300,relheight=0.28)
        B3=Button(rootc,height=250,width=155,background='black',highlightthickness=0,image=a3,borderwidth=0,command=None)
        B3.place(x=720,y=300,relheight=0.28)
        B4=Button(rootc,height=250,width=155,background='black',highlightthickness=0,image=a4,borderwidth=0,command=None)
        B4.place(x=920,y=300,relheight=0.28)
        B5=Button(rootc,text="NEXT PLAYER 4",font=('Arial',16),bg='burlywood4',fg='lemonchiffon1',command=ddd)
        B5.place(x=715,y=700)
        rootc.mainloop()

    def ddd():
        rootc.destroy()
        global rootd
        rootd=Tk()
        #rootd.geometry('1575x900')
        rootd.geometry('2000x1000')
        rootd.config(bg='black')
        rootd.title('PLAYER 4')
        c = Canvas(rootd, height = 25, width = 50)
        t=PhotoImage(file="C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\table.png")
        background_label = Label(rootd, image = t)
        background_label.place(x=0,y=0,relwidth=1,relheight=1)
        c.pack()
        xxx=(155,250)
        image1=Image.open(dict[z[0]])
        image2=Image.open(dict[z[1]])
        image3=Image.open(dict[z[2]])
        image4=Image.open(dict[z[3]])
        image5=Image.open(dict[z[4]])
        ri1=image1.resize(xxx)
        ri2=image2.resize(xxx)
        ri3=image3.resize(xxx)
        ri4=image4.resize(xxx)
        ri5=image5.resize(xxx)
        a1=ImageTk.PhotoImage(ri1)
        a2=ImageTk.PhotoImage(ri2)
        a3=ImageTk.PhotoImage(ri3)
        a4=ImageTk.PhotoImage(ri4)
        a5=ImageTk.PhotoImage(ri5)
        image6=Image.open(dict[z[5]])
        ri6=image6.resize(xxx)
        a6=ImageTk.PhotoImage(ri6)
        B6=Button(rootd,height=250,width=155,background='black',highlightthickness=0,image=a6,borderwidth=0,command=None)
        B6.place(x=1220,y=300,relheight=0.28)
        B1=Button(rootd,height=250,width=155,background='black',highlightthickness=0,image=a1,borderwidth=0,command=None)
        B1.place(x=220,y=300,relheight=0.28)
        B2=Button(rootd,height=250,width=155,background='black',highlightthickness=0,image=a2,borderwidth=0,command=None)
        B2.place(x=420,y=300,relheight=0.28)
        B3=Button(rootd,height=250,width=155,background='black',highlightthickness=0,image=a3,borderwidth=0,command=None)
        B3.place(x=620,y=300,relheight=0.28)
        B4=Button(rootd,height=250,width=155,background='black',highlightthickness=0,image=a4,borderwidth=0,command=None)
        B4.place(x=820,y=300,relheight=0.28)
        B4=Button(rootd,height=250,width=155,background='black',highlightthickness=0,image=a5,borderwidth=0,command=None)
        B4.place(x=1020,y=300,relheight=0.28)
        B5=Button(rootd,text="CLOSE",font=('Arial',16),bg='burlywood4',fg='lemonchiffon1',command=eee)
        B5.place(x=715,y=700)
        rootd.mainloop()

    def eee():
        rootd.destroy()
        os.startfile("game.py")
        
    a=weapon.copy()
    a.remove(murder_set[0])
    b=place.copy()
    b.remove(murder_set[1])
    c=person.copy()
    c.remove(murder_set[2])
    d=a+b+c
    w=[]
    x=[]
    y=[]
    z=[]
    xx=shuffle(d)
    count=1
    for i in xx:
        if count<=5:
            w.append(i)
            count+=1
        elif count<=10:
            x.append(i)
            count+=1
        elif count<=15:
            y.append(i)
            count+=1
        elif count<=21:
            z.append(i)
            count+=1
    print(w)
    print(x)
    print(y)
    print(z)
    aaa()



dict={'gun':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\2.png",
      'flowervase':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\5.png",
      'bat':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\6.png",
      'wrench':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\9.png",
      'knife':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\8.png",
      'brokenglassbottle':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\3.png",
      'candlestick':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\4.png",
      'openlivewire':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\1.png",
      'rope':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\7.png",
      'master bedroom':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\17.png",
      'bedroom1':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\15.png",
      'bedroom2':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\13.png",
      'garage':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\12.png",
      'kitchen':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\11.png",
      'storage room':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\10.png",
      'dining hall':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\18.png",
      'theatre':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\16.png",
      'library':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\14.png",
      'wife':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\21.png",
      'daughter':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\19.png",
      'son':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\24.png",
      'gardener':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\20.png",
      'butler':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\23.png",
      'psychiatrist':"C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\22.png"
      }
weapon=['gun','flowervase','bat','wrench','knife','brokenglassbottle','candlestick','openlivewire','rope']
place=['master bedroom','bedroom1','bedroom2','garage','kitchen','storage room','dining hall','theatre','library']
person=['wife','daughter','son','gardener','butler','psychiatrist']
murder_set=[]
display()
