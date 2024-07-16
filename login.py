import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

def register_user():
  n=name.get() 
  p=password.get()
  a = age.get()
  u = user.get()
  c = confirm.get()

  
  if(n.isalpha() is False or a.isdigit() is False or
     n is None or p is None or a is None or u is None or c is None or
     n == "" or p == "" or a == "" or u == "" or c == ""):
    messagebox.showinfo("","Kindly enter valid information")
  else:
    flag = 0
     
    try:
      fr = open((u+".txt"),"r")
      flag = 1
      fr.close()
    except FileNotFoundError:
      flag = 0
      
    counter = 0

    if(flag == 1):
      messagebox.showinfo("","Username already exists, kindly enter another username")
    else:
      if(n.isalpha() is True and a.isdigit() is True):
        if(p == c and int(a) >= 10):
          counter = 1
        elif(p != c):
          messagebox.showwarning("","Password and confirm password does not match, kindly check")
        elif(age < 10):
          messagebox.showinfo("","The players must be at least 10 years to play")
    
    if(counter == 1):
      fw = open(u+".txt","w")
      fw.write(n+","+u+","+p)
      fw.close()
      
      fileName = open("Player-Data.txt","a")
      fileName.write(n+","+a+","+u)
      fileName.write("\n")
      fileName.close()
      messagebox.showinfo("","Registration Successful")
      root1.withdraw()

      login()
    else:
      messagebox.showwarning("","Registration Unsuccessful")
    
def login_verify():
  name1=user_verify.get()
  password1=password_verify.get()

  if(name1 is None or password1 is None or
     name1 == "" or password1 == ""):
    messagebox.showinfo("","Kindly enter valid information")
  else:
    try:
      fr = open((name1+".txt"),"r")
      data = fr.read().split(",")
      flag = 0
      if(password1 == data[2]):
        flag = 1
      if(flag == 1):
        messagebox.showinfo("","Login Successful")
        root.destroy()
        #open the next section
      else:
        messagebox.showinfo("","Login Unsuccessful, Incorrect Password")
    except FileNotFoundError:
      messagebox.showwarning("","User does not exist")
    
def back2():
  root1.destroy()
  mainscreen()
    
def register():
  global root1,name,password,age,user,confirm
  global n_entry,p_entry,a_entry,u_entry,c_entry
  
  root1=Toplevel(root)
  name=StringVar()
  password=StringVar()
  age=StringVar()
  user=StringVar()
  confirm=StringVar()
  
  root1.geometry('1600x900')

  c = Canvas(root1, height = 25, width = 50)
  filename = PhotoImage(file="/home/monisha/myprojects/alibiforsaken/reg.png",master=root1)
  background_label = Label(root1, image = filename)
  background_label.place(x=0,y=0,relwidth=1,relheight=1)
  c.pack()

  #Add a frame for the widgets
  Label(root1,text="REGISTRATION",font=("Calibri 30"),bg = "black",fg = "white").place(x = 900, y = 300)
  
  Label(root1, text = "Please enter the following details",font=("Calibri 18"),bg = "black",fg = "white").place(x = 865, y = 340)

  Label(root1,text="Name",font=("Calibri 20"),bg = "black",fg = "white").place(x = 765, y = 365)
  n_entry=Entry(root1,textvariable=name,font = ("Calibri 20")).place(x = 940, y = 365) 
  
  Label(root1, text = "Age",font = ("Calibri 20"), bg = "black",fg = "white").place(x = 765, y = 415)
  a_entry=Entry(root1, textvariable=age,font = ("Calibri 20")).place(x = 940, y = 415)
  
  Label(root1, text = "Please enter the following account details",font = ("Calibri 18"),bg = "black",fg = "white").place(x = 840, y = 465)
  
  Label(root1,text = "Username",font = ("Calibri 20"),bg = "black",fg = "white").place(x =765, y = 490)
  u_entry=Entry(root1,textvariable=user,font = ("Calibri 20")).place(x = 940, y = 490)
  
  Label(root1,text="Password",font=("Calibri 20"),bg = "black",fg = "white").place(x = 765, y = 540)
  p_entry=Entry(root1,textvariable=password,font = ("Calibri 20"),show = "*").place(x = 940, y = 540)
  
  Label(root1, text = "Confirm Password",font = ("Calibri 20"),bg = "black",fg = "white").place(x = 765, y = 590)
  c_entry=Entry(root1,textvariable = confirm,font = ("Calibri 20"),show = "*").place(x = 940, y = 590)

  button=Button(root1,text="Register",command=lambda:register_user(),font=("Calibri 18"),bg = "white").place(x = 1000, y = 640)
  
  backbtn=Button(root1,text="Back to Main Menu",command=lambda:back2(),font=("Calibri 10")).place(x = 1500, y = 30)
  root.withdraw()
  root1.mainloop()

def back1():
  root2.destroy()
  mainscreen()
    
def login():
  global root2,u_entry1,p_entry1
  global user_verify,password_verify
  
  user_verify=StringVar()
  password_verify=StringVar()
  
  root2=Toplevel(root)
  root2.title("Login")
  root2.geometry('1600x900')

  c = Canvas(root2, height = 25, width = 50)
  filename = PhotoImage(file="/home/monisha/myprojects/alibiforsaken/login.png",master=root2)
  background_label = Label(root2, image = filename)
  background_label.place(x=0,y=0,relwidth=1,relheight=1)
  c.pack()

  #Add a frame into which all the labels and entry would be in
  Label(root2, text = "LOGIN",font = ("Calibri 30"),bg = "black",fg = "white").place(x = 790, y = 295)
  
  Label(root2,text="Username",font = ("Calibri 20"),bg = "black",fg = "white").place(x = 650, y = 350)
  u_entry1=Entry(root2,textvariable=user_verify,font = ("Calibri 20")).place(x = 770, y = 350)
  
  Label(root2,text="Password",font=("Calibri 20"),bg = "black",fg = "white").place(x = 650, y = 390)
  p_entry1=Entry(root2,textvariable=password_verify,font = ("Calibri 20"),show="*").place(x = 770, y = 390)
                                                        
  button1=Button(root2,text="Login",command=lambda:login_verify(),font=("Calibri 18"),bg = "white").place(x = 810, y = 443)

  backbtn=Button(root2, text = "Back to Main Menu",command=lambda:back1(),font=("Calibri 10")).place(x = 1350,y = 0)
  
  root.withdraw()
  root2.mainloop()

def mainscreen():
  global root,screen_w,screen_h,x,y
  root=Tk()
  screen_w=root.winfo_screenwidth()
  screen_h=root.winfo_screenheight()
  
  root.title("Register-Login")
  root.geometry('1600x900')

  c = Canvas(root, height = 25, width = 50)
  filename = PhotoImage(file="/home/monisha/myprojects/alibiforsaken/start1.png",master=root)
  background_label = Label(root, image = filename)
  background_label.place(x=0,y=0,relwidth=1,relheight=1)
  c.pack()

  heading=tkinter.Label(root,text="LOGIN-REGISTER PAGE",font=("Calibri 30"),bg = "black",fg = "white").place(x = 800, y = 400)
  login_button=tkinter.Button(root,text="Login",font=("Calibri 20"),command=lambda:login(),bg = "white").place(x = 850, y = 450)
  register_button=tkinter.Button(root,text="Register",font=("Calibri 20"),command=lambda:register(),bg = "white").place(x = 1000, y = 450)
  
  root.mainloop()
mainscreen()