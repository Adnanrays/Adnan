n=int(input("please enter a no for factorial"))
factorial=1
for i in range(1,n+1,1):
        factorial=factorial*i
print(n,"!=",factorial)