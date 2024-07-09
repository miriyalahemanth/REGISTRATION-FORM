from tkinter import *
from tkinter import messagebox
import mysql.connector
window=Tk()
window.geometry("1000x600")
window.resizable(False,False)
window.title("Student Registration Form")
window['bg']="blue"
#window.iconbitmap("registra")
#variables
fname=StringVar()
lname=StringVar()
age=IntVar()
gender=StringVar()
s1=IntVar()
s2=IntVar()
s3=IntVar()
s4=IntVar()
email=StringVar()

#Actions
def insertion():
    fn=fname.get()
    ln=lname.get()
    sage=age.get()
    sgender=gender.get()
    scourses=[]
    if s1.get()==1:
        scourses.append("Python")
    else:
        pass
    if s2.get()==1:
        scourses.append("Java")
    else:
        pass
    if s3.get()==1:
        scourses.append("Django")
    else:
        pass
    if s4.get()==1:
        scourses.append("Flask")
    else:
        pass
    course=",".join(scourses)
    semail=email.get()
        
    conn_obj=mysql.connector.connect(user='root',password='hemanth',
            host='localhost',port='3306',database="studentHemanth_db1")
    cur_obj=conn_obj.cursor()
    cur_obj.execute("insert into studentreg(fname,lname,age,gender,courses,email)\
 values(%s,%s,%s,%s,%s,%s)",(fn,ln,sage,sgender,course,semail))
    cur_obj.execute("commit")
    cur_obj.close()
    conn_obj.close()
    messagebox.showinfo("result","inserted successfully")
    
        

def clear():
   res=messagebox.askquestion("clear the fields","do you want to really clear the fields?")
   if res=='yes':
       fname.set('')
       lname.set('')
       age.set('')
       gender.set('')
       email.set('')
   else:
       pass

def destroy():
    res=messagebox.askquestion("close the window",
                               "do you want to really close the window?")
    if res=='yes':
        window.destroy()
    else:
        pass
#top frame
top_frame=Frame(window,width=980,height=50,bg="white")
top_frame.place(x=10,y=10)
L=Label(top_frame,text="Welcome To Registration",fg="red",bg="white",
         font="arial 20 italic")
L.place(x=200,y=10)



#center frame
center_frame=Frame(window,width=600,height=450,bg="white")
center_frame.place(x=200,y=75)
L1=Label(center_frame,text="Enter First Name:",bg="white",fg="purple",
         font="elephant 15 bold")
L1.place(x=5,y=5)
E1=Entry(center_frame,bd=3,bg="white",fg="orange",font="arial 15 bold",
         textvariable=fname)
E1.place(x=300,y=5)

L2=Label(center_frame,text="Enter Last Name:",bg="white",fg="purple",
         font="elephant 15 bold")
L2.place(x=5,y=45)
E2=Entry(center_frame,bd=3,bg="white",fg="orange",font="arial 15 bold",
         textvariable=lname)
E2.place(x=300,y=45)

L3=Label(center_frame,text="Enter Your Age:",bg="white",fg="purple",
         font="elephant 15 bold")
L3.place(x=5,y=85)
S3=Spinbox(center_frame,from_=0,to=100,bg="white",fg="orange",
           font="arial 15 bold",textvariable=age)
S3.place(x=300,y=85)

L4=Label(center_frame,text="Choose Your Gender:",bg="white",fg="purple",
         font="elephant 15 bold")
L4.place(x=5,y=125)
R1=Radiobutton(center_frame,text="Male",bg="white",fg="orange",
               font="elephant 15 bold",value="male",variable=gender)
R1.place(x=300,y=125)
R2=Radiobutton(center_frame,text="Female",bg="white",fg="orange",
               font="elephant 15 bold",value="female",variable=gender)
R2.place(x=450,y=125)      


L5=Label(center_frame,text="Select Your Courses:",bg="white",fg="purple",
         font="elephant 15 bold")
L5.place(x=5,y=165)
C1=Checkbutton(center_frame,text="Python",bg="white",fg="orange",
         font="elephant 15 bold",variable=s1)
C1.place(x=300,y=165)
C2=Checkbutton(center_frame,text="Java",bg="white",fg="orange",
         font="elephant 15 bold",variable=s2)
C2.place(x=450,y=165)
C3=Checkbutton(center_frame,text="Django",bg="white",fg="orange",
         font="elephant 15 bold",variable=s3)
C3.place(x=300,y=205)
C4=Checkbutton(center_frame,text="Flask",bg="white",fg="orange",
         font="elephant 15 bold",variable=s4)
C4.place(x=450,y=205)

L6=Label(center_frame,text="Enter Your Email",bg="white",fg="purple",
         font="elephant 15 bold")
L6.place(x=5,y=245)
E3=Entry(center_frame,bd=3,bg="white",fg="orange",font="arial 15 bold",
         textvariable=email)
E3.place(x=300,y=245)

B1=Button(center_frame,text="Insert",bg="white",fg="purple",
         font="elephant 15 bold",command=insertion)
B1.place(x=150,y=300)

B2=Button(center_frame,text="Clear",bg="white",fg="purple",
         font="elephant 15 bold",command=clear)
B2.place(x=300,y=300)

B3=Button(center_frame,text="Destroy",bg="white",fg="purple",
         font="elephant 15 bold",command=destroy)
B3.place(x=450,y=300)

window.mainloop()
