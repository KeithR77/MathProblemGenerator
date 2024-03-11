import random

# RANDOM MATH PROBLEM ~ PYTHON PROGRAM #
    # Description:
    # =-=-=-=-=-=-=-
    # The user is given a random math problem out of 5 total options.
    # This is done by assigning random 'mathNums' between 1-100, 1-50, or 1-25. And implementing them into a set problem.
    # Each problem is contained within a while loop. This allows users to have multiple attempts at the problem in the event that they answer incorrectly.
    # If the user answers correctly, the 'incorrect' boolean is set to False, and it breaks out of the loop. Ending the program.



mathNum1 = random.randint(1, 30)
mathNum2 = random.randint(1, 15)
mathNum3 = random.randint(1, 5)

problemSelector = random.randint(1, 5)

print("Solve the following math problem: ")
incorrect = True

# PROBLEM 1:
if problemSelector == 1:
    while incorrect: 
        print(f"{mathNum1} + {mathNum2} - {mathNum3}")
        answer = int(input("Answer: "))
        if answer == mathNum1 + mathNum2 - mathNum3:
            print("You got it correct, nice job!")
            incorrect = False
            print("TERMINATING PROGRAM")
            break
        elif answer != mathNum1 + mathNum2 - mathNum3:
            print("You got it incorrect, try again!")



#PROBLEM 2:
if problemSelector == 2:            
    while incorrect:         
        print(f"{mathNum1} - {mathNum2} - {mathNum3} + {mathNum1}")
        answer = int(input("Answer: "))
        if answer == mathNum1 - mathNum2 - mathNum3 + mathNum1:
            print("You got it correct, nice job!")
            incorrect = False
            print("TERMINATING PROGRAM")
            break
        elif answer != mathNum1 - mathNum2 - mathNum3 + mathNum1:
            print("You got it incorrect, try again!")


#PROBLEM 3:
if problemSelector == 3:          
    while incorrect:  
        print(f"{mathNum1} + {mathNum2} * {mathNum3} * {mathNum3}")
        answer = int(input("Answer: "))
        if answer == mathNum1 + mathNum2 * mathNum3 * mathNum3:
            print("You got it correct, nice job!")
            incorrect = False
            print("TERMINATING PROGRAM")
            break
        elif answer != mathNum1 + mathNum2 * mathNum3 * mathNum3:
            print("You got it incorrect, try again!")


#PROBLEM 4:
if problemSelector == 4:
    while incorrect: 
        print(f"{mathNum1} / {mathNum2} * {mathNum3}")
        answer = int(input("Answer: "))
        if answer == mathNum1 / mathNum2 * mathNum3:
            print("You got it correct, nice job!")
            incorrect = False
            print("TERMINATING PROGRAM")
            break
        elif answer != mathNum1 / mathNum2 * mathNum3:
            print("You got it incorrect, try again!")


#PROBLEM 5:
if problemSelector == 5:
    while incorrect: 
        print(f"{mathNum1} + {mathNum3} / {mathNum3} * {mathNum3} + {mathNum1}")
        answer = int(input("Answer: "))
        if answer == mathNum1 + mathNum3 / mathNum3 * mathNum3 + mathNum1:
            print("You got it correct, nice job!")
            incorrect = False
            print("TERMINATING PROGRAM")
            break
        elif answer != mathNum1 + mathNum3 / mathNum3 * mathNum3 + mathNum1:
            print("You got it incorrect, try again!")