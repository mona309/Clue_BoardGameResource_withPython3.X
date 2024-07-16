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
  
  space = 0
  
  for i in n:
    if(i == " "):
      space = 1
      break
  if(space == 1):
    NAME = n.split(" ")
  else:
    NAME = n.split()
  N = 0
  for i in NAME:
    if(i.isalpha() is True):
      N += 1
      
  if(N != len(NAME) or a.isdigit() is False or
     n is None or p is None or a is None or u is None or c is None or
     a == "" or u == "" or n == "" or c == "" or p == ""):
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
      root1.destroy()
      log = 1
      register()
    else:
      if(N == len(NAME) and a.isdigit() is True):
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
      root1.destroy()
      login()
    else:
      messagebox.showwarning("","Registration Unsuccessful")
    
def login_verify():
  USERNAME = user_verify.get()
  PASSWORD = password_verify.get()

  if(USERNAME is None or PASSWORD is None or
     USERNAME == "" or PASSWORD == ""):
    messagebox.showinfo("","Kindly enter valid information")
  else:
    try:
      fr = open((USERNAME+".txt"),"r")
      data = fr.read().split(",")
      flag = 0
      if(PASSWORD == data[2]):
        flag = 1
      if(flag == 1):
        messagebox.showinfo("","Login Successful")
        root.destroy()
        os.startfile("Loading-Page.py")
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
  
  root1.title("Register")
  root1.geometry('2000x1000')
  root1.configure(bg = "black")
  
  bg = PhotoImage(file = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\register - Copy.png",master=root1)
  Label(root1, image = bg,bg = "black").pack()

  Label(root1,text="REGISTRATION",font=("Calibri 30"),bg = "black",fg = "white").place(x = 720, y = 225)
  Label(root1, text = "Please enter the following details",font=("Calibri 18"),bg = "black",fg = "white").place(x = 680, y = 275)

  Label(root1,text="Name",font=("Calibri 20"),bg = "black",fg = "white").place(x = 660, y = 310)
  n_entry=Entry(root1,textvariable=name,font = ("Calibri 20")).place(x = 740, y = 310) 
  
  Label(root1, text = "Age",font = ("Calibri 20"), bg = "black",fg = "white").place(x = 660, y = 349)
  a_entry=Entry(root1, textvariable=age,font = ("Calibri 20")).place(x = 740, y = 349)
  
  Label(root1, text = "Please enter the following account details",font = ("Calibri 18"),bg = "black",fg = "white").place(x = 650, y = 389)
  
  Label(root1,text = "Username",font = ("Calibri 20"),bg = "black",fg = "white").place(x = 650, y = 425)
  u_entry=Entry(root1,textvariable=user,font = ("Calibri 20")).place(x = 770, y = 425)
  
  Label(root1,text="Password",font=("Calibri 20"),bg = "black",fg = "white").place(x = 650, y = 465)
  p_entry=Entry(root1,textvariable=password,font = ("Calibri 20"),show = "*").place(x = 770, y = 465)
  
  Label(root1, text = "Confirm Password",font = ("Calibri 20"),bg = "black",fg = "white").place(x = 555, y = 505)
  c_entry=Entry(root1,textvariable = confirm,font = ("Calibri 20"),show = "*").place(x = 770, y = 505)

  button=Button(root1,text="Register",command=lambda:register_user(),font=("Calibri 18"),bg = "white").place(x = 770, y = 550)
  
  backbtn=Button(root1,text="Back to Main Menu",command=lambda:back2(),font=("Calibri 10")).place(x = 1373, y = 0)
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
  root2.geometry('2000x1000')
  root2.configure(bg = "black")
  
  bg = PhotoImage(file = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\login - Copy.png",master=root2)
  Label(root2, image = bg, bg = "black").pack()

  Label(root2, text = "LOGIN",font = ("Calibri 30"),bg = "black",fg = "white").place(x = 735, y = 285)
  
  Label(root2,text="Username",font = ("Calibri 20"),bg = "black",fg = "white").place(x = 630, y = 350)
  u_entry1=Entry(root2,textvariable=user_verify,font = ("Calibri 20")).place(x = 750, y = 350)
  
  Label(root2,text="Password",font=("Calibri 20"),bg = "black",fg = "white").place(x = 630, y = 390)
  p_entry1=Entry(root2,textvariable=password_verify,font = ("Calibri 20"),show="*").place(x = 750, y = 390)

  button1=Button(root2,text="Login",command=lambda:login_verify(),font=("Calibri 18"),bg = "white").place(x = 750, y = 435)

  backbtn=Button(root2, text = "Back to Main Menu",command=lambda:back1(),font=("Calibri 10")).place(x = 1353,y = 0)
  
  root.withdraw()
  root2.update()
  root2.mainloop()

def mainscreen():
  global root,screen_w,screen_h,x,y
  root=Tk()
  root.geometry('2000x1000')
  root.configure(bg = "black")
  
  screen_w=root.winfo_screenwidth()
  screen_h=root.winfo_screenheight()
  
  root.title("Register-Login")

  bg = PhotoImage(file = "C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\start1.png",master=root)
  label1 = Label(root, image = bg, bg = "black")
  label1.pack()
  
  heading=Label(root,text="LOGIN-REGISTER PAGE",font=("Calibri 30"),bg = "black",fg = "white").place(x = 600, y = 300)
  login_button=Button(root,text="Login",font=("Calibri 20"),command=lambda:login(),bg = "white").place(x = 690, y = 360)
  register_button=Button(root,text="Register",font=("Calibri 20"),command=lambda:register(),bg = "white").place(x = 775, y = 360)
  
  root.mainloop()
mainscreen()
