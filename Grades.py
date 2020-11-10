#function for viewing grades
def viewGrade():
    print("What is the educational level of the student?\n1.Elementary\n2.Highschool\n3.College")
    studentLevel=input()
    print("What is the name of the student?:")
    studentName=input()

    # if studentLevel==1:
    #     with open('Elementary.txt') as readFile:
    #         search = readFile.readlines()
    #         for i, line in enumerate(search):
    #             if studentName in line:
    #                 for l in search[i:i+2]: print
    #             print
    # with open("file.txt", "r") as f:
    #     searchlines = f.readlines()
    # for i, line in enumerate(searchlines):
    #     if "searchphrase" in line:
    #         for l in searchlines[i:i + 3]:
    #             print(l,)

