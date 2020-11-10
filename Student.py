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

#student for elementary
def elementary():
    studentName=str(input("Enter student name: "))
    studentLevel="Elementary"

#code for input of grades each sub per quarter
    firstSub = []
    print("Enter first subject grades per quarter:")
    for i in range(0,4):
        firstsubgrades=int(input())
        firstSub.append(firstsubgrades)

    secondSub = []
    print("Enter second subject grades per quarter:")
    for i in range(0, 4):
        secondsubgrades = int(input())
        secondSub.append(secondsubgrades)

    thirdSub = []
    print("Enter third subject grades per quarter:")
    for i in range(0, 4):
        thirdsubgrades= int(input())
        thirdSub.append(thirdsubgrades)

    fourthSub = []
    print("Enter fourth subject grades per quarter:")
    for i in range(0,4):
        fourthsubgrades= int(input())
        fourthSub.append(fourthsubgrades)

    fifthSub = []
    print("Enter fifth subject grades per quarter:")
    for i in range(0,4):
        fifthsubgrades=int(input())
        fifthSub.append(fifthsubgrades)

    sixthSub = []
    print("Enter sixth subject grades per quarter:")
    for i in range(0, 4):
        sixthsubgrades = int(input())
        sixthSub.append(sixthsubgrades)

    seventhSub = []
    print("Enter seventh subject grades per quarter:")
    for i in range(0, 4):
        seventhsubgrades = int(input())
        seventhSub.append(seventhsubgrades)

    eighthSub = []
    print("Enter eighth subject grades per quarter:")
    for i in range(0, 4):
        eighthsubgrades = int(input())
        eighthSub.append(eighthsubgrades)



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
    print("Name: "+studentName)
    print("Educational Level: "+studentLevel)
    print("                 1st      2nd      3rd      4th      Final    ")
    print("First Subject    "+str(firstSub[0])+"       "+str(firstSub[1])+"       "+str(firstSub[2])+"       "+
          str(firstSub[3])+"       "+str(firstFinal))
    print("Second Subject   " + str(secondSub[0]) + "       " + str(secondSub[1]) + "       " + str(
        secondSub[2]) + "       " +
          str(secondSub[3]) + "       " + str(secondFinal))
    print("Third Subject    " + str(thirdSub[0]) + "       " + str(thirdSub[1]) + "       " + str(
        thirdSub[2]) + "       " +
          str(thirdSub[3]) + "       " + str(thirdFinal))
    print("Fourth Subject   " + str(fourthSub[0]) + "       " + str(fourthSub[1]) + "       " + str(
        fourthSub[2]) + "       " +
          str(fourthSub[3]) + "       " + str(fourthFinal))
    print("Fifth Subject    " + str(fifthSub[0]) + "       " + str(fifthSub[1]) + "       " + str(
        fifthSub[2]) + "       " +
          str(fifthSub[3]) + "       " + str(fifthFinal))
    print("Sixth Subject    " + str(sixthSub[0]) + "       " + str(sixthSub[1]) + "       " + str(
        sixthSub[2]) + "       " +
          str(sixthSub[3]) + "       " + str(sixthFinal))
    print("Seventh Subject  " + str(seventhSub[0]) + "       " + str(seventhSub[1]) + "       " + str(
        seventhSub[2]) + "       " +
          str(seventhSub[3]) + "       " + str(seventhFinal))
    print("Eighth Subject   " + str(eighthSub[0]) + "       " + str(eighthSub[1]) + "       " + str(
        eighthSub[2]) + "       " +
          str(eighthSub[3]) + "       " + str(eightFinal))
    print("                                    General Average: "+"%.2f" % generalAve)
    print("                                            Remarks: "+str(determine_grade(generalAve)))
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

    # code for input of grades each sub per quarter
    firstSub = []
    print("Enter first subject grades per quarter:")
    for i in range(0, 4):
        firstsubgrades = int(input())
        firstSub.append(firstsubgrades)

    secondSub = []
    print("Enter second subject grades per quarter:")
    for i in range(0, 4):
        secondsubgrades = int(input())
        secondSub.append(secondsubgrades)

    thirdSub = []
    print("Enter third subject grades per quarter:")
    for i in range(0, 4):
        thirdsubgrades = int(input())
        thirdSub.append(thirdsubgrades)

    fourthSub = []
    print("Enter fourth subject grades per quarter:")
    for i in range(0, 4):
        fourthsubgrades = int(input())
        fourthSub.append(fourthsubgrades)

    fifthSub = []
    print("Enter fifth subject grades per quarter:")
    for i in range(0, 4):
        fifthsubgrades = int(input())
        fifthSub.append(fifthsubgrades)

    sixthSub = []
    print("Enter sixth subject grades per quarter:")
    for i in range(0, 4):
        sixthsubgrades = int(input())
        sixthSub.append(sixthsubgrades)

    seventhSub = []
    print("Enter seventh subject grades per quarter:")
    for i in range(0, 4):
        seventhsubgrades = int(input())
        seventhSub.append(seventhsubgrades)

    eighthSub = []
    print("Enter eighth subject grades per quarter:")
    for i in range(0, 4):
        eighthsubgrades = int(input())
        eighthSub.append(eighthsubgrades)

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
    print("Name: " + studentName)
    print("Educational Level: " + studentLevel)
    print("                 1st      2nd      3rd      4th      Final    ")
    print("First Subject    " + str(firstSub[0]) + "       " + str(firstSub[1]) + "       " + str(
        firstSub[2]) + "       " +
          str(firstSub[3]) + "       " + str(firstFinal))
    print("Second Subject   " + str(secondSub[0]) + "       " + str(secondSub[1]) + "       " + str(
        secondSub[2]) + "       " +
          str(secondSub[3]) + "       " + str(secondFinal))
    print("Third Subject    " + str(thirdSub[0]) + "       " + str(thirdSub[1]) + "       " + str(
        thirdSub[2]) + "       " +
          str(thirdSub[3]) + "       " + str(thirdFinal))
    print("Fourth Subject   " + str(fourthSub[0]) + "       " + str(fourthSub[1]) + "       " + str(
        fourthSub[2]) + "       " +
          str(fourthSub[3]) + "       " + str(fourthFinal))
    print("Fifth Subject    " + str(fifthSub[0]) + "       " + str(fifthSub[1]) + "       " + str(
        fifthSub[2]) + "       " +
          str(fifthSub[3]) + "       " + str(fifthFinal))
    print("Sixth Subject    " + str(sixthSub[0]) + "       " + str(sixthSub[1]) + "       " + str(
        sixthSub[2]) + "       " +
          str(sixthSub[3]) + "       " + str(sixthFinal))
    print("Seventh Subject  " + str(seventhSub[0]) + "       " + str(seventhSub[1]) + "       " + str(
        seventhSub[2]) + "       " +
          str(seventhSub[3]) + "       " + str(seventhFinal))
    print("Eighth Subject   " + str(eighthSub[0]) + "       " + str(eighthSub[1]) + "       " + str(
        eighthSub[2]) + "       " +
          str(eighthSub[3]) + "       " + str(eightFinal))
    print("                                    General Average: " + "%.2f" % generalAve)
    print("                                            Remarks: " + str(determine_grade(generalAve)))
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

    # code for input of grades each sub per quarter
    firstSub = []
    print("Enter first subject grades per semester:")
    for i in range(0, 2):
        firstsubgrades = int(input())
        firstSub.append(firstsubgrades)

    secondSub = []
    print("Enter second subject grades per semester:")
    for i in range(0, 2):
        secondsubgrades = int(input())
        secondSub.append(secondsubgrades)

    thirdSub = []
    print("Enter third subject grades per semester:")
    for i in range(0, 2):
        thirdsubgrades = int(input())
        thirdSub.append(thirdsubgrades)

    fourthSub = []
    print("Enter fourth subject grades per semester:")
    for i in range(0, 2):
        fourthsubgrades = int(input())
        fourthSub.append(fourthsubgrades)

    fifthSub = []
    print("Enter fifth subject grades per semester:")
    for i in range(0, 2):
        fifthsubgrades = int(input())
        fifthSub.append(fifthsubgrades)

    sixthSub = []
    print("Enter sixth subject grades per semester:")
    for i in range(0, 2):
        sixthsubgrades = int(input())
        sixthSub.append(sixthsubgrades)

    seventhSub = []
    print("Enter seventh subject grades per semester:")
    for i in range(0, 2):
        seventhsubgrades = int(input())
        seventhSub.append(seventhsubgrades)

    eighthSub = []
    print("Enter eighth subject grades per semester:")
    for i in range(0, 2):
        eighthsubgrades = int(input())
        eighthSub.append(eighthsubgrades)

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
    print("Name: " + studentName)
    print("Educational Level: " + studentLevel)
    print("                 1st      2nd      Final")
    print("First Subject    " + str(firstSub[0]) + "       " + str(firstSub[1]) + "       " + str(firstFinal))
    print("Second Subject   " + str(secondSub[0]) + "       " + str(secondSub[1]) + "       " + str(secondFinal))
    print("Third Subject    " + str(thirdSub[0]) + "       " + str(thirdSub[1]) + "       " + str(thirdFinal))
    print("Fourth Subject   " + str(fourthSub[0]) + "       " + str(fourthSub[1]) + "       " + str(fourthFinal))
    print("Fifth Subject    " + str(fifthSub[0]) + "       " + str(fifthSub[1]) + "       " + str(fifthFinal))
    print("Sixth Subject    " + str(sixthSub[0]) + "       " + str(sixthSub[1]) + "       " + str(sixthFinal))
    print("Seventh Subject  " + str(seventhSub[0]) + "       " + str(seventhSub[1]) + "       " + str(seventhFinal))
    print("Eighth Subject   " + str(eighthSub[0]) + "       " + str(eighthSub[1]) + "       " + str(eightFinal))
    print("                  General Average: " + "%.2f" % generalAve)
    print("                          Remarks: " + str(determine_grade(generalAve)))
    print("                           Rating: " + str(determine_rate(generalAve)))
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