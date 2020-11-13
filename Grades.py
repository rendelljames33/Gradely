#function for viewing grades
import Misc
import Student

def elementaryHasgrades():
    try:
        with open('Elementary.txt', 'r') as elem:
            if elem.read():
                return True
    except:
        return False

def highschoolHasgrades():
    try:
        with open('Highschool.txt', 'r') as hs:
            if hs.read():
                return True
    except:
        return False
def collegeHasgrades():
    try:
        with open('College.txt', 'r') as col:
            if col.read():
                return True
    except:
        return False


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

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

def elemFile():
    with open('Elementary.txt','r') as elemData:
        return elemData.readlines()

def hsFile():
    with open('Highschool.txt','r') as hsData:
        return hsData.readlines()

def colFile():
    with open('College.txt','r') as colData:
        return colData.readlines()

def elemSearchGrade():
    with open('Elementary.txt', 'r') as searchElem:
        elem=[]
        num=0
        studentNames=[]
        for lines in searchElem.read().split("\n"):
            elem.append(lines)
        for names in elem[0::3]:
            if names:
                print("({}){}".format(num,names))
                num+=1
                studentNames.append(names)
        print()
        print("Select a student:")
        student = int(input())
        chosenStudent = studentNames[student]
        print(chosenStudent)
        print("Select an action:\n1.View grades\n2.Delete grades")
        action=int(input())
        pos = elem.index(chosenStudent)
        subject = elem[pos + 1].split()
        subjgrades = elem[pos + 2].split()
        newsubj = []
        newsubjgrades = []
        subjCount = len(subject)
        for x in subject:
            newsubj.append(str(x))
        for x in subjgrades:
            newsubjgrades.append(int(x))
            quartergrades = list(divide_chunks(newsubjgrades, 4))
            quartersum = [sum(i) for i in quartergrades]
            quarterAverage = []
            studentLevel = 'Elementary'
        for sums in quartersum:
            average = sums / 4
            quarterAverage.append(average)
        quarterAverage = [float("{:.2f}".format(num)) for num in quarterAverage]
        generalTotal = sum(quarterAverage)
        generalAverage = generalTotal / subjCount
        if action==1:
                Misc.load()
                Student.reportCard(chosenStudent,studentLevel,quartergrades,subject,quarterAverage,generalAverage)
                print()
        elif action==2:
                delete=str(input("Delete this entry? (y/n): ")).lower()
                if delete=='y':
                    data=elemFile()
                    for i in range(0,3):
                        data.pop(student)
                    with open('Elementary.txt','w') as elementary:
                        elementary.writelines(data)

def hsSeachGrade():
    with open('Highschool.txt', 'r') as searchHs:
        hs=[]
        num=0
        studentNames=[]
        for lines in searchHs.read().split("\n"):
            hs.append(lines)
        for names in hs[0::3]:
            if names:
                print("({}){}".format(num,names))
                num+=1
                studentNames.append(names)
        print()
        print("Select a student:")
        student=int(input())
        chosenStudent = studentNames[student]
        print(chosenStudent)
        print("Select an action:\n1.View grades\n2.Delete grades")
        action=int(input())
        pos = hs.index(chosenStudent)
        subject = hs[pos + 1].split()
        subjgrades = hs[pos + 2].split()
        newsubj = []
        newsubjgrades = []
        subjCount = len(subject)
        for x in subject:
            newsubj.append(str(x))
        for x in subjgrades:
            newsubjgrades.append(int(x))
        quartergrades = list(divide_chunks(newsubjgrades, 4))
        quartersum = [sum(i) for i in quartergrades]
        quarterAverage = []
        studentLevel = 'Highschool'
        for sums in quartersum:
            average = sums / 4
            quarterAverage.append(average)
        quarterAverage = [float("{:.2f}".format(num)) for num in quarterAverage]
        generalTotal = sum(quarterAverage)
        generalAverage = generalTotal / subjCount
        if action==1:
            Misc.load()
            Student.reportCard(chosenStudent,studentLevel,quartergrades,subject,quarterAverage,generalAverage)
            print()
        elif action==2:
            delete=str(input("Delete this entry? (y/n): ")).lower()
            if delete=='y':
                data=hsFile()
                for i in range(0,3):
                    data.pop(student)
                with open('Highschool.txt','w') as hs:
                    hs.writelines(data)

def colSearchGrades():
    with open('College.txt', 'r') as searchCol:
        col=[]
        num=0
        studentNames=[]
        for lines in searchCol.read().split("\n"):
            col.append(lines)
        for names in col[0::3]:
            if names:
                print("({}){}".format(num,names))
                num+=1
                studentNames.append(names)
        print()
        print("Select a student:")
        student=int(input())
        chosenStudent = studentNames[student]
        print(chosenStudent)
        print("Select an action:\n1.View grades\n2.Delete grades")
        action=int(input())
        pos = col.index(chosenStudent)
        subject = col[pos + 1].split()
        subjgrades = col[pos + 2].split()
        newsubj = []
        newsubjgrades = []
        subjCount = len(subject)
        for x in subject:
            newsubj.append(str(x))
        for x in subjgrades:
            newsubjgrades.append(int(x))
        quartergrades = list(divide_chunks(newsubjgrades, 2))
        quartersum = [sum(i) for i in quartergrades]
        quarterAverage = []
        studentLevel = 'College'
        for sums in quartersum:
            average = sums / 2
            quarterAverage.append(average)
        quarterAverage = [float("{:.2f}".format(num)) for num in quarterAverage]
        generalTotal = sum(quarterAverage)
        generalAverage = generalTotal / subjCount
        if action==1:
            Misc.load()
            Student.reportCardcollege(chosenStudent,studentLevel,quartergrades,subject,quarterAverage,generalAverage)
            print()
        elif action==2:
            delete=str(input("Delete this entry? (y/n): ")).lower()
            if delete=='y':
                data=colFile()
                for i in range(0,3):
                    data.pop(student)
                with open('College.txt','w') as college:
                    college.writelines(data)

def viewGrade():
    while True:
        print("Select category\n1.Elementary\n2.Highschool\n3.College\n4.Back")
        select=input()
        if select in '1234':
            select=int(select)
            if select==1:
                if elementaryHasgrades():
                    Misc.found()
                    elemSearchGrade()
                else:
                    Misc.error(type='entry')
            elif select==2:
                if highschoolHasgrades():
                    Misc.found()
                    hsSeachGrade()
                else:
                    Misc.error(type='entry')
            elif select==3:
                if collegeHasgrades():
                    Misc.found()
                    colSearchGrades()
                else:
                    Misc.error(type='entry')
            elif select==4:
                break
            else:
                Misc.error()
        else:
            Misc.error()

