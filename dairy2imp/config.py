# config.py - MySQL connection helper

import os
import mysql.connector
from mysql.connector import Error

# -----------------------------
# Database connection settings
# -----------------------------
DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PORT = int(os.environ.get('DB_PORT', 3306))
DB_USER = os.environ.get('DB_USER', 'gowri')        # MySQL username
DB_PASS = os.environ.get('DB_PASS', 'gowri123')     # MySQL password
DB_NAME = os.environ.get('DB_NAME', 'gowri')        # MySQL database name

# -----------------------------
# Function to get a new MySQL connection
# -----------------------------
def get_db():
    """
    Returns a new MySQL connection.
    If connection fails, prints the error and raises exception.
    """
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            autocommit=False
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"❌ Error connecting to MySQL: {e}")
        raise

# -----------------------------
# Optional: Simple test connection
# -----------------------------
if __name__ == "__main__":
    try:
        db = get_db()
        print("✅ MySQL connection successful.")
        db.close()
    except Exception as err:
        print("❌ Failed to connect:", err)
