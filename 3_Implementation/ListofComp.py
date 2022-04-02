from tkinter import *
from tkinter.ttk import *
from DBase import DBaseConnect
import sqlite3

class ListofComp:
    def __init__(self):
        self._DBaseconnect = DBaseConnect()
        self._DBaseconnect.row_factory = sqlite3.Row
        self._ws = Tk()
        self._ws.title('List of Complaints')
        tv = Treeview(self._ws)
        tv.pack()                                    # treeview /layout manager
        tv.heading('#0', text='ID')
        tv.configure(column=('#NameofStudent', '#Gender', '#Comment'))   # no of columns
        tv.heading('#NameofStudent', text='NameofStudent')
        tv.heading('#Gender', text='Gender')
        tv.heading('#Comment', text='Comment')
        cursor = self._DBaseconnect.ListRequest()
        for row in cursor:
            tv.insert('', 'end', '#{}'.format(row['ID']), text=row['ID'])
            tv.set('#{}'.format(row['ID']), '#NameofStudent', row['NameofStudent'])
            tv.set('#{}'.format(row['ID']), '#Gender', row['Gender'])
            tv.set('#{}'.format(row['ID']), '#Comment', row['Comment'])

