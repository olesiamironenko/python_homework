import sqlite3
import pandas as pd

with sqlite3.connect("../db/lesson.db") as conn:
    # 6.2: Read data into a DataFrame, as described in the lesson.
    sql_query = """
        SELECT line_items.line_item_id, line_items.quantity, products.product_id, products.product_name, products.price
        FROM line_items 
        JOIN products
        ON line_items.product_id = products.product_id
    """
    df = pd.read_sql_query(sql_query, conn)

    # 6.3: Print the first 5 lines of the resulting DataFrame
    print(df.head(5))

    # 6.4: Add a column to the DataFrame called "total"
    df['total'] = df['quantity'] * df['price']
    print(df.head(5))

    # 6.5: group by the product_id
    per_product_sales = df.groupby('product_id').agg({'line_item_id':'count', 'total':'sum', 'product_name':'first'})
    print(per_product_sales.head(5))

    # 6.6: Sort the DataFrame by the product_name column
    per_product_sales.sort_values(by = 'product_name', inplace=True)
    print(per_product_sales.head(5))

    # 6.7: write this DataFrame to a file order_summary.csv, which should be written in the assignment7 directory
    per_product_sales.to_csv('./order_summary.csv', sep=',', index=True, header=True, encoding=None)