import pyodbc as odbcconn

conn= odbcconn.connect("Driver={SQL Server};"
                      "Server=BUSHRA\MSSQLS;"
                      "Database=PythonConnection;" 
                      "Trusted_Connection=yes;")

conn.autocommit=True

cursor= conn.cursor()

cursor.execute("CREATE DATABASE PythonConnection")
cursor.close()
conn.close()


cursor.execute('CREATE TABLE products (product_id int primary key,product_name nvarchar(50),price int)')
conn.commit()

cursor.execute('''INSERT INTO products (product_id, product_name, price)
		VALUES
			(1,'Desktop Computer',800),
			(2,'Laptop',1200),
			(3,'Tablet',200),
			(4,'Monitor',350),
			(5,'Printer',150)''')

conn.commit()

cursor.execute('select * from products')
for row in cursor:
    print('row= %r' %(row,))

cursor.execute("SELECT AVG(price) from products")
avg = cursor.fetchone() # or fetchall()
print("The average price is",avg)

cursor.execute("SELECT STDEV(price) from products")
std = cursor.fetchone() # or fetchall()
print("The standard deviation is",std) 
