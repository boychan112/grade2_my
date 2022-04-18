# def add(a,b):
#     return a+b
# def hi():
#     print("hello")

# print(add(1,2))
# hi()

import random as r

def mid():
    list=[]

    for i in range(5):
        list.append(r.randint(0,45))

    list.sort()
    print(list[2])

mid()