# import sqlite3
# gig=sqlite3.connect("student.db")

# f=gig.cursor()
# # f.execute (""" CREATE TABLE student(subject TEXT,
# #             score TEXT)""")

# jes=[("chem","59"),("maht","34")]
# f.executemany("INSERT INTO student VALUES (?,?)",jes)
# gig.commit()
# def fun (a,b):
#     return a*b
# num={fun(23,45)}
# print(num)
# fish=lambda a,d: a*d
# print({fish(34,45)})
# print()
# irs=lambda x: x % 2 == 0
# print(f"is 10 even? {irs(10)}")
# print(f"is 7 even {irs(7)}")
# student=[("alice",92),("bob",85),("charlie",95)]
# grade=sorted(student,key=lambda student: student[0])
# print(grade)
# emp=[{'name':'john','age':35},
#      {'name':'liv','age':20},
#      {'name':'jef','age':29}
# ]

# sit=sorted(emp, key=lambda emp: emp['name'])
# print(sit)
# nmb = [1, 2, 3, 4, 5, 6, 7, 8]
# s_numb = map(lambda x: x ** 2, nmb)
# print(f"msthew: {s_numb}")
# print(f"mark: {list(s_numb)}")
# print()

# numbers=[1,2,3,4,5,6,7,8,9,10]

# even_numbers = filter(lambda x:x % 2 == 0,numbers)
# print(f"the numbers are: { list(even_numbers)}")
# cas=lambda age:"adult" if age>=18  else"minor"
# print(f"the age is: 


# dff = -1
# while dff <= 0:
#     print(dff)
#     dff -= 1


# def dubem (a,b):
#     return a // b



# just=int(input("enter your number plesase: "))
# just_2=int(input("enter your second number: "))

# sum=dubem(just,just_2)
# print(sum)
# school=int(input("enter your school state: "))
# if school<10:
#     print("your are ready for school: ")

# elif school==18:
#     print("your class is on wednesday and fridey: ")

# elif school==34:
#     print("you are too old for school: ")


# elif school>34:
#     print("you are very old")


# else:
#     print("get the fuck out of my school")


# get=["ded","fin","chess","check","film"]
# print(get[0])

# dic={"name":"chess","add":"onitcha","school":"phill foden","tep":["sef","jef","def",("jed","jack","chief")]}
# print(dic)