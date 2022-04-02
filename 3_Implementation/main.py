# Student Complaint Management System

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from DBase import DBaseConnect
from ListofComp import ListofComp

#Configaration
conn = DBaseConnect()
ws = Tk()
ws.geometry('550x300') #window size
ws.title('Student Complaint Management')
ws.configure(bg='silver')

#Gridx1353
labels = ['Name of Student:', 'Gender:', 'Comment:']
for i in range(3):
	Label(ws, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)

# Student Entries
NameofStudent = Entry(ws, width=35, font=('Ariel', 14))
NameofStudent.grid(row=0, column=1, columnspan = 2, sticky=W )
SpanGender = StringVar()
Radiobutton(ws, text='Male', value='male', variable=SpanGender).grid(row=1, column=1)
Radiobutton(ws, text='Female', value='female', variable=SpanGender).grid(row=1, column=2)

comment = Text(ws, width=30, height=5, font=('Ariel', 14))
comment.grid(row=2, column=1, columnspan=2, pady=10, sticky=W)

BuList = Button(ws, text='List of Comments.')
BuList.grid(row=4, column=1, sticky=W )
BuSubmit = Button(ws, text='Submit Now')
BuSubmit.grid(row=4, column=2,  sticky=W )

def SaveData():
 msg = conn.Add(NameofStudent.get(), SpanGender.get(), comment.get(1.0, 'end'))  #get() returns the value
 NameofStudent.delete(0, 'end')       #.del() clear the widget after the button is pressed
 comment.delete(1.0, 'end')
 showinfo(title='Add Info', message=msg)

def ShowList():
  listrequest = ListofComp

BuSubmit.config(command=SaveData)
BuList.config(command=ShowList)

ws.mainloop()
