import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    user='flaskuser',          # Replace with your MySQL username
    password='password123',    # Replace with your MySQL password
    host='127.0.0.1',          # or 'localhost'
    database='login_app'       # Replace with your MySQL DB name
)

cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
)
''')
conn.commit()

# Functions
def add_user(name, email, password):
    try:
        query = 'INSERT INTO users (name, email, password) VALUES (%s, %s, %s);'
        cursor.execute(query, (name, email, password))
        conn.commit()
    except mysql.connector.IntegrityError as e:
        print(f"Error: {e}")  # e.g., email already exists

def find_user(email, password=None):
    if password:
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
    else:
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
    
    return cursor.fetchall() 
