from tkinter import * # GUI
import tkinter.messagebox #POPUP
from PIL import Image, ImageTk
import tkinter as tk
def Home():
    global root
    root.destroy()
    main_display()

def main_display():
    global root
    IMAGE_PATH = "C:\\Users\\DELL\\Desktop\\Face_recognition_based_attendance_system (2)\\Face_recognition_based_attendance_system\\1.jpg"
    root = Tk()
    root.config(bg="white")
    root.title("Face Recognition Based Attendance System")
    root.geometry("1400x780")
    """canvas = Canvas(root, width=1400, height=780)
    

    img = root.PhotoImage(file = IMAGE_PATH)
    bg1 = root.Lable(root,image = img)
    bg1.place(x = 0, y = 0, relwidth = 1, relhight = 1)
    canvas.pack()
    canvas.background = img  # Keep a reference in case this code is put in a function.
    bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)"""
    
    l1=Label(root,text='Face Recognition Based Attendance System',  bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",width=300).pack()
    #canvas.create_window(10, 10, anchor=tk.NW, window=l1)
    Label(root,text="").pack()
    Button(root,text='Home', height="1",width="20",bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",command=Home).pack()
    Label(root,text="").pack()
    
    root.mainloop()
#main code here
main_display()

