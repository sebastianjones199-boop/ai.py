# empty_dict = {}
# print(f"empty dictionary: {empty_dict}")


user_profile = {
    "username": "jdoe",
    "email": "jdoe@example.com",
    "is_acctive": True,
    "roles": ["admin", "editor"]
}
'''print(f"user profile: {user_profile}")'''


# another_dict = dict(name="Alice", age=30)
# print(f"another dictionary: {another_dict}")

# print(f"roles: {user_profile['roles']}")




import sqlite3
import os
fun_file="sun.db"
if os.path.exists(fun_file):
    os.remove(fun_file)

print("removed database successfully {fun_file}")
try:
    conn=sqlite3.connect(fun_file)
    print("successfully connected to database{fun_file}")

except sqlite3.Error as e:
    print("error pleease check your code {e}")


# please check your code ok 

try:
    fun = conn.cursor()
    peep = """CREATE TABLE IF NOT EXISTS USERS(id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL,
    class TEXT NOT NULL UNIQUE);"""
    fun.execute(peep)

    print("successfully craeted a tabel in your database:(if didn't exist).")

except sqlite3.Error as e:
    print("please check your code ok ")

try:
    fun.execute("INSERT INTO users (name, class) VALUES (?,?)", ("chidinma", "ss1"))
    print("done with the first code")
    
    abi=[("chidubem","ss3" ),("joy","ss3")]
    
    fun.executemany("INSERT INTO users (name, class) VALUES (?,?)", abi)
    print("success with the inserting")

    conn.commit()
except sqlite3.Error as e:
     print("please chack for commers and indemtation")