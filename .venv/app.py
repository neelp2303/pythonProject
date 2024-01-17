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

#/---- lambda function
def add(fx,a):
    return 5+fx(a)
cube = lambda a:a*a*a
print(add(cube,5))