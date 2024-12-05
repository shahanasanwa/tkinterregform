from tkinter import *
from tkinter import messagebox
import sqlite3


dbexist=False

#function to create the sqlite3 database and tables
def createdb():
    global dbexist
    if dbexist:
        db=sqlite3.connect("employeedb.db")
        print(db)
        crsr=db.cursor()
        crsr.execute("create table employee(id integer primary key autoincrement,name text not null,email text not null,phoneno integer not null,username text unique not null,password text not null)")
        print("table is created")
        db.commit()
        db.close()
        dbexist=True


#function to save data int database
def regemp():
    name=en1.get()
    email=en2.get()
    phoneno=en3.get()
    username=en4.get()
    password=en5.get()

    if not(name and email and phoneno and username and password):
        messagebox.showerror("empty fields","all fields are required")
        return
    else:
        db=sqlite3.connect("employeedb.db")
        crsr=db.cursor()
        crsr.execute("insert into employee(name,email,phoneno,username,password)values(?,?,?,?,?)",(name,email,phoneno,username,password))
        db.commit()
        crsr.execute("select * from employee")
        x=crsr.fetchall()
        print(x)
        db.close()

#initialize database
createdb()


#create tkinte window
x=Tk()
x.title("EMPLOYEE REGISTRATION")
x.geometry("500x500")
x.configure(bg="lightgrey")


title=Label(x,text="REGISTRATION FORM",bg="lightgrey",font=("arial",15,"bold"),fg="brown")
title.grid(row=0,column=1)


lb1=Label(x,text="Name",padx=10,pady=5,bg="lightgrey",fg="black",font=("verdana",10,"normal"))
lb1.grid(row=1,column=0,padx=10,pady=5)

en1=Entry(x,width=30)
en1.grid(row=1,column=1)

lb2=Label(x,text="Email",padx=10,pady=5,bg="lightgrey",fg="black",font=("verdana",10,"normal"))
lb2.grid(row=2,column=0)

en2=Entry(x,width=30)
en2.grid(row=2,column=1)

lb3=Label(x,text="Phoneno",padx=10,pady=5,bg="lightgrey",fg="black",font=("verdana",10,"normal"))
lb3.grid(row=3,column=0)

en3=Entry(x,width=30)
en3.grid(row=3,column=1)

lb4=Label(x,text="Username",padx=10,pady=5,bg="lightgrey",fg="black",font=("verdana",10,"normal"))
lb4.grid(row=4,column=0)

en4=Entry(x,width=30)
en4.grid(row=4,column=1)

lb5=Label(x,text="Password",padx=10,pady=5,bg="lightgrey",fg="black",font=("verdana",10,"normal"))
lb5.grid(row=5,column=0)

en5=Entry(x,width=30)
en5.grid(row=5,column=1)

lb6=Label(x,text="",bg="lightgrey")
lb6.grid(row=6,column=1)

btn1=Button(x,text="REGISTER",font=("arial",10,"bold"),padx=10,pady=5,command=regemp,bg="green",fg="white")
btn1.grid(row=7,column=1)

x.mainloop()

