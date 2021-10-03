from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import pymysql


#connecting to the database
connectiondb = pymysql.connect(host="localhost",user="root",passwd="",database="attendence")
cursordb = connectiondb.cursor()


def login():
    global root2
    IMAGE_PATH = "13.jpeg"
    img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((1400, 780), Image.ANTIALIAS))

    root2 = Toplevel(root)
    root2.title("Account Login")
    root2.geometry("1400x780")
    root2.config(bg="white")
    label = Label(root2,image=img)
    label.place(x=0, y=0)
    

    global username_verification
    global password_verification
    l11=Label(root2, text='Please Enter your Account Details', bd=20,font=('arial', 20, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",width=100)
    l11.place(x=-160,y=0)
    username_verification = StringVar()
    password_verification = StringVar()
    
    l12=Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold'))
    l12.place(x=640,y=100)
    e1=Entry(root2, textvariable=username_verification)
    e1.place(x=640,y=150)
    
    l13=Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold'))
    l13.place(x=640,y=200)
    e2=Entry(root2, textvariable=password_verification, show="*")
    e2.place(x=640,y=250)
    
    b11=Button(root2, text="Login", bg="#00aeff", fg='white', relief="groove", font=('arial', 12, 'bold'),command=login_verification)
    b11.place(x=640,y=300)

    canvas = Canvas(root2,width=10, height=10)
    canvas.place(x=1000, y=1000)
    img1=tkinter.PhotoImage(file=IMAGE_PATH)
    canvas.create_Image(10,10,image=img1)
    

def logged_destroy():
    logged_message.destroy()
    root2.destroy()

def failed_destroy():
    failed_message.destroy()

def logged():
    global logged_message
    global root
    root.destroy()
    import main
    logged_message = Toplevel(root2)
    logged_message.title("Welcome")
    logged_message.geometry("500x100")
    Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="green", font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Logout", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=logged_destroy).pack()


def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message,text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=failed_destroy).pack()


def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from admin where adminid = %s and password = %s"
    cursordb.execute(sql,[(user_verification),(pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return

def main_display():
    global root
    IMAGE_PATH = "12.jpeg"
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("1400x780")

    img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((1400, 780), Image.ANTIALIAS))

    label = Label(root,image=img)
    label.place(x=0, y=0)
    
    l1=Label(root,text='Welcome to Log In System',  bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",width=100)
    l1.place(x=-180,y=0)
    
    b1=Button(root,text='Log In', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",command=login)
    b1.place(x=755,y=100)
    
    b2=Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="#00aeff",command=Exit)
    b2.place(x=755,y=150)
    root.mainloop()

main_display()
