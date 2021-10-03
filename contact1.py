from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

import about1

def Home():
    global root
    root.destroy()
    import home
def About():
    global root
    root.destroy()
    about1.main_display()
def Contact():
    global root
    root.destroy()
    main_display()
def Exit():
    wayOut = tkinter.messagebox.askyesno("Attendance System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return
def main_display():
    global root
    IMAGE_PATH = "14.jpeg"
    root = Tk()
    root.config(bg="white")
    root.title("Contact Us")
    root.geometry("1400x780")

    img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((1400, 780), Image.ANTIALIAS))

    label = Label(root,image=img)
    label.place(x=0, y=0)
    
    l1= Label(root,text='Advance Facial Recognition Employee Attendance System',  bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",width=100)
    l1.place(x=-160,y=0)
    
    b1=Button(root,text='Home', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",command=Home)
    b1.place(x=150,y=100)
    
    b2=Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",command=Exit)
    b2.place(x=150,y=150)
    
    var="""BCREC Help Line No : 8800443456
 	CONTACT
Registered Office
Dr. B.C. Roy Engineering College, Durgapur
"Management House"
Jemua Road, Fuljhore
Durgapur - 713206 (W.B.)

College Campus/Corporate Office
Jemua Road, Fuljhore
Durgapur – 713206
Phone No.- 0343- 250-1353/ 2449 / 3985 / 3360 / 4224 / 4106
Mobile No.- +91- 6297128554
Fax No.- 0343- 2504059 / 2503424
E-mail -  info@bcrec.ac.in


College Timings : TUESDAY TO SATURDAY (10:00 AM to 5:30 PM)
Sunday & Monday : Closed"""
    m1=Message(root,text=var)
    m1.place(x=80,y=200)
    root.mainloop()
