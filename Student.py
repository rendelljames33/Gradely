#Functions for encoding grade
import Misc

#function for remarks
def determine_grade(genAve):
    if genAve >= 90.00 and genAve <= 100.00:
        return 'Outstanding'
    elif genAve >= 85.00 and genAve <= 89.00:
        return 'Very Satisfactory'
    elif genAve >= 80.00 and genAve <= 84.00:
        return 'Satisfactory'
    elif genAve >= 75.00 and genAve <= 79.00:
        return 'Fairly Satisfactory'
    elif genAve < 75.00:
        return 'Failed'

#function for rating(college)
def determine_rate(genAve):
    if genAve >= 94.8 and genAve <= 100:
        return '1.00'
    elif genAve >= 89.2 and genAve <= 94.7:
        return '1.25'
    elif genAve >= 83.6 and genAve <= 89.1:
        return '1.50'
    elif genAve >= 78.0 and genAve <= 83.5:
        return '1.75'
    elif genAve >= 72.4 and genAve <= 77.9:
        return '2.00'
    elif genAve >= 66.8 and genAve <= 72.3:
        return '2.25'
    elif genAve >= 61.2 and genAve <= 66.7:
        return '2.50'
    elif genAve >= 55.6 and genAve <= 61.1:
        return '2.75'
    elif genAve >= 50.0 and genAve <= 55.5:
        return '3.00'
    elif genAve >= 0.0 and genAve <= 49.9:
        return '5.00'

#function for encoding grade(elem and hs)
def encodeQuartergrades():
    while True:
        quarterGrades=[]
        i=0
        while i!=4:
            grade=input()
            if grade.isdigit():
                quarterGrades.append(int(grade))
                i+=1
            else:
                Misc.error()
        return quarterGrades

#function for encoding grade(college)
def encodegradecollege():
    while True:
        quarterGrades=[]
        i=0
        while i!=2:
            grade=input()
            if grade.isdigit():
                quarterGrades.append(int(grade))
                i+=1
            else:
                Misc.error()
        return quarterGrades

#function for encoding subjects
def encodesubject():
    while True:
        listsubject = []
        subjCount =input("Enter the total number of subjects: ").strip()
        if subjCount in '1234567890':
            subjCount=int(subjCount)
            for i in range(int(subjCount)):
                listsubject.append(input("Enter subject {}: ".format(i + 1)))
            break
        else:
            Misc.error()

def reportCard(studName,studLevel,subjgrades,subjectslist,quarterAverage,generalAverage):
    print()
    print("Name: "+studName)
    print("Educational Level: "+studLevel)
    print(f"{'Subjects':<21}{'1st':<7}{'2nd':<7}{'3rd':<7}{'4th':<7}{'Final'}")
    for sub,grad,ave in zip(subjgrades,subjectslist,quarterAverage):
        print(f"{grad:<20}",end=" ")
        print(*sub,sep="     ",end="      ")
        print(ave)
    print(f"{' ':<33}{'General Average: '}"+"%.2f" % generalAverage)
    print(f"{' ':<41}{'Remarks: '}" +str(determine_grade(generalAverage)))

def reportCardcollege(studName,studLevel,subjgrades,subjectslist,quarterAverage,generalAverage):
    print()
    print("Name: "+studName)
    print("Educational Level: "+studLevel)
    print(f"{'Subjects':<21}{'1st':<7}{'2nd':<7}{'Final'}")
    for sub,grad,ave in zip(subjgrades,subjectslist,quarterAverage):
        print(f"{grad:<20}",end=" ")
        print(*sub,sep="     ",end="      ")
        print(ave)
    print(f"{' ':<19}{'General Average: '}"+"%.2f" % generalAverage)
    print(f"{' ':<30}{'Rate: '}" +str(determine_rate(generalAverage)))

def encodeGrade():
    while True:
        studentLevel = input("Enter educational level\n1.Elementary\n2.Highschool\n3.College\n4.Back\n")
        if studentLevel in '1234':
            studentLevel=int(studentLevel)
            if studentLevel == 1:
                elementary()
                break
            elif studentLevel == 2:
                highschool()
                break
            elif studentLevel == 3:
                college()
                break
            elif studentLevel == 4:
                return False
        else:
            Misc.error()

#student for elementary
def elementary():
    studentName=str(input("Enter student name: "))
    studentLevel="Elementary"
    while True:
        subjectslist = []
        subjCount =input("Enter the total number of subjects: ").strip()
        if subjCount in '1234567890':
            subjCount=int(subjCount)
            for i in range(int(subjCount)):
                subjectslist.append(input("Enter subject {}: ".format(i + 1)))
            break
        else:
            Misc.error()
    subjCount = len(subjectslist)
    subjgrades=[]
    quarterTotal=[]
    quarterAverage=[]

    for subjects in subjectslist:
        print("Enter "+subjects+" grades per quarter")
        subjgrades.append(encodeQuartergrades())

    for grades in subjgrades:
        quarterTotal.append(sum(grades))

    for total in quarterTotal:
        average= total/4
        quarterAverage.append(average)

    quarterAverage = [float("{:.2f}".format(num)) for num in quarterAverage]
    generalTotal = sum(quarterAverage)
    generalAverage = generalTotal / subjCount

    Misc.load()
    reportCard(studentName,studentLevel,subjgrades,subjectslist,quarterAverage,generalAverage)

    newsubgrades=[]
    for i in subjgrades:
        for x in i:
            newsubgrades.append(x)
    with open('Elementary.txt','a') as elem:
        elem.write(studentName+'\n')
        for i in subjectslist:
            elem.write(i+' ')
        elem.write('\n')
        for i in newsubgrades:
            elem.write(str(i)+' ')
        elem.write('\n')
    print()

#student for highschool
def highschool():
    studentName=str(input("Enter student name: "))
    studentLevel="Highschool"
    while True:
        subjectslist = []
        subjCount =input("Enter the total number of subjects: ").strip()
        if subjCount in '1234567890':
            subjCount=int(subjCount)
            for i in range(int(subjCount)):
                subjectslist.append(input("Enter subject {}: ".format(i + 1)))
            break
        else:
            Misc.error()
    subjgrades=[]
    quarterTotal=[]
    quarterAverage=[]


    for subjects in subjectslist:
        print("Enter "+subjects+" grades per quarter")
        subjgrades.append(encodeQuartergrades())

    for grades in subjgrades:
        quarterTotal.append(sum(grades))

    for total in quarterTotal:
        average= total/4
        quarterAverage.append(average)

    quarterAverage = [float("{:.2f}".format(num)) for num in quarterAverage]
    generalTotal = sum(quarterAverage)
    generalAverage = generalTotal / subjCount

    Misc.load()
    reportCard(studentName,studentLevel,subjgrades,subjectslist,quarterAverage,generalAverage)

    newsubgrades = []
    for i in subjgrades:
        for x in i:
            newsubgrades.append(x)

    with open('Highschool.txt', 'a') as hs:
        hs.write(studentName+'\n')
        for i in subjectslist:
            hs.write(i+' ')
        hs.write('\n')
        for i in newsubgrades:
            hs.write(str(i) + ' ')
        hs.write('\n')
    print()


#student for college
def college():
    studentName=str(input("Enter student name: "))
    studentLevel="College"
    while True:
        subjectslist = []
        subjCount =input("Enter the total number of subjects: ").strip()
        if subjCount in '1234567890':
            subjCount=int(subjCount)
            for i in range(int(subjCount)):
                subjectslist.append(input("Enter subject {}: ".format(i + 1)))
            break
        else:
            Misc.error()
    subjgrades=[]
    quarterTotal=[]
    quarterAverage=[]

    for subjects in subjectslist:
        print("Enter "+subjects+" grades per semester")
        subjgrades.append(encodegradecollege())

    for grades in subjgrades:
        quarterTotal.append(sum(grades))

    for total in quarterTotal:
        average= total/2
        quarterAverage.append(average)

    quarterAverage = [float("{:.2f}".format(num)) for num in quarterAverage]
    generalTotal = sum(quarterAverage)
    generalAverage = generalTotal / subjCount

    Misc.load()
    reportCardcollege(studentName,studentLevel,subjgrades,subjectslist,quarterAverage,generalAverage)

    newsubgrades = []
    for i in subjgrades:
        for x in i:
            newsubgrades.append(x)

    with open('College.txt', 'a') as col:
        col.write(studentName+'\n')
        for i in subjectslist:
            col.write(i+' ')
        col.write('\n')
        for i in newsubgrades:
            col.write(str(i) + ' ')
        col.write('\n')
    print()