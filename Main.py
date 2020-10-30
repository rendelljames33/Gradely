import Student
menu = ""
while menu!="3":
    print("Welcome to Gradely: A Grade Encoding and Storage System")
    print("1.Encode grade\n2.View grades\n3.Exit")
    menu=input()
    if menu=="0" or menu>"3":
        print("Input error\n")
    if menu=="1":
        print("\nEncode grade\n")
    studentLevel = int(input("Enter educational level (1=elementary,2=highschool,3=college): "))
    if studentLevel==1:
        Student.student()
    elif studentLevel==2:
        Student.student()