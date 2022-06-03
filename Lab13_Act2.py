# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Sriram Mittal
#               Cyrus Buhariwala
#               Jky Martin
#               Tyler Kaluza
# Section:      509
# Assignment:   Lab13_Act2
# Date:         3 December 2019

#
import random as r

# Functions for dice graphics
def die1():
    print("   ______",'\n'," /     /|",'\n',"+-----+ |",'\n',"|     | |",'\n',"|  o  | |",'\n',"|     |/",'\n',"+-----+")
def die2():
    print("   ______",'\n'," /     /|",'\n',"+-----+ |",'\n',"|o    | |",'\n',"|     | |",'\n',"|    o|/",'\n',"+-----+")
def die3():
    print("   ______",'\n'," /     /|",'\n',"+-----+ |",'\n',"|o    | |",'\n',"|  o  | |",'\n',"|    o|/",'\n',"+-----+")
def die4():
    print("   ______",'\n'," /     /|",'\n',"+-----+ |",'\n',"|o   o| |",'\n',"|     | |",'\n',"|o   o|/",'\n',"+-----+")
def die5():
    print("   ______",'\n'," /     /|",'\n',"+-----+ |",'\n',"|o   o| |",'\n',"|  o  | |",'\n',"|o   o|/",'\n',"+-----+")
def die6():
    print("   ______",'\n'," /     /|",'\n',"+-----+ |",'\n',"|o   o| |",'\n',"|o   o| |",'\n',"|o   o|/",'\n',"+-----+")

def die(n): # Function to decide which die value to display
    if n == 1:
        die1()
    if n == 2:
        die2()
    if n == 3:
        die3()
    if n == 4:
        die4()
    if n == 5:
        die5()
    if n == 6:
        die6()

def roll(dice_vals,dice): # Function to roll the dice
    """
    used to roll our die and display them
    """
    is_show = False
    
    for i in range(len(dice_vals)): # Find the values of the dice

        if dice[i] == True: # Check if dice is suppose to roll
            dice_vals[i] = r.randint(1,6) # Randomly generate new value
            print("\n\nDie #"+str(i+1)) # Display the dice
            die(dice_vals[i])
        else:
            is_show = True
            
    if is_show == True: # Display you current kept die if necessary
        show(dice_vals,dice)
        
def lastRoll(dice_vals,dice): # Same as roll except it does not display the die or check for kept die
    """
    used for the last roll same as roll excepet doesnt diplay the die
    """
    for i in range(len(dice_vals)):
        if dice[i] == True:
            dice_vals[i] = r.randint(1, 6)
            
def show(dice_vals,dice): # Function to show which dice are kept
    """
    used to show the current kept die
    """
    print("\n\nYour current kept die: ")
    for i in range(len(dice)):
        if dice[i] == False:
            print("\nDie #"+str(i+1))
            die(dice_vals[i])
            
def display(dice_vals): # Function to display all of the current dice; uses die function
    """
    used to display all your die at the end of the turn
    """
    for i in range(5):
        die(dice_vals[i])

def ones(dice_vals): # Function to add all the ones in the final dice
    """
    takes the dice values and adds all the ones in it and returns that number, if there are none, then it returns zero
    """
    sum = 0
    for i in range(len(dice_vals)):
        if dice_vals[i] == 1:
            sum += 1
        else:
            sum += 0
    return sum

def twos(dice_vals): # Function to add all the twos in the final dice
    """
    takes the dice values and adds all the twos in it and returns that number, if there are none, then it returns zero
    """
    sum = 0
    for i in range(len(dice_vals)):
        if dice_vals[i] == 2:
            sum += 2
        else:
            sum += 0
    return sum

def threes(dice_vals): # Function to add all the threes in the final dice
    """
    takes the dice values and adds all the threes in it and returns that number, if there are none, then it returns zero
    """
    sum = 0
    for i in range(len(dice_vals)):
        if dice_vals[i] == 3:
            sum += 3
        else:
            sum += 0
    return sum

def fours(dice_vals): # Function to add all the fours in the final dice
    """
    takes the dice values and adds all the fours in it and returns that number, if there are none, then it returns zero
    """
    sum = 0
    for i in range(len(dice_vals)):
        if dice_vals[i] == 4:
            sum += 4
        else:
            sum += 0
    return sum

def fives(dice_vals): # Function to add all the fives in the final dice
    """
    takes the dice values and adds all the fives in it and returns that number, if there are none, then it returns zero
    """
    sum = 0
    for i in range(len(dice_vals)):
        if dice_vals[i] == 5:
            sum += 5
        else:
            sum += 0
    return sum

def sixes(dice_vals): # Function to add all the sixes in the final dice
    """
    takes the dice values and adds all the sixes in it and returns that number, if there are none, then it returns zero
    """
    sum = 0
    for i in range(len(dice_vals)):
        if dice_vals[i] == 6:
            sum += 6
        else:
            sum += 0
    return sum

def three_of_akind(dice_vals): # Function adds all the dice up if there are three of a kind
    """
    takes the dice values to check if there is a three-of-a-kind, if there is then it adds all the dice values and returns that number, if there isn’t one then it returns zero
    """
    sum = 0
    dice_vals.sort() # We sort the values so the following if statements will work
    if dice_vals[0] == dice_vals[1] == dice_vals[2]: # If first three are the same
        for i in range(len(dice_vals)):
            sum += dice_vals[i]
    elif dice_vals[1] == dice_vals[2] == dice_vals[3]: # If second three are the same
        for i in range(len(dice_vals)):
            sum += dice_vals[i]
    elif dice_vals[2] == dice_vals[3] == dice_vals[4]: # If last three are the same
        for i in range(len(dice_vals)):
            sum += dice_vals[i]
    else: # If none then score of 0
        sum = 0
    return sum

def four_of_akind(dice_vals): # Function adds all the dice up if there are four of a kind
    """
    takes the dice values to check if there is a four-of-a-kind, if there is then it adds all the dice values and returns that number, if there isn’t one then it returns zero
    """
    sum = 0
    dice_vals.sort() # We sort the values so the following if statements will work
    if dice_vals[0] == dice_vals[1] == dice_vals[2] == dice_vals[3]: # If first four are the same
        for i in range(len(dice_vals)):
            sum += dice_vals[i]
    elif dice_vals[1] == dice_vals[2] == dice_vals[3] == dice_vals[4]: # If last four are the same
        for i in range(len(dice_vals)):
            sum += dice_vals[i]
    return sum

def full_house(dice_vals): # Function gives a score of 25 if dice make a full house (three-of-a-kind and a pair)
    """
    takes the dice values and checks to see if there is a full house(a three-of-a-kind and a pair) and if there is then it returns a value of 25, if there is not then it returns zero
    """
    sum = 0
    dice_vals.sort() # We sort the values so the following if statements will work
    if dice_vals[0] == dice_vals[1] == dice_vals[2]: # If first 3 are same
        if dice_vals[3] == dice_vals[4]: # ... and last 2 are the same
            sum = 25
    elif dice_vals[2] == dice_vals[3] == dice_vals[4]: # If last 3 are same
        if dice_vals[0] == dice_vals[1]: #If first 2 are the same
            sum = 25
    else: # If not score of 0
        sum = 0
    return sum

def small_straight(dice_vals): # Function gives a score of 30 if user has a small straight(4 in a order)
    """
    takes the dice values and checks to see if there is a small straight(4 numbers in order) and if there is then it returns a value of 30, if there is not then it returns zero
    """
    sum = 0
    dice_vals.sort() # We sort the values so the following if statements will work
    if (dice_vals[0] == 1 or dice_vals[1] == 1) and (dice_vals[1] == 2 or dice_vals[2] == 2) and (
            dice_vals[2] == 3 or dice_vals[3] == 3) and (dice_vals[3] == 4 or dice_vals[4] == 4):#if 1,2,3,4 anywhere
        sum = 30
    elif (dice_vals[0] == 2 or dice_vals[1] == 2) and (dice_vals[1] == 3 or dice_vals[2] == 3) and (
            dice_vals[2] == 4 or dice_vals[3] == 4) and (dice_vals[3] == 5 or dice_vals[4] == 5):#if 2,3,4,5 anywhere
        sum = 30
    elif (dice_vals[0] == 3 or dice_vals[1] == 3) and (dice_vals[1] == 4 or dice_vals[2] == 4) and (
            dice_vals[2] == 5 or dice_vals[3] == 5) and (dice_vals[3] == 6 or dice_vals[4] == 6):#if 3,4,5,6 anywhere
        sum = 30
    else: # If not score of 0
        sum = 0

    return sum

def large_straight(dice_vals): # Function gives a score of 40 if user has a large straight (5 in order)
    """
    takes the dice values and checks to see if there is a large straight (5 numbers in order) and if there is then it returns a value of 40, if there is not then it returns zero
    """
    sum = 0
    dice_vals.sort()
    if (dice_vals[0] == 1 and dice_vals[1] == 2 and dice_vals[2] == 3 and dice_vals[3] == 4 and dice_vals[4] == 5): #if 1,2,3,4,5
        sum = 40
    elif (dice_vals[0] == 2 and dice_vals[1] == 3 and dice_vals[2] == 4 and dice_vals[3] == 5 and dice_vals[4] == 6):#if 2,3,4,5,6
        sum = 40
    else: # If not score is 0
        sum = 0
    return sum

def yahtzee(dice_vals): # Function gives a score of 50 if user has a yahtzee(5 of a kind)
    """
    takes the dice values and checks to see if there is a yahtzee (5 of a kind) and if there is then it returns a value of 50, if there is not then it returns zero
    """
    sum = 0
    if dice_vals[0] == dice_vals[1] == dice_vals[2] == dice_vals[3] == dice_vals[4]:#if all 5 match
        sum = 50
    else: # If not score is 0
        sum = 0
    return sum

def chance(dice_vals):# Function adds all the dice up(no order or specifics required)
    """
    takes the sum of the dice values and returns that number
    """
    sum = 0
    for i in range(len(dice_vals)):
        sum += dice_vals[i]

    return sum





# Welcome for the user
print('\n\nWelcome to Yahtzee!')
print('This program was made by Cyrus Buhariwala, Tyler Kaluza, Jky Martin, and Sriram Mittal.')

# Display a set of instructions
print('\nInstructions:')
print('- To play Yahtzee, you try and collect the most amount of points throughout the game.')
print('- For each turn, you get to intially roll 5 dice and choose to keep or reroll which dice you want.')
print('- At the end or during each turn, you choose which category you want to get your points from.')
print('- If you have no option to choose a category, you can choose to put zero on one of the categories.\n')

# Display the value of each category
print('\nScoring:')
print('- For each 1,2,3,4,5,6 it is the cumulative value of only the number.')
print('- For a three and four of a kind, you need three or four of the same numbers and its the cumulative value of all your numbers displayed.')
print('- A small straight (4 values in a row, ex. 1-2-3-4) is worth 30 points and a large straight (5 values in a row) is worth 40 points.')
print('- A yahtzee is all 5 dice that are the same numbers and is worth 50 points.')
print('- Chance is the cumulative value of all of your dice.\n')

play = input("Press Enter to Continue.") # Allows player to actually read the instructions

dice = [True,True,True,True,True] # Initial dice boolean values; changed later when choosing to keep or roll

dice_vals = [0,0,0,0,0] # Initial dice integer values; changed later

roll_count = 3 # Used to limit turns; incremented later
        
total = 0
scorecard = {'Ones':-1,'Twos':-1,'Threes':-1,'Fours':-1,'Fives':-1,'Sixes':-1,'ThreeOfAKind':-1,'FourOfAKind':-1,'FullHouse':-1,'SmallStraight':-1,'LargeStraight':-1,'Yahtzee':-1,'Chance':-1} #dictionary used for score card

turnCount = 1 # Used to keep track of roll #

for i in range(13): # Loop for 13 turns

    while roll_count > 0: # ACTUAL GAME PROCESS
        try: # With valid input
            if(roll_count == 1): # If its the last roll call last roll
                lastRoll(dice_vals,dice)
                print("\nRoll #"+str(turnCount))

            if(roll_count > 1): # If not the last roll
                roll(dice_vals, dice) # Roll the dice
                print("\n\nRoll #"+str(turnCount))
                choice = input('Which die would you like to keep?\nInput with spaced numbers. If you wish to keep none enter "no".\nYour Choice: ').split(" ") #ask which you would like to keep

            if roll_count < 3 and roll_count > 1:
                choice2 = input('Do you want to roll any of your kept die? If not, enter "no".\nYour Choice: ').split(" ") #ask if you would like to roll a kept die

                if choice2[0] == 'no': # If you do not want to roll a kept die
                    if (choice[0] != 'no'):  # If you  want to keep certain die
                        for i in range(len(choice)): # Change the die inputted to false so it doesnt roll
                            dice[int(choice[i])-1] = False
                else:
                    if (choice[0] != 'no'): # If you want to keep any die
                        for i in range(len(choice)):
                            dice[int(choice[i])-1] = False # Change the die inputted to false so it doesnt roll
                        for i in range(len(choice2)):
                            dice[int(choice2[i])-1] = True # Change the kept die to roll so they can roll
                    else:
                        for i in range(len(choice2)): # Otherwise if you don't want to keep any die change the kept die
                            dice[int(choice2[i])-1] = True
            else:
                if(choice[0] != 'no' ):
                    for i in range(len(choice)):
                        dice[int(choice[i]) - 1] = False
            print("\n-------------------------------------------------")
            roll_count -= 1
            turnCount+=1
        except: # If invalid input
            fail = input("Invalid input try again by pressing Enter.")
    print()
    display(dice_vals)
    print("\n\nRoll #"+str(turnCount))
    print("These are your final dice.")
    print('\nChoose the category you want your dice to be scored.')
    print('\nYour options are "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sevens", "ThreeOfAKind", "FourOfAKind", "FullHouse", "SmallStraight", "LargeStraight", "Yahtzee", or "Chance".')
    inputUser = input('Your Choice: ')
    turnCount = 1 # Reset turn count
    
    valid = False
    while(valid == False): # While you have an invalid input
        if inputUser in scorecard: # Check to see if category exists
            # Check to see the correct category and it not being scored already
            if inputUser == 'Ones' and scorecard[inputUser] == -1:
                scorecard['Ones'] = ones(dice_vals)  # update score
                total += scorecard[inputUser] # Add total score
                valid = True # Change input to valid
            elif inputUser == 'Twos' and scorecard[inputUser] == -1:
                scorecard['Twos'] = twos(dice_vals)
                total += scorecard[inputUser]
                valid = True
            elif inputUser == 'Threes' and scorecard[inputUser] == -1:
                scorecard['Threes'] = threes(dice_vals)
                total += scorecard[inputUser]
                valid = True
            elif inputUser == 'Fours' and scorecard[inputUser] == -1:
                scorecard['Fours'] = fours(dice_vals)
                total += scorecard[inputUser]
                valid = True
            elif inputUser == 'Fives' and scorecard[inputUser] == -1:
                scorecard['Fives'] = fives(dice_vals)
                total += scorecard[inputUser]
                valid = True
            elif inputUser == 'Sixes' and scorecard[inputUser] == -1:
                scorecard['Sixes'] = sixes(dice_vals)
                total += scorecard[inputUser]
                valid = True
            elif inputUser == 'ThreeOfAKind' and scorecard[inputUser] == -1:
                scorecard['ThreeOfAKind'] = three_of_akind(dice_vals)
                total += scorecard[inputUser]
                valid = True
            elif inputUser == 'FourOfAKind' and scorecard[inputUser] == -1:
                scorecard['FourOfAKind'] = four_of_akind(dice_vals)
                total += scorecard[inputUser]
                valid = True
            elif inputUser == 'FullHouse' and scorecard[inputUser] == -1:
                scorecard['FullHouse'] = full_house(dice_vals)
                total += scorecard[inputUser]
                valid = True
            elif inputUser == 'SmallStraight' and scorecard[inputUser] == -1:
                scorecard['SmallStraight'] = small_straight(dice_vals)
                total += scorecard[inputUser]
                valid = True
            elif inputUser == 'LargeStraight' and scorecard[inputUser] == -1:
                scorecard['LargeStraight'] = large_straight(dice_vals)
                total += scorecard[inputUser]
                valid = True
            elif inputUser == 'Yahtzee' and scorecard[inputUser] == -1:
                scorecard['Yahtzee'] = yahtzee(dice_vals)
                total += scorecard[inputUser]
                valid = True
            elif inputUser == 'Chance' and scorecard[inputUser] == -1:
                scorecard['Chance'] = chance(dice_vals)
                total += scorecard[inputUser]
                valid = True
            else: # Invalid input ask again
                print('\nThat category has already been used.')
                print('\nYour options are "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sevens", "ThreeOfAKind", "FourOfAKind", "FullHouse", "SmallStraight", "LargeStraight", "Yahtzee", or "Chance".')
                print("\nReminder: Those are all of the catagories. Be sure to choose one that hasn't been used yet.")
                inputUser = input('Your Choice: ')
        else: # Invalid input ask again
            print('\nYou entered an invalid category.')
            print('Your options are "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sevens", "ThreeOfAKind", "FourOfAKind", "FullHouse", "SmallStraight", "LargeStraight", "Yahtzee", or "Chance".')
            print('Choose the category in which you want your dice to be scored.')
            inputUser = input("Your Choice: ")


    with open("Yahtzee!_ScoreCard.tsv", 'w') as myfile: # Write the scorecard
        
        # Welcome for the user
        myfile.write('\n\nWelcome to Yahtzee!')
        myfile.write('\nThis program was made by Cyrus Buhariwala, Tyler Kaluza, Jky Martin, and Sriram Mittal. \n')

        # Display a set of instructions
        myfile.write('\nInstructions:\n')
        myfile.write('- To play Yahtzee, you try and collect the most amount of points throughout the game. \n')
        myfile.write('- For each turn, you get to intially roll 5 dice and choose to keep or reroll which dice you want. \n')
        myfile.write('- At the end or during each turn, you choose which category you want to get your points from. \n')
        myfile.write('- If you have no option to choose a category, you can choose to put zero on one of the categories.\n')

        # Display the value of each category
        myfile.write('\nScoring:\n')
        myfile.write('- For each 1,2,3,4,5,6 it is the cumulative value of only the number.')
        myfile.write('- For a three and four of a kind, you need three or four of the same numbers and its the cumulative value of all your numbers displayed. \n')
        myfile.write('- A small straight (4 values in a row, ex. 1-2-3-4) is worth 30 points and a large straight (5 values in a row) is worth 40 points. \n')
        myfile.write('- A yahtzee is all 5 dice that are the same numbers and is worth 50 points. \n')
        myfile.write('- Chance is the cumulative value of all of your dice.\n')
        if(scorecard["Ones"] != -1): # If the score exists
            myfile.write("Ones:" + "\t\t\t\t"+ str(scorecard["Ones"]))
            myfile.write(str("\n"))
        else: # If it does not exist
            myfile.write("Ones:" + "\t\t\t\t")
            myfile.write(str("\n"))
        if (scorecard["Twos"] != -1):
            myfile.write("Twos:" + "\t\t\t\t" + str(scorecard["Twos"]))
            myfile.write(str("\n"))
        else:
            myfile.write("Twos:" + "\t\t\t\t")
            myfile.write(str("\n"))
        if (scorecard["Threes"] != -1):
            myfile.write("Threes:" + "\t\t\t\t" + str(scorecard["Threes"]))
            myfile.write(str("\n"))
        else:
            myfile.write("Threes:" + "\t\t\t\t")
            myfile.write(str("\n"))
        if (scorecard["Fours"] != -1):
            myfile.write("Fours:" + "\t\t\t\t" + str(scorecard["Fours"]))
            myfile.write(str("\n"))
        else:
            myfile.write("Fours:" + "\t\t\t\t")
            myfile.write(str("\n"))
        if (scorecard["Fives"] != -1):
            myfile.write("Fives:" + "\t\t\t\t" + str(scorecard["Fives"]))
            myfile.write(str("\n"))
        else:
            myfile.write("Fives:" + "\t\t\t\t")
            myfile.write(str("\n"))
        if (scorecard["Sixes"] != -1):
            myfile.write("Sixes:" + "\t\t\t\t" + str(scorecard["Sixes"]))
            myfile.write(str("\n"))
        else:
            myfile.write("Sixes:" + "\t\t\t\t")
            myfile.write(str("\n"))
        if (scorecard["ThreeOfAKind"] != -1):
            myfile.write("Three of a Kind:" + "\t" + str(scorecard["ThreeOfAKind"]))
            myfile.write(str("\n"))
        else:
            myfile.write("Three of a Kind:" + "\t")
            myfile.write(str("\n"))
        if (scorecard["FourOfAKind"] != -1):
            myfile.write("Four of a Kind:" + "\t\t" + str(scorecard["FourOfAKind"]))
            myfile.write(str("\n"))
        else:
            myfile.write("Four of a Kind:" + "\t\t")
            myfile.write(str("\n"))
        if (scorecard["FullHouse"] != -1):
            myfile.write("Full House:" + "\t\t\t" + str(scorecard["FullHouse"]))
            myfile.write(str("\n"))
        else:
            myfile.write("Full House:" + "\t\t\t")
            myfile.write(str("\n"))
        if (scorecard["SmallStraight"] != -1):
            myfile.write("Small Straight:" + "\t\t" + str(scorecard["SmallStraight"]))
            myfile.write(str("\n"))
        else:
            myfile.write("Small Straight:" + "\t\t")
            myfile.write(str("\n"))
        if (scorecard["LargeStraight"] != -1):
            myfile.write("Large Straight:" + "\t\t" + str(scorecard["LargeStraight"]))
            myfile.write(str("\n"))
        else:
            myfile.write("Large Straight:" + "\t\t")
            myfile.write(str("\n"))
        if (scorecard["Yahtzee"] != -1):
            myfile.write("Yahtzee:" + "\t\t\t" + str(scorecard["Yahtzee"]))
            myfile.write(str("\n"))
        else:
            myfile.write("Yahtzee:" + "\t\t\t")
            myfile.write(str("\n"))
        if (scorecard["Chance"] != -1):
            myfile.write("Chance:" + "\t\t\t\t" + str(scorecard["Chance"]))
            myfile.write(str("\n"))
        else:
            myfile.write("Chance:" + "\t\t\t\t")
            myfile.write(str("\n"))
        myfile.write("Total Score:" +"\t\t"+ str(total))
    
    roll_count = 3 # Reset roll count
    dice_vals = [0,0,0,0,0] # Reset dice values
    dice = [True,True,True,True,True] # Reset dice to roll all
    print("\nYou recieved", scorecard[inputUser], "point(s).")
    print("You can now view your updated scorecard.")
    play = input("Press Enter to Continue or 'Q' to quit ")  # Allows player to quit game
    if (play == 'Q' or play == "q"): # Exit loop
        break

print("\n----------------------------------------------------------------------\n")
print("Game Over")
print("\nFinal Score:", total) # Print final score


#