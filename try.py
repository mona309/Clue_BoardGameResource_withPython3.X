from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time

  
def logo4():
  global lg4
  image_pathl4 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\preview(4).png"
  lg4 = ImageTk.PhotoImage(Image.open(image_pathl4))
  
  l4 = tk.Label(root, image=lg4, bg = "DarkGoldenRod1")
  l4.place(x = 430, y = 120)
  root.after(500, l4.destroy)
  
def logo3():
  global lg3
  image_pathl3 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\preview(3).png"
  lg3 = ImageTk.PhotoImage(Image.open(image_pathl3))
  
  l3 = tk.Label(root, image=lg3, bg = "DarkGoldenRod1")
  l3.place(x = 495, y = 160)
  root.after(500, l3.destroy)
  
def logo2():
  global lg2
  image_pathl2 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\preview(2).png"
  lg2 = ImageTk.PhotoImage(Image.open(image_pathl2))
  
  l2 = tk.Label(root, image=lg2, bg = "DarkGoldenRod1")
  l2.place(x = 560, y = 215)
  root.after(500, l2.destroy)
  
def logo1():
  global lg1
  image_pathl1 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\preview(1).png"
  lg1 = ImageTk.PhotoImage(Image.open(image_pathl1))
  
  l1 = tk.Label(root, image=lg1, bg = "DarkGoldenRod1")
  l1.place(x = 625, y = 270)
  root.after(500, l1.destroy)
  
def displayLabel11():
  global img12
  image_path12 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\pixil-frame-0(1)(3).png"
  img12 = ImageTk.PhotoImage(Image.open(image_path12))
  
  label12 = tk.Label(root, image=img12,bg = "DarkGoldenRod1")
  label12.place(x = 1020, y = 180)
  root.after(500, label12.destroy)
  
def displayLabel10():
  global img11
  image_path11 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\pixil-frame-0(2)(3).png"
  img11 = ImageTk.PhotoImage(Image.open(image_path11))
  
  label11 = tk.Label(root, image=img11,bg = "DarkGoldenRod1")
  label11.place(x = 1020, y = 205)
  root.after(500, label11.destroy)
  
def displayLabel9():
  global img10
  image_path10 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\pixil-frame-0(3)(3).png"
  img10 = ImageTk.PhotoImage(Image.open(image_path10))
  
  label10 = tk.Label(root, image=img10,bg = "DarkGoldenRod1")
  label10.place(x = 1020, y = 230)
  root.after(500, label10.destroy)
  
def displayLabel8():
  global img9
  image_path9 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\pixil-frame-0(3)(2).png"
  img9 = ImageTk.PhotoImage(Image.open(image_path9))
  
  label9 = tk.Label(root, image=img9,bg = "DarkGoldenRod1")
  label9.place(x = 1020, y = 595)
  root.after(500, label9.destroy)

def displayLabel7():
  global img8
  image_path8 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\pixil-frame-0(4)(2).png"
  img8 = ImageTk.PhotoImage(Image.open(image_path8))
  
  label8 = tk.Label(root, image=img8,bg = "DarkGoldenRod1")
  label8.place(x = 1045, y = 595)
  root.after(500, label8.destroy)
  
def displayLabel6():
  global img7
  image_path7 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\pixil-frame-0(5)(2).png"
  img7 = ImageTk.PhotoImage(Image.open(image_path7))
  
  label7 = tk.Label(root, image=img7,bg = "DarkGoldenRod1")
  label7.place(x = 1070, y = 595)
  root.after(500, label7.destroy)

def displayLabel5():
  global img6
  image_path6 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\pixil-frame-0(3)(1).png"
  img6 = ImageTk.PhotoImage(Image.open(image_path6))
  
  label6 = tk.Label(root, image=img6,bg = "DarkGoldenRod1")
  label6.place(x = 450, y = 140)
  root.after(500, label6.destroy)
  
def displayLabel4():
  global img5
  image_path5 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\pixil-frame-0(2)(1).png"
  img5 = ImageTk.PhotoImage(Image.open(image_path5))
  
  label4 = tk.Label(root, image=img5,bg = "DarkGoldenRod1")
  label4.place(x = 425, y = 140)
  root.after(500, label4.destroy)
  
def displayLabel3():
  global img4
  image_path4 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\pixil-frame-0(1)(1).png"
  img4 = ImageTk.PhotoImage(Image.open(image_path4))
  
  label4 = tk.Label(root, image=img4,bg = "DarkGoldenRod1")
  label4.place(x = 400, y = 140)
  root.after(500, label4.destroy)
  
def displayLabel2():
  global img3
  image_path3 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\pixil-frame-4(1).png"
  img3 = ImageTk.PhotoImage(Image.open(image_path3))
  
  label3 = tk.Label(root, image=img3,bg = "DarkGoldenRod1")
  label3.place(x = 400, y = 550)
  root.after(500, label3.destroy)
  
def displayLabel1():
  global img2
  image_path2 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\pixil-frame-1(1).png"
  img2 = ImageTk.PhotoImage(Image.open(image_path2))
  
  label2 = tk.Label(root, image=img2,bg = "DarkGoldenRod1")
  label2.place(x = 400, y = 575)
  root.after(500, label2.destroy)
  
# Create the main window
root = tk.Tk()
root.title("Loading-Page...")
root.geometry('2000x1000')
root.configure(bg = "black")

Label(text = "", font = ("Calibri 6"), bg = "black").pack()
c = Canvas(root, height = 25, width = 50)
filename = PhotoImage(file = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\map.png",master=root)
background_label = Label(root, image = filename,bg = "black").pack()
#background_label.place(x=0,y=0,relwidth=1,relheight=1)
#c.pack()

#Label with picture
#Set 1
image_path1 = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\pixil-frame-0(1).png"
img1 = Image.open(image_path1)
img1 = ImageTk.PhotoImage(img1)

label1 = tk.Label(root, image=img1, bg = "DarkGoldenRod1")
label1.place(x = 400, y = 600)

root.after(500, label1.destroy)
root.after(500, displayLabel1)
root.after(1000, displayLabel2)

#Set 2
root.after(1500, displayLabel3)
root.after(2000, displayLabel4)
root.after(2500, displayLabel5)

#Set 3
root.after(3000, displayLabel6)
root.after(3500, displayLabel7)
root.after(4000, displayLabel8)

#Set 4
root.after(4500, displayLabel11)
root.after(5000, displayLabel10)
root.after(5500, displayLabel9)

#Logo Display
root.after(6000, logo1)
root.after(6500, logo2)
root.after(7000, logo3)
root.after(7500, logo4)

#Closing the window
root.after(8000, root.destroy)
root.mainloop()