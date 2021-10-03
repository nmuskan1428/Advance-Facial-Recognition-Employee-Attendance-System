from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import contact1

def Home():
    global root
    root.destroy()
    import home
def About():
    global root
    root.destroy()
    main_display()
def Contact():
    global root
    root.destroy()
    contact1.main_display()
def Exit():
    wayOut = tkinter.messagebox.askyesno("Attendance System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return
def main_display():
    global root
    IMAGE_PATH = "10.jpeg"
    root = Tk()
    root.config(bg="white")
    root.title("About Us")
    root.geometry("1400x780")

    img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((1400, 780), Image.ANTIALIAS))

    label = Label(root,image=img)
    label.place(x=0, y=0)
    
    l1=Label(root,text='Advance Facial Recognition Employee Attendance System',  bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",width=100)
    l1.place(x=-100,y=0)
    
    b1=Button(root,text='Home', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",command=Home)
    b1.place(x=600,y=100)
    
    b2=Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",command=Exit)
    b2.place(x=600,y=150)
    
    m1=Message(root,text="Dr. B.C. Roy Engineering College, Durgapur, popularly known as BCREC, was set up on 21st August, 2000, under the over all management of Dr. B.C. Roy Engineering College Society. Born of a vision of a group of Durgapur based philanthropic entrepreneurs, the institute is dedicated to the memory of Dr. Bidhan Chandra Roy, the architect of modern West Bengal and BCREC management is deeply committed to gradually build the college as one of the best seats of Engineering and Management  Education in Eastern India with domestic and global requirements in view.")
    m1.place(x=570,y=200)
    root.mainloop()
    
