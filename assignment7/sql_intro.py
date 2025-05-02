import sqlite3
import pandas as pd

#  3.2: Create functions, one for each of the tables, to add entries
def add_publisher(publisher_name, contact, address, phone):
    try:
        cursor.execute("INSERT INTO publishers (publisher_name, contact, address, phone) VALUES (?,?,?,?)", (publisher_name, contact, address, phone))
    except sqlite3.IntegrityError:
        print(f"{publisher_name} is already in the database.")

def add_magazine(magazine_name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (magazine_name, publisher_id) VALUES (?,?)", (magazine_name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{magazine_name} is already in the database.")

def add_subscriber(subscriber_name, address, phone):
    try:
        cursor.execute("INSERT INTO subscribers (subscriber_name, address, phone) VALUES (?,?,?)", (subscriber_name, address, phone))
    except sqlite3.IntegrityError:
        print(f"{subscriber_name} with {address} is already in the database.")

def add_subscription(subscriber_id, magazine_id):
    try:
        cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id) VALUES (?,?)", (subscriber_id, magazine_id))
    except sqlite3.IntegrityError:
        print(f"{subscriber_id} and {magazine_id} combination is already in the database.")

# Connect to a new SQLite database
with  sqlite3.connect("../db/magazines.db") as conn:  
    print("Database created and connected successfully.")
    # 3.1: turn on the foreign key constraint
    conn.execute("PRAGMA foreign_keys = 1") 
    cursor = conn.cursor()

    # 2.2: create tables

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,          
            publisher_name TEXT NOT NULL UNIQUE,
            contact TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL
        )
        """)
        print("Table publishars created successfully.")
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,          
            magazine_name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER,
            FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id)
        )
        """)
        print("Tables magazines created successfully.")
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,          
            subscriber_name TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL,
            UNIQUE (subscriber_name, address)
        )
        """)
        print("Tables subscribers created successfully.")
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,          
            subscriber_id INTEGER,
            magazine_id INTEGER,
            UNIQUE (subscriber_id, magazine_id),
            FOREIGN KEY(subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY(magazine_id) REFERENCES magazines(magazine_id)
        )
        """)
        print("Tables subscriptions created successfully.")
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

    conn.commit() 

    # 3.3: populate each of the 4 tables with at least 3 entries

    add_publisher('Hillman Periodicals', 'Alex L. Hillman', '535 Fifth Avenue, New York City, NY', '+12129724865')
    add_publisher('Blood-Horse Publications', 'Marla Bickel', '821 Corporate Dr, Lexington, KY', '+18005825604')
    add_publisher('National Geographic Society', 'Jean M. Case', '1145 17th St NW, Washington, DC', '+18006475463')

    conn.commit()
    print("Sample data for publishers table inserted successfully.")

    add_magazine('Pageant', 1)
    add_magazine('The Freeman', 1)
    add_magazine('People Today', 1)
    add_magazine('The Blood-Horse', 2)
    add_magazine('TBH Auction Edge', 2)
    add_magazine('Keeneland Magazine', 2)
    add_magazine('National Geographic Explorer', 3)
    add_magazine('National Geographic History', 3)
    add_magazine('National Geographic Traveler', 3)

    conn.commit()
    print("Sample data for magazines table inserted successfully.")

    add_subscriber('Simon Villareal', '105 Hudson Ave, Totowa, NJ', '+19347264488')
    add_subscriber('Carter Matthews', '1633 Pulaski Ave, Coal Township, PA', '+17364560033')
    add_subscriber('Lance Pagan', '214 Broadway Ave, Defiance, OH', '+17362541342')
    add_subscriber('Ray Moyer', '204 Monroe St NE, Albuquerque, NM', '+18462514352')
    add_subscriber('Lilianna Davila', '1921 SE 7th Ave, Portland, OR', '+17354627483')
    add_subscriber('Lilianna Davila', '1921 SE 7th Ave, Portland, OR', '+17354627483')
    add_subscriber('Lilianna Davila', '204 Monroe St NE, Albuquerque, NM, OR', '+17354627483')

    conn.commit()
    print("Sample data for subscribers table inserted successfully.")

    add_subscription(1, 1)
    add_subscription(1, 5)
    add_subscription(2, 9)
    add_subscription(2, 4)
    add_subscription(3, 8)
    add_subscription(3, 3)
    add_subscription(4, 6)
    add_subscription(5, 7)

    conn.commit()
    print("Sample data for subscriptions table inserted successfully.")

    # Task 4: Write SQL Queries
        # 4.1: Write a query to retrieve all information from the subscribers table.
    sql_subscribers_all = """SELECT * FROM subscribers;"""
    df_subscribers_all = pd.read_sql_query(sql_subscribers_all, conn)

        # 4.2: Write a query to retrieve all magazines sorted by name.
    sql_magazines_all = """SELECT * FROM magazines ORDER BY magazine_name;"""
    df_magazines_all = pd.read_sql_query(sql_magazines_all, conn)

        # 4.3: Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
    sql_magazines_for_publisher1 = """
        SELECT p.publisher_name, m.magazine_name 
        FROM publishers AS p
        JOIN magazines AS m
        ON p.publisher_id == m.publisher_id
        WHERE p.publisher_id == 1;
    """
    df_magazines_for_publisher1 = pd.read_sql_query(sql_magazines_for_publisher1, conn)
    
        # 4.4: Add these queries to your script. For each, print out all the rows returned by the query.
    print(df_subscribers_all)
    print(df_magazines_all)
    print(df_magazines_for_publisher1)