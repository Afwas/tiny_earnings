import sqlite3

if __name__ == "__main__":
    db = "earnings.sqlite"
    print("Creating the SQLite database")
    sql = """
    CREATE TABLE IF NOT EXISTS earnings (
        id INTEGER PRIMARY KEY, 
        today DATE DEFAULT CURRENT_DATE,
        revenue INTEGER,
        advertising INTEGER,
        UNIQUE(today))
    """
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
