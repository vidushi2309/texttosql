import sqlite3

## Connect to sqlite
connection=sqlite3.connect("EMPLOYEE.db")

## Create a cursor object to insert record,create table,retrieve data
cursor=connection.cursor()

## create the table
table_info="""
Create table EMPLOYEE(NAME VARCHAR(25),DESIGNATION VARCHAR(25),RATING INT,SALARY INT);


"""

cursor.execute(table_info)

## Insert some more records

cursor.execute('''Insert Into EMPLOYEE values('Vidushi','Engineer',5,5000)''')
cursor.execute('''Insert Into EMPLOYEE values('Varad','Lawyer',2,2000)''')
cursor.execute('''Insert Into EMPLOYEE values('Alka','Teacher',3,5600)''')
cursor.execute('''Insert Into EMPLOYEE values('Dhirendra','Programmer',5,10000)''')
cursor.execute('''Insert Into EMPLOYEE values('Varija','Engineer',5,3000)''')
cursor.execute('''Insert Into EMPLOYEE values('Rhythm','Accountant',4,2000)''')
cursor.execute('''Insert Into EMPLOYEE values('Swarmay','Engineer',1,1000)''')
cursor.execute('''Insert Into EMPLOYEE values('InduBhushan','PA',5,10000)''')
cursor.execute('''Insert Into EMPLOYEE values('Cherry','Actress',4,100)''')
cursor.execute('''Insert Into EMPLOYEE values('Harry','Engineer',2,10000)''')


## Display all the records
print("THE INSERTED RECORDS ARE")

data=cursor.execute('''Select * from EMPLOYEE''')

for row in data:
    print(row)

## close connection

connection.commit()
connection.close()
