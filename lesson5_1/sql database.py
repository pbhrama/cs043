import sqlite3

connection = sqlite3.connect('business.db')
connection.execute('CREATE TABLE products (prodname, price, weight)')

connection.execute('CREATE TABLE users (name, password, email)')


connection.execute('INSERT INTO products VALUES (?, ?, ?)', ['book', 7.99, 0.5])
connection.execute('INSERT INTO products VALUES (?, ?, ?)', ['drink', 2.00, 0.4])
connection.execute('INSERT INTO products VALUES (?, ?, ?)', ['car', 70000, 1875])

connection.commit()

cursor = connection.cursor()

product_cursor = cursor.execute('SELECT prodname, weight FROM products')
product_list = product_cursor.fetchall()

for pname, weight in product_list:
    print('Product: {}\tWeight: {} kg'.format(pname, weight))