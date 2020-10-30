from time import sleep

#student for elementary
def student():
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

    #code for load
    loading = '..........'
    print("GENERATING REPORT CARD PLEASE WAIT",end=" ")
    for i in range(10):
        print(loading[i], sep=' ', end=' ', flush=True);
        sleep(0.5)

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
