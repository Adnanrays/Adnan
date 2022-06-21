# i=0
# while i<=5:
#     print("hello",i)
#     i+=1
# for i in range(2,5):
#     print('hello',i)
#     print("---")
# for c in "hello rays":
#     print(c)
#     print("---")
# str="python"
# for i in str:
#     if i=="o":
#         break
#     print(i)

# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)
# import datetime
# x=datetime.datetime.now()
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.hour)
# functions:
# def sum(a,b):
#     "it sums two number"
#     c=a+b
#     return c
# print(sum(5,10))
# print(sum(10,20))
# d=sum(b=7,a=8)
# print(d)

# def sum(a,b):
#     c=a+b
#     return c
# print(sum(5,10))
# print(sum(10,20))
# list=[1,2,3,4,5]
# def changelist(list):
#      list.append(6)
#      return list
# print(changelist(list))
def sumnum(a,*varg):
    t=a
    for n in varg:
        t=t+n
    return t
total=sumnum(1,2,3,4,5)
print("total",total)





