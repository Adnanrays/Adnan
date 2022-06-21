

#file=open("io2")
#for line in file:
 #   print(line)
#file.close()


"searching words in line "
import re
def readline():
    file=open("io2")
    for line in file:
        if(re.search("adnan",line)):
            print(line,end='')
    file.close()
readline()

# "reading file by numbers"
# file=open("io")
# text=file.read(9)
# print(text)
# file.close()

