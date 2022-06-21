n=int(input("please enter a no"))
for i in range(2,n):
    if n%i==0 :
        print("its  not prime no")
        break

else:
    print("its a prime no")