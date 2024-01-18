print("hello world")
# patient="Neel"
# type="new"
# print(patient,type)
# age=input("Enter your birth year :" )
# print(2024-int(age))

#/----  Code for calculator program
# num1=int(input("Enter a num : "))
# num2=int(input("Enter a num : "))
# option = int(input("Enter option 1-add \n2-sub \n3-mul \n4-div "))
# if option==1:
#     print(num2+num1)
# elif option==2:
#     print(num2-num1)
# elif option==3:
#     print(num2*num1)
# elif option==4:
#     print(num2/num1)
# else:print("Enter valid number")

#/---- for loop,while loop,lists
# num=[1,2,3]
# num.reverse()
# print(num)
# # for item in range(10):
# #     print(item * "*")
# i=0
# while i<len(num):
#     print(num[i])
#     i +=1

#/---- FStrings
# st="Hello {}"
# name =input("Enter name")
# print(f"Hello {name}")

#/---- Functions and recursion
# def factorial(a):
#     if (a==0 or a==1):
#         return (a)
#     else:
#         return (a * factorial(a-1))
#
# fact=factorial(5)
# print(fact)

#/---- Sets
# s1={1,2,3,4}
# s2={4,5,6}
# print(s1.intersection(s2))
# print(s1.symmetric_difference(s2))
# print(s1.union(s2))
# s1.update(s2)
# print(s1)

#/---- Dictionary
# dictio={1:"Neel",2:"Apar",3:"Nishil"}
# print(dictio.keys())
# for key in dictio.keys():
#     print(dictio[key])
# print(dictio.items())

# #/---- lambda function
# def add(fx,a):
#     return 5+fx(a)
# cube = lambda a:a*a*a
# print(add(cube,5))

#/---- map,filter,reduce
# from functools import reduce
# l1=[1,2,3,4,5,6,7,8,9,10]
# li=list(map(lambda a:a*a,l1))
# print(li)
#
# def filterfunc(a):
#     return a>3
#
# newl=list(filter(filterfunc,l1))
# print(newl)
#
# reduceout=reduce(lambda a,b:a+b,l1)
# print(reduceout)

#/---- Exception handling
# a=int(input("Enter a num"))
# try:
#     div=(15/a)
#     print(div)
# except ZeroDivisionError:
#     print("Divided by zero")
#
# finally:
#     print("Code executed")

#/---- OOPS
#/-- class constructor
# class person:
#     name=""
#     age=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f"Name is {self.name} and age is {self.age}")
#
# a=person("Neel",21)
# b=person("Apar",21)
# a.info()
# b.info()

#/---- Decorators
# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("Hello")
#         fx(*args,**kwargs)
#         print(("thank you"))
#     return mfx
# @greet
# def add(a,b):
#     print(a+b)
# add(5,2)

#/---- Threading
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def fun(sec):
    print(f"this is {sec} ")
    time.sleep(sec)
# time1=time.perf_counter()
# t1=threading.Thread(target=fun,args=[4])
# t2=threading.Thread(target=fun,args=[2])
# t3=threading.Thread(target=fun,args=[5])
#
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()
# time2=time.perf_counter()
# time3=time2-time1
# print("\n"+str(time3))

def pooling():
    with ThreadPoolExecutor() as exe:
        # exe1=exe.submit(fun,4)
        # exe2=exe.submit(fun,2)
        # exe3=exe.submit(fun,1)
        li=[1,2,3,4,5]
        exe4=exe.map(fun,li)
pooling()