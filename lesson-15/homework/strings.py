import sqlite3

conn = sqlite3.connect("my_database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

conn.commit()
conn.close()

print("Database and table created successfully!")



import sqlite3


conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")


characters = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]


cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", characters)


conn.commit()

cursor.execute("SELECT * FROM Roster")
for row in cursor.fetchall():
    print(row)

conn.close()



import sqlite3


conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()


cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")


conn.commit()


cursor.execute("SELECT * FROM Roster")
for row in cursor.fetchall():
    print(row)


conn.close()





import sqlite3


conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()


cursor.execute("""
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
""")


for row in cursor.fetchall():
    print(row)


conn.close()
