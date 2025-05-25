import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Task 1: Plotting with Pandas
# 1.2: Load a DataFrame called employee_results using SQL

conn = sqlite3.connect("../db/lesson.db",isolation_level='IMMEDIATE')
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

sql_employee_revenue = """SELECT last_name AS last_name, SUM(price * quantity) as revenue 
    FROM employees e
    JOIN orders o
    ON e.employee_id == o.employee_id
    JOIN line_items l
    ON o.order_id == l.order_id
    JOIN products p
    ON l.product_id == p.product_id
    GROUP BY e.employee_id;"""

employee_results = pd.read_sql_query(sql_employee_revenue, conn)
print(employee_results)
