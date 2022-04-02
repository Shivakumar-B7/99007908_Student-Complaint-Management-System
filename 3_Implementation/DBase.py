import sqlite3

class DBaseConnect:
	def __init__(self):
		self._DBase = sqlite3.connect('information.db')
		self._DBase.row_factory = sqlite3.Row
		self._DBase.execute('create table if not exists Comp(ID integer primary key autoincrement, Name varchar(255), Gender varchar(255), Comment text)')
		self._DBase.commit()
	def Add(self, name, gender, comment):
		self._DBase.execute('insert into Comp (Name, Gender, comment) values (?,?,?)',(name,gender,comment))
		self._DBase.commit()
		return 'Your complaint has been submitted.'
	def ListRequest(self):
		cursor = self._DBase.execute('select * from Comp')
		return cursor
