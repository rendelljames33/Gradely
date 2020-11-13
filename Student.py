from time import sleep

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

#function for loading part
def load():
    loading = '..........'
    print()
    print("GENERATING REPORT CARD PLEASE WAIT", end=" ")
    for i in range(10):
        print(loading[i], sep=' ', end=' ', flush=True);
        sleep(0.5)
    print()

#function for encoding grade(elem and hs)
def encodeQuartergrades():
    quarterGrades=[]
    for i in range(0, 4):
        quarterGrades.append(int(input()))
    return quarterGrades

#function for encoding grade(college)
def encodegradecollege():
    listgrade=[]
    for i in range(0,2):
        grad=int(input())
        listgrade.append(grad)
    return listgrade

#function for encoding subjects
def encodesubject():
    listsubject = []
    subjCount =input("Enter the total number of subjects: ").strip()
    for i in range(int(subjCount)):
        listsubject.append(input("Enter subject {}: ".format(i + 1)))
    return listsubject

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
    studentLevel = int(input("Enter educational level (1=elementary,2=highschool,3=college): "))
    if studentLevel == 1:
        elementary()
    elif studentLevel == 2:
        highschool()
    elif studentLevel == 3:
        college()

#student for elementary
def elementary():
    studentName=str(input("Enter student name: "))
    studentLevel="Elementary"
    subjectslist = encodesubject()
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

    load()
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
    subjectslist = encodesubject()
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

    load()
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
    subjectslist = encodesubject()
    subjCount = len(subjectslist)
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

    load()
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