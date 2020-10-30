from time import sleep
def student():
    studentName=str(input("Enter student name: "))
    studentLevel="Elementary"

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
    loading = '..........'
    print("GENERATING REPORT CARD PLEASE WAIT",end=" ")
    for i in range(10):
        print(loading[i], sep=' ', end=' ', flush=True);
        sleep(0.5)
    print("\n")
    print("Name: "+studentName)
    print("Educational Level: "+studentLevel)
    print("                 1st      2nd      3rd      4th      Final    ")
    print("First Subject    "+str(firstSub[0])+"       "+str(firstSub[1])+"       "+str(firstSub[2])+"       "+
          str(firstSub[3])+"       "+str(firstFinal))
    print("%.2f" % generalAve)
