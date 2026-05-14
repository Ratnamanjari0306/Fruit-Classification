import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

print("Database connected")