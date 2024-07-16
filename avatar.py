from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import os

def roundPolygon(canvas,x, y, sharpness, **kwargs):
    if sharpness < 2:
        sharpness = 2
    ratioMultiplier = sharpness - 1
    ratioDividend = sharpness
    points = []
    for i in range(len(x)):
        points.append(x[i])
        points.append(y[i])
        if i != (len(x) - 1): 
            points.append((ratioMultiplier*x[i] + x[i + 1])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[i + 1])/ratioDividend)
            points.append((ratioMultiplier*x[i + 1] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[i + 1] + y[i])/ratioDividend)
        else:
            points.append((ratioMultiplier*x[i] + x[0])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[0])/ratioDividend)
            points.append((ratioMultiplier*x[0] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[0] + y[i])/ratioDividend)
            points.append(x[0])
            points.append(y[0])
    return canvas.create_polygon(points, **kwargs, smooth=TRUE)

def label1back():
    change_image_backward()
    image_label1.config(image=photo)
    image_label1.image = photo

def label1forward():
    change_image_forward()
    image_label1.config(image=photo)
    image_label1.image = photo

def label2back():
    change_image_backward()
    image_label2.config(image=photo)
    image_label2.image = photo

def label2forward():
    change_image_forward()
    image_label2.config(image=photo)
    image_label2.image = photo

def label3back():
    change_image_backward()
    image_label3.config(image=photo)
    image_label3.image = photo

def label3forward():
    change_image_forward()
    image_label3.config(image=photo)
    image_label3.image = photo

def label4back():
    change_image_backward()
    image_label4.config(image=photo)
    image_label4.image = photo

def label4forward():
    change_image_forward()
    image_label4.config(image=photo)
    image_label4.image = photo
    
def change_image_backward():
    global current_image_index, photo
    current_image_index = (current_image_index - 1) % len(images)
    photo = ImageTk.PhotoImage(images[current_image_index])
    
def change_image_forward():
    global current_image_index, photo
    current_image_index = (current_image_index + 1) % len(images)
    photo = ImageTk.PhotoImage(images[current_image_index])

def next_pg():
    flag = 0
    players = [user1.get(),user2.get(),user3.get(),user4.get()]
    print(players)
    for i in players:
        if(None in players or "" in players):
            flag = 1
            break
        else:
            if(players.count(i) > 1):
                flag = 1
                break
    if(flag == 1):
        messagebox.showinfo("","Kindly ensure that all 4 usernames are unique")
        messagebox.showinfo("","The page will now be reloaded")
        root.destroy()
        os.startfile("avatar.py")
    else:
        root.destroy()
        os.startfile("cards.py")

root=Tk()
root.config(bg='burlywood3')
root.geometry('2000x1000')
root.title("Avatar Page")

c1 = Canvas(root,bg='burlywood3',bd=0,highlightthickness=0, relief='ridge')
c1.place(x=350,y=50,relheight=0.38,relwidth=0.22)
c2 = Canvas(root,bg='burlywood3',bd=0,highlightthickness=0, relief='ridge')
c2.place(x=850,y=50,relheight=0.38,relwidth=0.22)
c3 = Canvas(root,bg='burlywood3',bd=0,highlightthickness=0, relief='ridge')
#c3.place(x=350,y=450,relheight=0.38,relwidth=0.22)
c3.place(x=350,y=400,relheight=0.38,relwidth=0.22)
c4 = Canvas(root,bg='burlywood3',bd=0,highlightthickness=0, relief='ridge')
#c4.place(x=850,y=450,relheight=0.38,relwidth=0.22)
c4.place(x=850,y=400,relheight=0.38,relwidth=0.22)

my_rectangle = roundPolygon(c1,[2, 343,343, 2], [2, 2, 339,339], 3, width=5, outline="coral3", fill="peachpuff")
my_rectangle = roundPolygon(c2,[2, 343,343, 2], [2, 2, 339,339], 3, width=5, outline="deep pink", fill="#f2cbec")
my_rectangle = roundPolygon(c3,[2, 343,343, 2], [2, 2, 339,339], 3, width=5, outline="steel blue", fill="light cyan")
my_rectangle = roundPolygon(c4,[2, 343,343, 2], [2, 2, 339,339], 3, width=5, outline="darkorchid2", fill="lavender")
my_rectangle = roundPolygon(c1,[100,250,250,100], [25,25,75,75], 5, width=5, outline="coral3", fill="coral3")
my_rectangle = roundPolygon(c2,[100,250,250,100], [25,25,75,75], 5, width=5, outline="deep pink", fill="deep pink")
my_rectangle = roundPolygon(c3,[100,250,250,100], [25,25,75,75], 5, width=5, outline="steel blue", fill="steel blue")
my_rectangle = roundPolygon(c4,[100,250,250,100], [25,25,75,75], 5, width=5, outline="darkorchid2", fill="darkorchid2")

#Box Titles
Label(root, text = "PLAYER 1", font = ("Calibri 22"), bg = "coral3", fg = "white").place(x = 470, y = 80)
Label(root, text = "PLAYER 2", font = ("Calibri 22"), bg = "deep pink", fg = "white").place(x = 970, y = 80)
Label(root, text = "PLAYER 3", font = ("Calibri 22"), bg = "steel blue", fg = "white").place(x = 470, y = 430)
Label(root, text = "PLAYER 4", font = ("Calibri 22"), bg = "darkorchid2", fg = "white").place(x = 970, y = 430)

#Loading the image paths
image_paths =["C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\Avatar 1.png",
              "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\Avatar 2.png",
              "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\Avatar 3.png",
              "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\Avatar 4.png",
              "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\Avatar 5.png",
              "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\Avatar 6.png"]

images = [Image.open(image_path) for image_path in image_paths]

# Create a label to display the image
#Rectangle 1
initial_photo1 = ImageTk.PhotoImage(images[0])
image_label1 = tk.Label(root, image=initial_photo1, relief = SUNKEN)
image_label1.place(x = 470, y = 142)

current_image_index = 0

b1=Button(root,text='←',command=label1back).place(x=375,y=200,relheight=0.038,relwidth=0.022)
b2=Button(root,text='→',command=label1forward).place(x=640,y=200,relheight=0.038,relwidth=0.022)

#Rectangle 2
initial_photo2 = ImageTk.PhotoImage(images[1])
image_label2 = tk.Label(root, image=initial_photo2, relief = SUNKEN)
image_label2.place(x = 970, y = 142)

current_image_index = 0

b3=Button(root,text='←', command = label2back).place(x=875,y=200,relheight=0.038,relwidth=0.022)
b4=Button(root,text='→', command = label2forward).place(x=1140,y=200,relheight=0.038,relwidth=0.022)

#Rectangle 3
initial_photo3 = ImageTk.PhotoImage(images[2])
image_label3 = tk.Label(root, image=initial_photo3, relief = SUNKEN)
#image_label3.place(x = 470, y = 575)
image_label3.place(x = 470, y = 495)

current_image_index = 0

b5=Button(root,text='←', command = label3back).place(x=375,y=550,relheight=0.038,relwidth=0.022)
b6=Button(root,text='→', command = label3forward).place(x=640,y=550,relheight=0.038,relwidth=0.022)

#Rectangle 4
initial_photo4 = ImageTk.PhotoImage(images[3])
image_label4 = tk.Label(root, image=initial_photo4, relief = SUNKEN)
#image_label4.place(x = 970, y = 575)
image_label4.place(x = 970, y = 495)

current_image_index = 0

b7=Button(root,text='←', command = label4back).place(x=875,y=550,relheight=0.038,relwidth=0.022)
b8=Button(root,text='→', command = label4forward).place(x=1140,y=550,relheight=0.038,relwidth=0.022)

#Retrieving the data from player data
fr = open("Player-Data.txt","r")
usernames = []
try:
    while True:
        ln = fr.readline().split(",")
        usernames.append(ln[2][:(len(ln[2])-1)])
except:
    fr.close()
    
#Combobox 1
user1 = tk.StringVar() 
cb1 = ttk.Combobox(root, textvariable = user1)
cb1['values'] = usernames
cb1.place(x = 450, y = 325)
cb1.set("Select Player...")

#Combobox 2
user2 = tk.StringVar() 
cb2 = ttk.Combobox(root, textvariable = user2)
cb2['values'] = usernames
cb2.place(x = 950, y = 325)
cb2.set("Select Player...")

#Combobox 3
user3 = tk.StringVar() 
cb3 = ttk.Combobox(root, textvariable = user3)
cb3['values'] = usernames
cb3.place(x = 450, y = 680)
cb3.set("Select Player...")

#Combobox 4
user4 = tk.StringVar() 
cb4 = ttk.Combobox(root, textvariable = user4)
cb4['values'] = usernames
cb4.place(x = 950, y = 680)
cb4.set("Select Player...")

next_btn = Button(text = "Next ->", font = ("Calibri 12"),command = next_pg).place(x = 1470, y = 0)
root.mainloop()
