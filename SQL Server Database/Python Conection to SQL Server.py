import pyodbc as odbcconn

#connect Python to SQL Server
conn= odbcconn.connect("Driver={SQL Server};"
                      "Server=BUSHRA\MSSQLS;"
                      "Database=PythonConnection;" 
                      "Trusted_Connection=yes;")
cursor= conn.cursor()

#create database PythonConnection
conn.autocommit=True
cursor.execute("CREATE DATABASE PythonConnection")
cursor.close()
conn.close()

#create the table products
cursor.execute('CREATE TABLE products (product_id int primary key,product_name nvarchar(50),price int)')
conn.commit()

#inserting records to products table
cursor.execute('''INSERT INTO products (product_id, product_name, price)
		VALUES
			(1,'Desktop Computer',800),
			(2,'Laptop',1200),
			(3,'Tablet',200),
			(4,'Monitor',350),
			(5,'Printer',150)''')
conn.commit()

#review the table
cursor.execute('select * from products')
for row in cursor:
    print('row= %r' %(row,))

#calculate the mean
cursor.execute("SELECT AVG(price) from products")
avg = cursor.fetchone() # or fetchall()
print("The average price is",avg)
  
#calculate the standard deviation
cursor.execute("SELECT STDEV(price) from products")
std = cursor.fetchone() # or fetchall()
print("The standard deviation is",std) 
