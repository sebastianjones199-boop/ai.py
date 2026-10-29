import sqlite3
import os
DB_file="example.db"

if os.path.exists(DB_file):
    os.remove(DB_file)
    print(f"remove old database file:{DB_file}")

try:
    conn=sqlite3.connect(DB_file)
    print(f"successfully connected to a database: {DB_file}")
except sqlite3.Error as  e:
    print(f"error connecting to database: {e}")       
    exit()



try:
    cursor =conn.cursor()
    form="""CREATE TABLE IF NOT EXISTS USERS( id INTEGER PRIMARY KEY,
                                          name TEXT NOT NULL ,
                                          email TEXT NOT NULL UNIQUE)"""
    cursor.execute(form)
    print("table 'user' created successfully (if it didn't exist).")
except sqlite3.Error as e:
    print(f"error creating table {e}")


# first=12,34,"fun"
# print(first)

# # count=0
# while count<5:
#     print(count)
#     count+=1
try:
    cursor.execute("INSERT INTO users (name,email) VALUES (?,?)",("Alice", "alice@gmail.com"))
    print("Insert one row for Alice. ")

    user_to_insert=[ ("bob","bob@example.com"), ("charlie","charlie@example.ccom")
    ]
    cursor.executemany("INSERT INTO users (name,email) VALUES (?,?)",user_to_insert)
    print("Insert multiple for bob and charlie.")
    conn.commit()
except sqlite3.Error as e:
    print(f"Eroor inserting data: {e}")












# try:
#     cursor.execute("SELECT * FROM users")
#     all_users=cursor.fetchall()
#     print("ALL users in the database:")
#     for users in all_users:
#         print(f"ID: {users[0]}, NAME: {users[1]},Email:{users[2]} ")
#     cursor.execute("SELECT * FROM users WHERE name= ? ", ("bob",))
#     bob=cursor.fetchone()
#     if bob:
#         print(f"Found bob {bob}")
#     else:
#         print("bob not found.")

# except sqlite3.Error as e:
#     print(f"Error querying data: {e} ")






# try:
#     fun = "UPDATE users SET email= ? WHERE name= ? "
#     cursor.execute(fun, (" alice. smith@newdomain.com", "Alice"))
#     conn.commit()

#     print("update Alice's email.")

#     cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
#     updated_alice = cursor.fetchone()
#     print("f Alice's updated info: {updated_alice}")
# except sqlite3.Error as e:
#      print(f"Error updating data {e}")
    
# try:
#     dude = "DELETE FROM users WHERE name = ?"
#     cursor.execute(dude, ("charlie",))
#     conn.commit()
#     print("deleted charlie from the database.")

#     cursor.execute(" SELECT * FROM users")
#     deck = cursor.fetchall()
#     print("remaining users:")
#     for users in deck:
#         print(f"  {users}")

# except sqlite3.Error as e:
#     print(f" Error delicting data {e}")



# finally:
#     if conn:
#         conn.close()
#         print(" database connection closed. ")