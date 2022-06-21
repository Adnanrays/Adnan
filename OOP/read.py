"read file"
'''file=open("io")
for line in file :
    print(line)
  file.close()'''
'''
#"write file"
file =open("io","w")
file.write("hey\n")
file.write("this is an institute")
file.close()

with open ("io","w") as file:
    file.write("hello my name is adnan khan \n")
    file.write("its me")
file=open("io")
str= file.read(2)
position=file.tell()
position = file.seek(0,0)
'''
import os
os.rename("io","io2")









