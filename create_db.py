import pandas as pd
import sqlite3

def init_db(db_name="user_info.db"):
    create_db = """
    CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP)
    """
    try:
        with sqlite3.connect(db_name) as conn:
            c = conn.cursor()
            c.execute(create_db)
            conn.commit()
    except sqlite3.DatabaseError as e:
        print("Error creating database: %s", e)

def insert_db(db_name="user_info.db"):
    clients_data = [
        ("Bill Gates", "bill.gates@microsoft.com", "+123456789", "New York, USA"),
        ("Elon Musk", "elon.musk@spacex.com", "+111222333", "Florida, USA"),
        ("Will Smith", "will.smith@gmail.com", "+111133555", "California, USA"),
        ("Bob Marley", "bob@gmail.com", "+111555999", "Texas, USA"),
        ("Cristiano Ronaldo", "cristiano.ronaldo@gmail.com", "+32447788993", "Manchester, England"),
        ("Boris Johnson", "boris.johnson@gmail.com", "+4499778855", "London, England")
    ]

    try:
        with sqlite3.connect(db_name) as conn:
            c = conn.cursor()
            c.executemany("""INSERT INTO clients (name, email, phone, address) VALUES (?, ?, ?, ?)""",
                          clients_data)
            conn.commit()
    except sqlite3.DatabaseError as e:
        print("Error inserting user info into database: %s", e)

def fetch_user_info(db_name="user_info.db"):
    query = """SELECT * FROM clients;"""
    
    try:
        with sqlite3.connect(db_name) as conn:
            user_info = pd.read_sql(query, conn)
            return user_info
    except sqlite3.DatabaseError as e:
        print("Error fetching user info from database %s", e)

if __name__ == '__main__':
    data = fetch_user_info()
    print(data)