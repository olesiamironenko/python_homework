import sqlite3
import pandas as pd

conn = sqlite3.connect("../db/lesson.db",isolation_level='IMMEDIATE')
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

# Task 1: Complex JOINs with Aggregation
# Find the total price of each of the first 5 orders
sql_order_total = """SELECT orders.order_id AS order_id, SUM(line_items.quantity * products.price) AS order_total
    FROM orders
    JOIN line_items
    ON orders.order_id == line_items.order_id
    JOIN products
    ON line_items.product_id == products.product_id
    GROUP BY line_items.order_id
    ORDER BY orders.order_id
    LIMIT 5;"""
df_order_total = pd.read_sql_query(sql_order_total, conn)
print(df_order_total)

# Task 2: Understanding Subqueries
# For each customer, find the average price of their orders.
sql_customer_avg = """SELECT customers.customer_name AS customer_name, AVG(orders_total.order_total) AS order_average 
    FROM customers
    JOIN (
        SELECT orders.customer_id AS customer_id, orders.order_id AS order_id, SUM(line_items.quantity * products.price) AS order_total
            FROM orders
            JOIN line_items
            ON orders.order_id == line_items.order_id
            JOIN products
            ON line_items.product_id == products.product_id
            GROUP BY line_items.order_id
            ORDER BY orders.order_id
    ) AS orders_total
    ON customers.customer_id == orders_total.customer_id
    GROUP BY customers.customer_id
    ORDER BY customers.customer_name
    LIMIT 5;"""
df_customer_avg = pd.read_sql_query(sql_customer_avg, conn)
print(df_customer_avg)

# Task 3: An Insert Transaction Based on Data
# - Create a new order for the customer named Perez and Sons.  
# - The employee creating the order is Miranda Harris. 
# - The customer wants 10 of each of the 5 least expensive products
conn.execute("BEGIN")
try:
# 3.1. Do a SELECT statement to retrieve the customer_id
    cursor.execute("""SELECT customer_id FROM customers WHERE customer_name = ?;""", ('Perez and Sons',))
    customer_id = cursor.fetchone()[0]

# 3.2. Do a SELECT statement to retrieve the employee_id
    cursor.execute("""SELECT employee_id 
        FROM employees 
        WHERE first_name = ? AND last_name = ?;""", 
        ('Miranda', 'Harris'))
    employee_id = cursor.fetchone()[0]

# 3.3. Do a SELECT statement to retrieve the product_ids of the 5 least expensive products
    cursor.execute("""SELECT products.product_id 
        FROM products
        ORDER BY products.price ASC
        LIMIT 5;""")
    product_ids = [row[0] for row in cursor.fetchall()]

# 3.4. Create the order record and the 5 line_item records comprising the order
    # Create an order
    cursor.execute(
        """INSERT INTO orders (customer_id, employee_id, date) 
        VALUES (?, ?, DATE('now'));""",
        (customer_id, employee_id)
    )
    # retrieve the order id
    last_order_row_id = cursor.lastrowid
    print(last_order_row_id)

    # add products to the order
    for product_id in product_ids:
        cursor.execute(
            """INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?);""",
            (last_order_row_id, product_id, 10)
        )
    conn.commit()  # Commit transaction

except Exception as e:
    conn.rollback()  # Rollback transaction if there's an error
    print("Error:", e)

sql_last_order = """SELECT customers.customer_name, orders.order_id, products.product_name, line_items.quantity
    FROM customers
    JOIN orders
    ON customers.customer_id = orders.customer_id
    JOIN line_items
    ON orders.order_id = line_items.order_id
    JOIN products 
    ON line_items.product_id = products.product_id
    WHERE customers.customer_name == 'Perez and Sons' 
        AND orders.order_id == (
            SELECT orders.order_id 
            FROM orders
            ORDER BY order_id DESC
            LIMIT 1);"""
df_last_order = pd.read_sql_query(sql_last_order, conn)
print(df_last_order)

# Task 4: Aggregation with HAVING
# Find all employees associated with more than 5 orders
sql_order_cout = """SELECT employees.first_name, employees.last_name, COUNT(orders.order_id) AS orders_count
    FROM employees
    JOIN orders
    ON employees.employee_id == orders.employee_id
    GROUP BY employees.employee_ID
    HAVING orders_count > 5 
    ORDER BY employees.first_name, employees.last_name;"""
df_order_cout = pd.read_sql_query(sql_order_cout, conn)
print(df_order_cout)

# Deleting inserted info
cursor.execute("""DELETE FROM line_items WHERE order_id >= 250;""")
cursor.execute("""DELETE FROM orders WHERE order_id >= 250;""")
conn.commit()  # Commit transaction

# Clean up the database connection
conn.close()
