student_name='adnan'
marks={'adnan':45,'adam':66,'abu':55}
for student in marks:
    if student== student_name:
        print(marks[student])
        break
else:
    print('no entry with that name found')