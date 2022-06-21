
'''n=int(input("please enter a number"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("its palindrome")
else:
    print("it's not palindrome")'''
num=input("please enter a no ")
l=list(num)
print(l)
i=0
n=len(num)
if l[i]==l[n-i-1]:
    i=i+1
    print("its pallindrome")
else:
    print("its not a pallindorme")