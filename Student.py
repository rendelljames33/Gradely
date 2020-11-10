from time import sleep

#function for remarks
def determine_grade(genAve):
    if genAve >= 90 and genAve <= 100:
        return 'Outstanding'
    elif genAve >= 85 and genAve <= 89:
        return 'Very Satisfactory'
    elif genAve >= 80 and genAve <= 84:
        return 'Satisfactory'
    elif genAve >= 75 and genAve <= 79:
        return 'Fairly Satisfactory'
    elif genAve < 75:
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
    print("GENERATING REPORT CARD PLEASE WAIT", end=" ")
    for i in range(10):
        print(loading[i], sep=' ', end=' ', flush=True);
        sleep(0.5)

#function for encoding grade(elem and hs)
def encodegrade():
    listgrade=[]
    for i in range(0,4):
        grad=int(input())
        listgrade.append(grad)
    return listgrade

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
    for subjects in range(0,8):
        subj=str(input())
        listsubject.append(subj)
    return listsubject

#student for elementary
def elementary():
    studentName=str(input("Enter student name: "))
    studentLevel="Elementary"
    print("Enter subjects")
    subjectslist = encodesubject()
#code for input of grades each sub per quarter
    print("Enter "+subjectslist[0]+" grades per quarter:")
    firstSub = encodegrade()
    print("Enter "+subjectslist[1]+" grades per quarter:")
    secondSub = encodegrade()
    print("Enter "+subjectslist[2]+" grades per quarter:")
    thirdSub = encodegrade()
    print("Enter "+subjectslist[3]+" grades per quarter:")
    fourthSub = encodegrade()
    print("Enter "+subjectslist[4]+" grades per quarter:")
    fifthSub = encodegrade()
    print("Enter "+subjectslist[5]+" grades per quarter:")
    sixthSub = encodegrade()
    print("Enter "+subjectslist[6]+" grades per quarter:")
    seventhSub = encodegrade()
    print("Enter "+subjectslist[7]+" grades per quarter:")
    eighthSub = encodegrade()
#formula for all grades
    firstFinal=sum(firstSub)/len(firstSub)
    secondFinal=sum(secondSub)/len(secondSub)
    thirdFinal=sum(thirdSub)/len(thirdSub)
    fourthFinal=sum(fourthSub)/len(fourthSub)
    fifthFinal=sum(fifthSub)/len(fifthSub)
    sixthFinal=sum(sixthSub)/len(sixthSub)
    seventhFinal=sum(seventhSub)/len(seventhSub)
    eightFinal=sum(eighthSub)/len(eighthSub)
    generalAve=(firstFinal+secondFinal+thirdFinal+fourthFinal+fifthFinal+sixthFinal+seventhFinal+eightFinal)/8
    print("\n")
    load()
#printcode for the output
    print("\n")
    print("Name: " + studentName)
    print("Educational Level: " + studentLevel)
    print(f"{' ':<30}{'1st':<7}{'2nd':<7}{'3rd':<7}{'4th':<7}{'Final'}")
    print(f"{subjectslist[0]:<30}{str(firstSub[0]):<7}{str(firstSub[1]):<7}{str(firstSub[2]):<7}{str(firstSub[3]):<7}"
          f"{str(firstFinal)}")
    print(
        f"{subjectslist[1]:<30}{str(secondSub[0]):<7}{str(secondSub[1]):<7}{str(secondSub[2]):<7}{str(secondSub[3]):<7}"
        f"{str(secondFinal)}")
    print(f"{subjectslist[2]:<30}{str(thirdSub[0]):<7}{str(thirdSub[1]):<7}{str(thirdSub[2]):<7}{str(thirdSub[3]):<7}"
          f"{str(thirdFinal)}")
    print(
        f"{subjectslist[3]:<30}{str(fourthSub[0]):<7}{str(fourthSub[1]):<7}{str(fourthSub[2]):<7}{str(fourthSub[3]):<7}"
        f"{str(fourthFinal)}")
    print(f"{subjectslist[4]:<30}{str(fifthSub[0]):<7}{str(fifthSub[1]):<7}{str(fifthSub[2]):<7}{str(fifthSub[3]):<7}"
          f"{str(fifthFinal)}")
    print(f"{subjectslist[5]:<30}{str(sixthSub[0]):<7}{str(sixthSub[1]):<7}{str(sixthSub[2]):<7}{str(sixthSub[3]):<7}"
          f"{str(sixthFinal)}")
    print(
        f"{subjectslist[6]:<30}{str(seventhSub[0]):<7}{str(seventhSub[1]):<7}{str(seventhSub[2]):<7}{str(seventhSub[3]):<7}"
        f"{str(seventhFinal)}")
    print(
        f"{subjectslist[7]:<30}{str(eighthSub[0]):<7}{str(eighthSub[1]):<7}{str(eighthSub[2]):<7}{str(eighthSub[3]):<7}"
        f"{str(eightFinal)}")
    print("                                         General Average: " + "%.2f" % generalAve)
    print("                                                 Remarks: " + str(determine_grade(generalAve)))
    print()
    #changing lists into string for write
    firstSub=str(firstSub)
    secondSub=str(secondSub)
    thirdSub=str(thirdSub)
    fourthSub=str(fourthSub)
    fifthSub=str(fifthSub)
    sixthSub=str(sixthSub)
    seventhSub=str(seventhSub)
    eighthSub=str(eighthSub)

    with open('Elementary.txt','a') as elem:
        elem.write(studentName+'\n')
        elem.write(firstSub)
        elem.write(secondSub)
        elem.write(thirdSub)
        elem.write(fourthSub)
        elem.write(fifthSub)
        elem.write(sixthSub)
        elem.write(seventhSub)
        elem.write(eighthSub+'\n')

#student for highschool
def highschool():
    studentName = str(input("Enter student name: "))
    studentLevel = "Highschool"
    print("Enter subjects")
    subjectslist = encodesubject()

    # code for input of grades each sub per quarter
    print("Enter "+subjectslist[0]+" grades per quarter:")
    firstSub = encodegrade()
    print("Enter "+subjectslist[1]+" grades per quarter:")
    secondSub = encodegrade()
    print("Enter "+subjectslist[2]+" grades per quarter:")
    thirdSub = encodegrade()
    print("Enter "+subjectslist[3]+" grades per quarter:")
    fourthSub = encodegrade()
    print("Enter "+subjectslist[4]+" grades per quarter:")
    fifthSub = encodegrade()
    print("Enter "+subjectslist[5]+" grades per quarter:")
    sixthSub = encodegrade()
    print("Enter "+subjectslist[6]+" grades per quarter:")
    seventhSub = encodegrade()
    print("Enter "+subjectslist[7]+" grades per quarter:")
    eighthSub = encodegrade()

    # formula for all grades
    firstFinal = sum(firstSub) / len(firstSub)
    secondFinal = sum(secondSub) / len(secondSub)
    thirdFinal = sum(thirdSub) / len(thirdSub)
    fourthFinal = sum(fourthSub) / len(fourthSub)
    fifthFinal = sum(fifthSub) / len(fifthSub)
    sixthFinal = sum(sixthSub) / len(sixthSub)
    seventhFinal = sum(seventhSub) / len(seventhSub)
    eightFinal = sum(eighthSub) / len(eighthSub)
    generalAve = (firstFinal + secondFinal + thirdFinal + fourthFinal + fifthFinal +
                  sixthFinal + seventhFinal + eightFinal) / 8

    print("\n")

    load()

    # printcode for the output
    print("Name: "+studentName)
    print("Educational Level: "+studentLevel)
    print(f"{' ':<30}{'1st':<7}{'2nd':<7}{'3rd':<7}{'4th':<7}{'Final'}")
    print(f"{subjectslist[0]:<30}{str(firstSub[0]):<7}{str(firstSub[1]):<7}{str(firstSub[2]):<7}{str(firstSub[3]):<7}"
          f"{str(firstFinal)}")
    print(f"{subjectslist[1]:<30}{str(secondSub[0]):<7}{str(secondSub[1]):<7}{str(secondSub[2]):<7}{str(secondSub[3]):<7}"
          f"{str(secondFinal)}")
    print(f"{subjectslist[2]:<30}{str(thirdSub[0]):<7}{str(thirdSub[1]):<7}{str(thirdSub[2]):<7}{str(thirdSub[3]):<7}"
          f"{str(thirdFinal)}")
    print(f"{subjectslist[3]:<30}{str(fourthSub[0]):<7}{str(fourthSub[1]):<7}{str(fourthSub[2]):<7}{str(fourthSub[3]):<7}"
          f"{str(fourthFinal)}")
    print(f"{subjectslist[4]:<30}{str(fifthSub[0]):<7}{str(fifthSub[1]):<7}{str(fifthSub[2]):<7}{str(fifthSub[3]):<7}"
          f"{str(fifthFinal)}")
    print(f"{subjectslist[5]:<30}{str(sixthSub[0]):<7}{str(sixthSub[1]):<7}{str(sixthSub[2]):<7}{str(sixthSub[3]):<7}"
          f"{str(sixthFinal)}")
    print(f"{subjectslist[6]:<30}{str(seventhSub[0]):<7}{str(seventhSub[1]):<7}{str(seventhSub[2]):<7}{str(seventhSub[3]):<7}"
          f"{str(seventhFinal)}")
    print(f"{subjectslist[7]:<30}{str(eighthSub[0]):<7}{str(eighthSub[1]):<7}{str(eighthSub[2]):<7}{str(eighthSub[3]):<7}"
          f"{str(eightFinal)}")
    print("                                         General Average: "+"%.2f" % generalAve)
    print("                                                 Remarks: "+str(determine_grade(generalAve)))
    print()

    # changing lists into string for write
    firstSub = str(firstSub)
    secondSub = str(secondSub)
    thirdSub = str(thirdSub)
    fourthSub = str(fourthSub)
    fifthSub = str(fifthSub)
    sixthSub = str(sixthSub)
    seventhSub = str(seventhSub)
    eighthSub = str(eighthSub)

    with open('Highschool.txt', 'a') as hs:
        hs.write(studentName + '\n')
        hs.write(firstSub)
        hs.write(secondSub)
        hs.write(thirdSub)
        hs.write(fourthSub)
        hs.write(fifthSub)
        hs.write(sixthSub)
        hs.write(seventhSub)
        hs.write(eighthSub + '\n')

#student for college
def college():
    studentName = str(input("Enter student name: "))
    studentLevel = "College"
    print("Enter subjects")
    subjectslist = encodesubject()
    # code for input of grades each sub per quarter
    print("Enter " + subjectslist[0] + " grades per quarter:")
    firstSub = encodegradecollege()
    print("Enter " + subjectslist[1] + " grades per quarter:")
    secondSub = encodegradecollege()
    print("Enter " + subjectslist[2] + " grades per quarter:")
    thirdSub = encodegradecollege()
    print("Enter " + subjectslist[3] + " grades per quarter:")
    fourthSub = encodegradecollege()
    print("Enter " + subjectslist[4] + " grades per quarter:")
    fifthSub = encodegradecollege()
    print("Enter " + subjectslist[5] + " grades per quarter:")
    sixthSub = encodegradecollege()
    print("Enter " + subjectslist[6] + " grades per quarter:")
    seventhSub = encodegradecollege()
    print("Enter " + subjectslist[7] + " grades per quarter:")
    eighthSub = encodegradecollege()

    # formula for all grades
    firstFinal = sum(firstSub) / len(firstSub)
    secondFinal = sum(secondSub) / len(secondSub)
    thirdFinal = sum(thirdSub) / len(thirdSub)
    fourthFinal = sum(fourthSub) / len(fourthSub)
    fifthFinal = sum(fifthSub) / len(fifthSub)
    sixthFinal = sum(sixthSub) / len(sixthSub)
    seventhFinal = sum(seventhSub) / len(seventhSub)
    eightFinal = sum(eighthSub) / len(eighthSub)
    generalAve = (firstFinal + secondFinal + thirdFinal + fourthFinal + fifthFinal +
                  sixthFinal + seventhFinal + eightFinal) / 8
    print("\n")
    load()
    # printcode for the output
    print("\n")
    print("Name: "+studentName)
    print("Educational Level: "+studentLevel)
    print(f"{' ':<30}{'1st':<7}{'2nd':<7}{'Final'}")
    print(f"{subjectslist[0]:<30}{str(firstSub[0]):<7}{str(firstSub[1]):<7}"
          f"{str(firstFinal)}")
    print(f"{subjectslist[1]:<30}{str(secondSub[0]):<7}{str(secondSub[1]):<7}"
          f"{str(secondFinal)}")
    print(f"{subjectslist[2]:<30}{str(thirdSub[0]):<7}{str(thirdSub[1]):<7}"
          f"{str(thirdFinal)}")
    print(f"{subjectslist[3]:<30}{str(fourthSub[0]):<7}{str(fourthSub[1]):<7}"
          f"{str(fourthFinal)}")
    print(f"{subjectslist[4]:<30}{str(fifthSub[0]):<7}{str(fifthSub[1]):<7}"
          f"{str(fifthFinal)}")
    print(f"{subjectslist[5]:<30}{str(sixthSub[0]):<7}{str(sixthSub[1]):<7}"
          f"{str(sixthFinal)}")
    print(f"{subjectslist[6]:<30}{str(seventhSub[0]):<7}{str(seventhSub[1]):<7}"
          f"{str(seventhFinal)}")
    print(f"{subjectslist[7]:<30}{str(eighthSub[0]):<7}{str(eighthSub[1]):<7}"
          f"{str(eightFinal)}")
    print("                           General Average: "+"%.2f" % generalAve)
    print("                                   Remarks: "+str(determine_grade(generalAve)))

    # changing lists into string for write
    firstSub = str(firstSub)
    secondSub = str(secondSub)
    thirdSub = str(thirdSub)
    fourthSub = str(fourthSub)
    fifthSub = str(fifthSub)
    sixthSub = str(sixthSub)
    seventhSub = str(seventhSub)
    eighthSub = str(eighthSub)

    with open('College.txt', 'a') as col:
        col.write(studentName + '\n')
        col.write(firstSub)
        col.write(secondSub)
        col.write(thirdSub)
        col.write(fourthSub)
        col.write(fifthSub)
        col.write(sixthSub)
        col.write(seventhSub)
        col.write(eighthSub + '\n')