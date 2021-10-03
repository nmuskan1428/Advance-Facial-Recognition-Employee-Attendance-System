from tkinter import * # GUI
import tkinter.messagebox #POPUP
import about1
import contact1
from PIL import Image, ImageTk
import tkinter as tk

def Home():
    global root
    root.destroy()
    main_display()
def About():
    global root
    root.destroy()
    about1.main_display()
def Contact():
    global root
    root.destroy()
    contact1.main_display()

def Attandance():
    global root
    root.destroy()
    import check

def Login():
    global root
    root.destroy()
    import login
    
def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return
def main_display():
    global root
    IMAGE_PATH = "11.jpeg"
    root = Tk()
    root.config(bg="white")
    root.title("Advance Facial Recognition Employee Attendance System")
    root.geometry("1400x780")
    

    img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((1400, 780), Image.ANTIALIAS))

    label = Label(root,image=img)
    label.place(x=0, y=0)
    
    

    l1=Label(root,text='Advance Facial Recognition Employee Attendance System',  bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",width=100)
    l1.place(x=-110, y=0)

    
    b1=Button(root,text='Home', height="1",width="20",bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",command=Home)
    b1.place(x=600,y=100)
    
    b2=Button(root,text='Take Attandance', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",command=Attandance)
    b2.place(x=600,y=150)
    
    b3= Button(root,text='About', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",command=About)
    b3.place(x=600,y=200)
    
    b4=Button(root,text='Contact', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",command=Contact)
    b4.place(x=600,y=250)
   
    
    b5=Button(root,text='Admin Login', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",command=Login)
    b5.place(x=600,y=300)
    

    b6=Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",command=Exit)
    b6.place(x=600,y=350)
    
    root.mainloop()
#main code here
main_display()
