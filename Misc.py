#This is where all the minor functions are found
from time import sleep
import Student
import Grades

#function for loading part
def load():
    loading = '..........'
    print()
    print("GENERATING REPORT CARD PLEASE WAIT", end=" ")
    for i in range(10):
        print(loading[i], sep=' ', end=' ', flush=True);
        sleep(0.5)
    print()

#function for error messages
def error(type='option'):
    if type=='option':
        print("Incorrect option. Please choose from the given options.")
    if type=='input':
        print("Incorrect input.")
    if type=='entry':
        print("There are no entries found in this category.")

#function for message if there is an entries found
def found():
    print("There are entries found in this category")

#function for startup
def startup():
    menu = 0
    while True:
        print("Welcome to Gradely: A Grade Encoding and Storage System")
        print("1.Encode grade\n2.View grades\n3.Exit")
        mainMenu = int(input())
        if mainMenu == 1:
            print("\nEncode grade\n")
            Student.encodeGrade()
        elif mainMenu == 2:
            print("\nView grades\n")
            Grades.viewGrade()
        elif mainMenu == 3:
            print("\nThank You for using Gradely!")
            break
        else:
            Misc.error()