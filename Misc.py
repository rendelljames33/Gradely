from time import sleep
#This is where minor functions are found

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