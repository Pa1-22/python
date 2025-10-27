from collections import namedtuple

Student=namedtuple('Student',["id","name","score"])

choice=0

students=[]

while choice != -1:
    id=int(input("Enter the student id:"))
    name=input("Enter the student name: ")
    score=int(input("Enter the marks: "))
    choice=int(input("enter the number 0 or -1:"))
    students.append(Student(id,"name",score))
    top=max(students,key=lambda x: x.score)
print(top)









