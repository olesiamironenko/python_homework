import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect("../db/lesson.db",isolation_level='IMMEDIATE')
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

# Task 2: A Line Plot with Pandas
# 2.1: Create a DataFrame with the order_id and the total_price for each order
sql_order_total = """SELECT o.order_id AS order_id, SUM(l.quantity * p.price) AS total_price
    FROM orders o
    JOIN line_items l
    ON o.order_id == l.order_id
    JOIN products p
    ON l.product_id == p.product_id
    GROUP BY l.order_id
    ORDER BY o.order_id;"""
order_total = pd.read_sql_query(sql_order_total, conn)
#print(order_total)

# 2.2: Add a "cumulative" column to the DataFrame using cumsum()
order_total['cumulative'] = order_total['total_price'].cumsum()
#print(order_total.head(5))

# 2.3: Create a line plot of cumulative revenue vs. order_id.
order_total.plot(x="order_id", y=["cumulative"], kind="line")
plt.title("Cumulative Totals", fontsize=14, fontweight='bold')
plt.xlabel("Order ID", fontsize=12)
plt.ylabel("Cumulative ($)", fontsize=12)
plt.tight_layout()

# 2.4: Show the Plot
plt.show()