#function for viewing grades

def elementaryHasgrades():
    try:
        with open('Elementary.txt', 'r') as elem:
        # If file contains account, return True
            if elem.read():
                return True
        # If file does not contain account, return False
    except:
        return False

def highschoolHasgrades():
    with open('Elementary.txt', 'r') as elem:
        # If file contains account, return True
        if elem.read():
            return True
        # If file does not contain account, return False
        else:
            return False
def collegeHasgrades():
    with open('Elementary.txt', 'r') as elem:
        # If file contains account, return True
        if elem.read():
            return True
        # If file does not contain account, return False
        else:
            return False
def elemView():
    with open('Elementary.txt', 'rt') as readfile:
        readfile.readlines(0)
def viewGrade():
    while True:
        print("Select category\n1.Elementary\n2.Highschool\n3.College")
        select=int(input())
        if select==1:
            if elementaryHasgrades():
                print("There are entries found in Elementary category.")
                elemView()
            else:
                print("There are no entries found in Elementary category.")
                return False