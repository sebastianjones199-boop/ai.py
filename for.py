import sqlite3
import os 


DB_file="example_2.db"
if os.path.exists(DB_file):
    os.remove(DB_file)
    print(f"remove old database file {DB_file}")


try:
    conn=sqlite3.connect(DB_file)
    print(f"successfully craeted a database ")

except sqlite3.Error as e:
    print(f"theres is an error please check: {e}")
    exit()


try:
    cursor = conn.cursor()
    form = """CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL,
    state TEXT NOT NULL UNIQUE)"""
    cursor.execute(form)
    print("table user created successfully:(if didn't exist).")


except sqlite3.Error as e:
    print(f"connecting error please check: {e}")




try:
    cursor.execute("INSERT INTO users (name,state) VALUES (?,?)",("chidubem","anambara"))
    print("insert one row for chidubem")



    user_to_insert=[ ("chief","lagos"), ("malik","oyo")
    ]
    cursor.executemany("INSERT INTO users (name,state) VALUES (?,?)",user_to_insert)
    print("Insert multiple for chief and malik.")
    conn.commit()
except sqlite3.Error as e:
    print(f"Eroor inserting data: {e}")






# try:
#     cursor.execute("INSERT INTO users (name,state) VALUES (?,?)",("Chidubem","lagos"))
#     print("done inserting the items you wanted")


#     fox = [ ("michel","anambara state"), ("bobby","lagos")
#     ]
#     cursor.executemany("INSERT INTO users (name,state) VALUES (?,?)", fox)
#     print("successfully adding to tabel thankyou")
#     conn.commit()
# except sqlite3.Error as e:
#     print(f"error please check your code: {e}")
# exit()





