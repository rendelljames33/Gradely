import Student
import Grades
import Misc
menu = 0
while True:
    print("Welcome to Gradely: A Grade Encoding and Storage System")
    print("1.Encode grade\n2.View grades\n3.Exit")
    mainMenu=int(input())
    if mainMenu==1:
        print("\nEncode grade\n")
        Student.encodeGrade()
    elif mainMenu==2:
        print("\nView grades\n")
        Grades.viewGrade()
    elif mainMenu==3:
        print("\nThank You for using Gradely!")
        break
    else:
        Misc.error()