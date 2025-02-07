import sqlite3

def create_database():
    # Connect to SQLite database (creates new one if not exists)
    conn = sqlite3.connect('financial_data.db')
    cursor = conn.cursor()

    # Read and execute the SQL file
    with open('financial_data.sql', 'r') as sql_file:
        sql_script = sql_file.read()
        cursor.executescript(sql_script)
    
    # Commit the changes
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()