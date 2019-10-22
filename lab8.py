import sqlite3
conn=sqlite3.connect("student.db")
cur=conn.cursor()
cur.execute('''CREATE TABLE if not exists Student
(emp_ssn varchar(10) NOT NULL,
emp_name TEXT NOT NULL,
emp_category char(1) NOT NULL,
gross_sal real,
basic_sal real);''')
if cur:
print "Table created successfully";
ssn=''
name=''
cat=''
bsal=0.0
gsal=0.0
td=0.0
netsal=0.0
da=0.0
ch=input("You want enter the details\n")
if ch=='y':
n=int(input("Enter the number of employees\n"))
for i in range(0,n):
print("")
ssn=input("Enter SSN of an Emp\n")
print("")
name=input("Enter name of an Emp\n")
print("")
cat=input("Enter Category of an Emp\n")
print("")
bsal=float(input("Enter Basic Salary of an Emp\n"))
cur.execute("INSERT INTO Employee (emp_ssn,emp_name,emp_category,basic_sal)VALUES (:1,:2,:3,:4)",(ssn,name,cat,bsal ));
else:
cur.execute("SELECT * from Employee")
cursor=cur.fetchall()
for row in cursor:
cat=row[2]
gsal=row[3]

bsal=row[4]
if row[2]=='A':
da=(bsal*0.8)
gsal=bsal+da
td=gsal*0.3
netsal=gsal-td
elif row[2]=='B':
da=(bsal*0.5)
gsal=bsal+da
td=gsal*0.2
netsal=gsal-td
elif row[2]=='C':
da=(bsal*0.3)
gsal=bsal+da
td=gsal*0.1
netsal=gsal-td
print("SSN = ", row[0],)
print( "NAME = ", row[1], )
print( "Category = ", row[2],)
print( "GROSS SALARY = ", row[3],)
print( "Basic Salary = ", row[4],)
print( "Tax = ", td,)
print( "Net Salary = ", netsal)
conn.commit()
conn.close()