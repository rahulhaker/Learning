'''
Python Problems Solved
'''
#1. Guess the number - Takes input from user between 1-10, pick random number and check if user number is
# greater or lesser than print how many guesses did user make to get to the correct number

def CheckGreaterOrLesser(SystemNumber,UserNumber):
    if SystemNumber==UserNumber:
        return 0
    elif SystemNumber>UserNumber:
        return 1
    elif SystemNumber<UserNumber:
        return 2

def TakeInputFromUser(SystemNumber):
    NumberOfGuess = 0
    while True:
        UserNumber = int(input("Enter a Number b/W 1 to 10 to guess system number:"))
        NumberOfGuess+=1
        Result = CheckGreaterOrLesser(SystemNumber,UserNumber)
        if Result == 0: 
            print(f"Wow! You made it in {NumberOfGuess} number of guess.")
            break
        elif Result == 1: print(f"Your number {UserNumber} is lesser than system Number,Guess Again? Enter 'Y' to Proceed 'N' to End Guessing")
        elif Result == 2: print(f"Your number {UserNumber} is greater than system Number,Guess Again? Enter 'Y' to Proceed 'N' to End Guessing")
        UserInput = input()
        if UserInput == "N" or UserInput == "n":
            break
        elif NumberOfGuess>=7:
            print(f"Exceeded Max number of Guesses. System number is {SystemNumber}")

import random
SystemNumbers = random.sample(range(1,10),1)
SystemNumber = SystemNumbers[0]
print("Program#1 - Guess the Number")
#print(SystemNumbers,SystemNumber)
#TakeInputFromUser(SystemNumber)

#2 - Printing Pattern - Input from user number N and second number 0 or 1 for normal/reverse printing
def TakeUserInput():
    UserInputNumber = int(input("Enter Number of Max pattern to print? "))
    NormalorReverse = int(input("Want to print pattern in Reverse [1] or Normal [0]. \nEnter your choice...."))
    if bool(NormalorReverse) == False: 
        for i in range(UserInputNumber):
            for j in range(i+1):
                print("*",end =  "")
            print("\n",end = "")
    else:
        for i in reversed(range(UserInputNumber)):
            for j in range (i+1):
                print("*",end =  "")
            print("\n",end = "")
if __name__ == "__main__":
    print("Program#2 - Pattern Printing")
    #TakeUserInput()

#3 - Health Management System
with open("TestTextFile.txt",'r+') as f:
    a = f. readline()
    print (a)
print (f.readline())