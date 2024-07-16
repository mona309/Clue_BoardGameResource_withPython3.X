from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import random
import os

flagr=0
flagt=0
def rol():
    global flagr,r
    flagr=1
    roota=Toplevel()
    roota.geometry('200x300')
    roota.configure(bg="#f3ba4b")
    roota.geometry("+1050+326")
    r = random.randint(1,12)
    rz=(172,277)
    if(r == 1):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-1.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==2):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-2.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==3):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-3.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==4):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-4.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==5):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-5.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==6):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-6.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==7):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-7.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==8):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-8.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==9):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-9.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==10):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-10.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==11):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-11.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==12):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-12.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    background_label = Label(roota, image = g, fg = "#f3ba4b")
    background_label.place(x=0,y=0,relwidth=1,relheight=1)  
    roota.mainloop()

def nex():
    global pyr,rnd,mp,flagr,flagt
    if pyr<4:
        pyr+=1
    else:
        pyr=0
        if pyr<8:
            rnd+=1
            pyr+=1
        else:
            pyr=0
            if pyr<12:
                rnd+=1
                pyr+=1
            else:
                pass
    if rnd==11:
        root.destroy()
        os.startfile("Ending-Page.py")
    flagr=0
    flagt=1
    try:
        player.config(text="Now : Player "+str(pyr))
        rounds.config(text="Round -  "+str(rnd))
        mp=pyr
    except Exception:
        pass

def pos(x):
    global p1p,p2p,p3p,p4p
    if rnd==0:
        if pyr==1:
            x.config(bg='hot pink')
            p1p=x
            nex()
        elif pyr==2:
            x.config(bg='blue')
            p2p=x
            nex()
        elif pyr==3:
            x.config(bg='green')
            p3p=x
            nex()
        elif pyr==4:
            x.config(bg='lavender')
            p4p=x
            nex()
    else:
        if pyr==1:
            p1p.config(bg='burlywood3')
            p1p=x
            p1p.config(bg='hot pink')
        elif pyr==2:
            p2p.config(bg='burlywood3')
            p2p=x
            p2p.config(bg='blue')
        elif pyr==3:
            p3p.config(bg='burlywood3')
            p3p=x
            p3p.config(bg='green')
        elif pyr==4:
            p4p.config(bg='burlywood3')
            p4p=x
            p4p.config(bg='lavender')

rnd=0
pyr=1
p1p=0
p2p=0
p3p=0
p4p=0
root = tk.Tk()
root.title("Loading-Page...")
#root.geometry('1575x900')
root.geometry('2000x1000')
root.configure(bg = "burlywood4")
filename=PhotoImage(file="C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\mp.png")
background_label = Label(root, image = filename,bg = "burlywood2").place(x=675,y=0)
rounds=Label(root,text="Round -  "+str(rnd),bg="burlywood4",font=("Arial",40))
rounds.place(x=205,y=100)
player=Label(root,text="Now : Player "+str(pyr),bg="burlywood4",font=("Arial",40))
player.place(x=150,y=175)
roll=Button(root,text="       Roll       ",command=rol,bg="burlywood2",font=("Arial",30)).place(x=215,y=350)
next_btn=Button(root,text="      Next      ",command=nex,bg="burlywood2",font=("Arial",30)).place(x=215,y=500)

image=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\cards.png")
ri=image.resize((100,162))
c=ImageTk.PhotoImage(ri)

w1=101
h1=164

h2=1
w2=1

C1=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
i1=C1.create_image(h2,w2,image=c,anchor=NW)
C1.place(x=50,y=600)
C2=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
i2=C2.create_image(h2,w2,image=c,anchor=NW)
C2.place(x=200,y=600)
C3=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
i3=C3.create_image(h2,w2,image=c,anchor=NW)
C3.place(x=350,y=600)
C4=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
i4=C4.create_image(h2,w2,image=c,anchor=NW)
C4.place(x=500,y=600)


#room buttons

r3=Button(root,command=None,bg="burlywood3",height=23,width=450).place(x=1350,y=0)
r2=Button(root,command=None,bg="burlywood3",height=15,width=31).place(x=1100,y=0)
r1=Button(root,command=None,bg="burlywood3",height=13,width=49).place(x=675,y=0)

r4=Button(root,command=None,bg="burlywood3",height=11,width=38).place(x=676,y=276)
r5=Button(root,command=None,bg="burlywood3",height=11,width=38).place(x=676,y=476)
r6=Button(root,command=None,bg="burlywood3",height=16,width=32).place(x=1350,y=426)

r7=Button(root,command=None,bg="burlywood3",height=20,width=28).place(x=1050,y=325)

r8=Button(root,command=None,bg="burlywood3",height=10,width=57).place(x=675,y=725)
r9=Button(root,command=None,bg="burlywood3",height=8,width=55).place(x=1150,y=750)

#start position buttons

b=Button(root,command=lambda :pos(b),bg="burlywood4",height=2,width=3)
b.place(x=1051,y=1)
bb=Button(root,command=lambda :pos(bb),bg="burlywood4",height=2,width=3)
bb.place(x=676,y=227)
bbb=Button(root,command=lambda :pos(bbb),bg="burlywood4",height=2,width=3)
bbb.place(x=676,y=677)
bbbb=Button(root,command=lambda :pos(bbbb),bg="burlywood4",height=2,width=3)
bbbb.place(x=1100,y=744)
bbbbb=Button(root,command=lambda :pos(bbbbb),bg="burlywood4",height=2,width=3)
bbbbb.place(x=1490,y=370)
bbbbbb=Button(root,command=lambda :pos(bbbbbb),bg="burlywood4",height=2,width=3)
#bbbbbb.place(x=1510,y=702)
bbbbbb.place(x=1490,y=702)

#grid buttons
#y1=40
y1=52
g1=Button(root,height=2,width=3,command=lambda :pos(g1),bg="burlywood2")
g1.place(x=1053,y=y1)
g12=Button(root,height=2,width=3,command=lambda :pos(g12),bg="burlywood2")
g12.place(x=1053,y=y1+30)
g13=Button(root,height=2,width=3,command=lambda :pos(g13),bg="burlywood2")
g13.place(x=1053,y=y1+60)
g14=Button(root,height=2,width=3,command=lambda :pos(g14),bg="burlywood2")
g14.place(x=1053,y=y1+90)
g15=Button(root,height=2,width=3,command=lambda :pos(g15),bg="burlywood2")
g15.place(x=1053,y=y1+120)
g16=Button(root,height=2,width=3,command=lambda :pos(g16),bg="burlywood2")
g16.place(x=1053,y=y1+150)
g17=Button(root,height=2,width=3,command=lambda :pos(g17),bg="burlywood2")
g17.place(x=1053,y=y1+180)

#x1=710
x1 = 720
g2=Button(root,height=2,width=3,command=lambda :pos(g2),bg="burlywood2")
g2.place(x=x1+5,y=226)
g21=Button(root,height=2,width=3,command=lambda :pos(g21),bg="burlywood2")
g21.place(x=x1+30,y=226)
g22=Button(root,height=2,width=3,command=lambda :pos(g22),bg="burlywood2")
g22.place(x=x1+60,y=226)
g23=Button(root,height=2,width=3,command=lambda :pos(g23),bg="burlywood2")
g23.place(x=x1+90,y=226)
g24=Button(root,height=2,width=3,command=lambda :pos(g24),bg="burlywood2")
g24.place(x=x1+120,y=226)
g25=Button(root,height=2,width=3,command=lambda :pos(g25),bg="burlywood2")
g25.place(x=x1+150,y=226)
g26=Button(root,height=2,width=3,command=lambda :pos(g26),bg="burlywood2")
g26.place(x=x1+180,y=226)
g27=Button(root,height=2,width=3,command=lambda :pos(g27),bg="burlywood2")
g27.place(x=x1+210,y=226)
g28=Button(root,height=2,width=3,command=lambda :pos(g28),bg="burlywood2")
g28.place(x=x1+240,y=226)
g29=Button(root,height=2,width=3,command=lambda :pos(g29),bg="burlywood2")
g29.place(x=x1+270,y=226)
g20=Button(root,height=2,width=3,command=lambda :pos(g20),bg="burlywood2")
g20.place(x=x1+300,y=226)

g3=Button(root,height=2,width=3,command=lambda :pos(g3),bg="burlywood2")
g3.place(x=x1+5,y=676)
g31=Button(root,height=2,width=3,command=lambda :pos(g31),bg="burlywood2")
g31.place(x=x1+30,y=676)
g32=Button(root,height=2,width=3,command=lambda :pos(g32),bg="burlywood2")
g32.place(x=x1+60,y=676)
g33=Button(root,height=2,width=3,command=lambda :pos(g33),bg="burlywood2")
g33.place(x=x1+90,y=676)
g34=Button(root,height=2,width=3,command=lambda :pos(g34),bg="burlywood2")
g34.place(x=x1+120,y=676)
g35=Button(root,height=2,width=3,command=lambda :pos(g35),bg="burlywood2")
g35.place(x=x1+150,y=676)
g36=Button(root,height=2,width=3,command=lambda :pos(g36),bg="burlywood2")
g36.place(x=x1+180,y=676)
g37=Button(root,height=2,width=3,command=lambda :pos(g37),bg="burlywood2")
g37.place(x=x1+210,y=676)
g38=Button(root,height=2,width=3,command=lambda :pos(g38),bg="burlywood2")
g38.place(x=x1+240,y=676)
g39=Button(root,height=2,width=3,command=lambda :pos(g39),bg="burlywood2")
g39.place(x=x1+270,y=676)
g30=Button(root,height=2,width=3,command=lambda :pos(g30),bg="burlywood2")
g30.place(x=x1+300,y=676)
g301=Button(root,height=2,width=3,command=lambda :pos(g301),bg="burlywood2")
g301.place(x=x1+330,y=676)
g302=Button(root,height=2,width=3,command=lambda :pos(g302),bg="burlywood2")
g302.place(x=x1+360,y=676)
g303=Button(root,height=2,width=3,command=lambda :pos(g303),bg="burlywood2")
g303.place(x=x1+390,y=676)
g304=Button(root,height=2,width=3,command=lambda :pos(g304),bg="burlywood2")
g304.place(x=x1+420,y=676)
g305=Button(root,height=2,width=3,command=lambda :pos(g305),bg="burlywood2")
g305.place(x=x1+450,y=676)
g306=Button(root,height=2,width=3,command=lambda :pos(g306),bg="burlywood2")
g306.place(x=x1+480,y=676)
g307=Button(root,height=2,width=3,command=lambda :pos(g307),bg="red")
g307.place(x=x1+510,y=676)
g308=Button(root,height=2,width=3,command=lambda :pos(g308),bg="burlywood2")
g308.place(x=x1+540,y=676)
g309=Button(root,height=2,width=3,command=lambda :pos(g309),bg="burlywood2")
g309.place(x=x1+570,y=676)
g310=Button(root,height=2,width=3,command=lambda :pos(g310),bg="burlywood2")
g310.place(x=x1+597,y=676)

y2=875
'''
g4=Button(root,height=2,width=3,command=lambda :pos(g4),bg="burlywood2")
g4.place(x=1105,y=y2-35)
g41=Button(root,height=2,width=3,command=lambda :pos(g41),bg="burlywood2")
g41.place(x=1105,y=y2-60)
g42=Button(root,height=2,width=3,command=lambda :pos(g42),bg="burlywood2")
g42.place(x=1105,y=y2-90)
g43=Button(root,height=2,width=3,command=lambda :pos(g43),bg="burlywood2")
g43.place(x=1105,y=y2-120)
g44=Button(root,height=2,width=3,command=lambda :pos(g44),bg="burlywood2")
g44.place(x=1105,y=y2-145)
g45=Button(root,height=2,width=3,command=lambda :pos(g45),bg="burlywood2")
g45.place(x=1105,y=y2-175)
'''
x2=1100
g5=Button(root,height=2,width=3,command=lambda :pos(g5),bg="burlywood2")
g5.place(x=x2,y=702)
g51=Button(root,height=2,width=3,command=lambda :pos(g51),bg="burlywood2")
g51.place(x=x2+30,y=702)
g52=Button(root,height=2,width=3,command=lambda :pos(g52),bg="burlywood2")
g52.place(x=x2+60,y=702)
g53=Button(root,height=2,width=3,command=lambda :pos(g53),bg="burlywood2")
g53.place(x=x2+90,y=702)
g54=Button(root,height=2,width=3,command=lambda :pos(g54),bg="burlywood2")
g54.place(x=x2+120,y=702)
g55=Button(root,height=2,width=3,command=lambda :pos(g55),bg="burlywood2")
g55.place(x=x2+150,y=702)
g56=Button(root,height=2,width=3,command=lambda :pos(g56),bg="burlywood2")
g56.place(x=x2+180,y=702)
g57=Button(root,height=2,width=3,command=lambda :pos(g57),bg="burlywood2")
g57.place(x=x2+210,y=702)
g58=Button(root,height=2,width=3,command=lambda :pos(g58),bg="burlywood2")
g58.place(x=x2+240,y=702)
g59=Button(root,height=2,width=3,command=lambda :pos(g59),bg="burlywood2")
g59.place(x=x2+270,y=702)
g50=Button(root,height=2,width=3,command=lambda :pos(g50),bg="burlywood2")
g50.place(x=x2+300,y=702)
g501=Button(root,height=2,width=3,command=lambda :pos(g501),bg="burlywood2")
g501.place(x=x2+330,y=702)
g502=Button(root,height=2,width=3,command=lambda :pos(g502),bg="burlywood2")
g502.place(x=x2+360,y=702)
'''
g503=Button(root,height=2,width=3,command=lambda :pos(g503),bg="burlywood2")
g503.place(x=x2+390,y=702)
'''
#y3=250
y3=256
g6=Button(root,height=2,width=3,command=lambda :pos(g6),bg="burlywood2")
g6.place(x=979,y=y3)
g61=Button(root,height=2,width=3,command=lambda :pos(g61),bg="burlywood2")
g61.place(x=979,y=y3+30)
g62=Button(root,height=2,width=3,command=lambda :pos(g62),bg="burlywood2")
g62.place(x=979,y=y3+60)
g63=Button(root,height=2,width=3,command=lambda :pos(g63),bg="burlywood2")
g63.place(x=979,y=y3+90)
g64=Button(root,height=2,width=3,command=lambda :pos(g64),bg="burlywood2")
g64.place(x=979,y=y3+120)
g65=Button(root,height=2,width=3,command=lambda :pos(g65),bg="burlywood2")
g65.place(x=979,y=y3+150)
g66=Button(root,height=2,width=3,command=lambda :pos(g66),bg="burlywood2")
g66.place(x=979,y=y3+180)
g67=Button(root,height=2,width=3,command=lambda :pos(g67),bg="burlywood2")
g67.place(x=979,y=y3+210)
g68=Button(root,height=2,width=3,command=lambda :pos(g68),bg="burlywood2")
g68.place(x=979,y=y3+240)
g69=Button(root,height=2,width=3,command=lambda :pos(g69),bg="burlywood2")
g69.place(x=979,y=y3+270)
g60=Button(root,height=2,width=3,command=lambda :pos(g60),bg="burlywood2")
g60.place(x=979,y=y3+300)
g601=Button(root,height=2,width=3,command=lambda :pos(g601),bg="burlywood2")
g601.place(x=979,y=y3+330)
g602=Button(root,height=2,width=3,command=lambda :pos(g602),bg="burlywood2")
g602.place(x=979,y=y3+360)
g603=Button(root,height=2,width=3,command=lambda :pos(g603),bg="red")
g603.place(x=979,y=y3+390)

g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=1008,y=y3)
g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="red").place(x=1008,y=y3+30)
g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=1008,y=y3+60)
g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=1008,y=y3+90)
g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=1008,y=y3+120)
g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=1008,y=y3+150)
g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=1008,y=y3+180)
g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=1008,y=y3+210)
g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=1008,y=y3+240)
g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=1008,y=y3+270)
g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=1008,y=y3+300)
g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=1008,y=y3+330)
g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=1008,y=y3+360)
g7=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=1008,y=y3+390)

x4=1279
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x4,y=y3)
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x4,y=y3+30)
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x4,y=y3+60)
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x4,y=y3+90)
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x4,y=y3+120)
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x4,y=y3+150)
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x4,y=y3+180)
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="red").place(x=x4,y=y3+210)
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x4,y=y3+240)
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x4,y=y3+270)
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x4,y=y3+300)
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x4,y=y3+330)
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x4,y=y3+360)
g8=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x4,y=y3+390)

x5=1308
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3)
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3+30)
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3+60)
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3+90)
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3+120)
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3+150)
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3+180)
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3+210)
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3+240)
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3+270)
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3+300)
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3+330)
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3+360)
g9=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x5,y=y3+390)

x6=1040
h1=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x6,y=251)
h1=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x6+30,y=251)
h1=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x6+60,y=251)
h1=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x6+90,y=251)
h1=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x6+120,y=251)
h1=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x6+150,y=251)
h1=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x6+180,y=251)
h1=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x6+210,y=251)

x7=1040
h2=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x7,y=278)
h2=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x7+30,y=278)
h2=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x7+60,y=278)
h2=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x7+90,y=278)
h2=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x7+120,y=278)
h2=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x7+150,y=278)
h2=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x7+180,y=278)
h2=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x7+210,y=278)

x8=1040
y4=645
h3=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x8,y=y4)
h3=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x8+30,y=y4)
h3=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x8+60,y=y4)
h3=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x8+90,y=y4)
h3=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x8+120,y=y4)
h3=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x8+150,y=y4)
h3=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x8+180,y=y4)
h3=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x8+210,y=y4)

y5=370
x9=1340
h4=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x9,y=y5)
h4=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x9+30,y=y5)
h4=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x9+60,y=y5)
h4=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x9+90,y=y5)
h4=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x9+120,y=y5)
#h4=Button(root,height=2,width=3,command=lambda :pos(b),bg="burlywood2").place(x=x9+150,y=y5)

root.mainloop()



