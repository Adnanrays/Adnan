file=open("hello.txt")
text=file.read()
print(text)
print("file name:",file.name)
print("mode of opening : ",file.mode)
print("is closed:",file.closed)
file.close()

