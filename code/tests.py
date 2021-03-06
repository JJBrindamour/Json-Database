from database import Database

def test1():
	db = Database('data.json')
	names = db.table('Names', 'Primary Key', 'fname', 'lname', primaryKey=(True, False, False))
	names.commit()
	work = db.table('Work', 'Primary Key', 'Person ID', 'Occupation', 'Salary', primaryKey=(True, False, False, False), foreignKey=(None, ["Names", "Primary Key"], None, None))
	names.addRow('JJ', 'Brindamour')
	work.addRow(0, 'Fisherman', 35000)
	names.commit()
	work.commit()
	print(names.find('fname', 'JJ'))
	db.commit()

def test2():
	db = Database('data.json')
	names = db.table('Names')
	work = db.table('Work')
	names.addRow('Tim', 'Smith')
	names.commit()
	work.addRow(1, 'Software Engineer', 100000)
	work.commit()
	db.commit()
	print(work.find('Person ID', 1))

def test3():
	db = Database('data.json')
	names = db.table('Names')
	work = db.table('Work')
	names.addRow('Jake', 'Ceaser')
	work.addRow(2, 'Musician', 56000)
	names.commit()
	work.commit()
	work.removeRow(2)
	work.commit()
	db.commit()

def test4():
	db = Database('data.json')
	db.delTable('Names')
	db.commit()

def test5():
	db = Database('data.json')
	table = db.table("Table", "Primary Key", "Unique", primaryKey=(True, False), unique=(True, True))
	table.addRow("data")
	table.addRow("data2")
	table.commit()
	db.commit()

def test6():
	db = Database('data.json')
	table = db.table('Table', 'primaryKey', 'fname', 'lname', primaryKey=(True, False, False), notNull=(False, True, False))
	table.addRow('JJ', 'Brindamour')
	table.addRow('MyName', 'MyLastName')
	table.commit()
	db.commit()

def test7():
	db = Database('data.json')
	table = db.table('Table', 'Primary Key', 'SomeData', primaryKey=(True, False), default=(None, "This is Data"))
	table.addRow()
	table.commit()
	db.commit()

#test1()
#test2()
#test3()
#test4()
#test5()
#test6()
#test7()