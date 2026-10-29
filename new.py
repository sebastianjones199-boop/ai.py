import sqlite3
gig=sqlite3.connect('school.db')

f=gig.cursor()

# f.execute("""CREATE TABLE grades(name_of_school TEXT,
#             location TEXT,
#            uniform TEXT)  """)
dubem=[('wes','blake','good'),('fun','food','face')]

f.executemany("INSERT INTO grades VALUES (?,?,?)",dubem)
f.execute("SELECT * FROM grades")
# print(f.fetchall()[3])
items=f.fetchall()

for item in items:
    print(item[0])




gig.commit()
