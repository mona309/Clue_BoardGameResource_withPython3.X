from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

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
        
root=Tk()
root.config(bg='burlywood3')
root.geometry('2000x1000')

c1 = Canvas(root,bg='burlywood3',bd=0,highlightthickness=0, relief='ridge')
c1.place(x=350,y=50,relheight=0.38,relwidth=0.22)
c2 = Canvas(root,bg='burlywood3',bd=0,highlightthickness=0, relief='ridge')
c2.place(x=850,y=50,relheight=0.38,relwidth=0.22)
c3 = Canvas(root,bg='burlywood3',bd=0,highlightthickness=0, relief='ridge')
c3.place(x=350,y=450,relheight=0.38,relwidth=0.22)
c4 = Canvas(root,bg='burlywood3',bd=0,highlightthickness=0, relief='ridge')
c4.place(x=850,y=450,relheight=0.38,relwidth=0.22)

my_rectangle = roundPolygon(c1,[2, 343,343, 2], [2, 2, 339,339], 3, width=5, outline="coral3", fill="peachpuff")
my_rectangle = roundPolygon(c2,[2, 343,343, 2], [2, 2, 339,339], 3, width=5, outline="deep pink", fill="#f2cbec")
my_rectangle = roundPolygon(c3,[2, 343,343, 2], [2, 2, 339,339], 3, width=5, outline="steel blue", fill="light cyan")
my_rectangle = roundPolygon(c4,[2, 343,343, 2], [2, 2, 339,339], 3, width=5, outline="darkorchid2", fill="lavender")
my_rectangle = roundPolygon(c1,[100,250,250,100], [25,25,75,75], 5, width=5, outline="coral3", fill="coral3")
my_rectangle = roundPolygon(c2,[100,250,250,100], [25,25,75,75], 5, width=5, outline="deep pink", fill="deep pink")
my_rectangle = roundPolygon(c3,[100,250,250,100], [25,25,75,75], 5, width=5, outline="steel blue", fill="steel blue")
my_rectangle = roundPolygon(c4,[100,250,250,100], [25,25,75,75], 5, width=5, outline="darkorchid2", fill="darkorchid2")

#Loading the image paths
#Forward Button
image_paths =["C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\green.png",
    "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\peacock.png",
    "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\scarlett.png",
    "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\white.png"]

images = [Image.open(image_path) for image_path in image_paths]

# Create a label to display the image
#Rectangle 1
initial_photo1 = ImageTk.PhotoImage(images[0])
image_label1 = tk.Label(root, image=initial_photo1, relief = SUNKEN)
image_label1.place(x = 470, y = 175)

current_image_index = 0

b1=Button(root,text='←',command=label1back).place(x=375,y=200,relheight=0.038,relwidth=0.022)
b2=Button(root,text='→',command=label1forward).place(x=640,y=200,relheight=0.038,relwidth=0.022)

#Rectangle 2
initial_photo2 = ImageTk.PhotoImage(images[1])
image_label2 = tk.Label(root, image=initial_photo2, relief = SUNKEN)
image_label2.place(x = 970, y = 175)

current_image_index = 0

b3=Button(root,text='←', command = label2back).place(x=875,y=200,relheight=0.038,relwidth=0.022)
b4=Button(root,text='→', command = label2forward).place(x=1140,y=200,relheight=0.038,relwidth=0.022)

#Rectangle 3
initial_photo3 = ImageTk.PhotoImage(images[2])
image_label3 = tk.Label(root, image=initial_photo3, relief = SUNKEN)
image_label3.place(x = 470, y = 575)

current_image_index = 0

b5=Button(root,text='←', command = label3back).place(x=375,y=600,relheight=0.038,relwidth=0.022)
b6=Button(root,text='→', command = label3forward).place(x=640,y=600,relheight=0.038,relwidth=0.022)

#Rectangle 4
initial_photo4 = ImageTk.PhotoImage(images[3])
image_label4 = tk.Label(root, image=initial_photo4, relief = SUNKEN)
image_label4.place(x = 970, y = 575)

current_image_index = 0

b7=Button(root,text='←', command = label4back).place(x=875,y=600,relheight=0.038,relwidth=0.022)
b8=Button(root,text='→', command = label4forward).place(x=1140,y=600,relheight=0.038,relwidth=0.022)

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
cb1.place(x = 440, y = 325)
cb1.set("Select Player...")

#Combobox 2
user2 = tk.StringVar() 
cb2 = ttk.Combobox(root, textvariable = user2)
cb2['values'] = usernames
cb2.place(x = 940, y = 325)
cb2.set("Select Player...")

#Combobox 3
user3 = tk.StringVar() 
cb3 = ttk.Combobox(root, textvariable = user3)
cb3['values'] = usernames
cb3.place(x = 440, y = 725)
cb3.set("Select Player...")

#Combobox 4
user4 = tk.StringVar() 
cb4 = ttk.Combobox(root, textvariable = user4)
cb4['values'] = usernames
cb4.place(x = 940, y = 725)
cb4.set("Select Player...")

players = [user1.get(),user2.get(),user3.get(),user4.get()]

'''
***
This validation is for verifying the data before moving to the next section of our game.
***
if(user1.get() == None or user2.get() == None or user3.get() == None or user4.get() == None or
   user1.get() == "" or user2.get() == "" or user3.get() == "" or user4.get()):
    messagebox.showinfo("","Kindly ensure all the 4 player usernames have been selected")
else:
    for i in players:
        count = 0
        for j in players:
            if(i == j):
                count += 1
        if(count > 1):
            messagebox.showinfo("","No 2 or more player usernames can be the same, kindly ensure all 4 usernames are distinct")
            break
'''   
root.mainloop()
