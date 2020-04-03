# This is a basic game called "Guess The Word", set up for two players. Player One must first enter a word,
# then Player Two must guess this word a letter at a time. For every letter that Player Two gets wrong, a shape will
# be drawn which will, after 8 wrong attempts, add up to a drawing of an ambulance, causing Player Two to lose the game.
# SRN: 18070042
# Last Modified:


# This initial section sets up the turtle's required for the game. I have a main turtle that draw most of the screen,
# I have include a turtle named 'tu' which controls the onscreen display of the number of guesses left, and finally
# I have created an empty list which I will use later on in the code to create a specific number of turtles, depending
# on the word length.

import turtle
tu = turtle.Turtle()
tu.hideturtle()
t = []

# This first function 'chooseWord' allows Player One to input their word and then converts it into a list.

def chooseWord():


    print("************************")
    print("       Player One")
    print("************************\n")
    print("Player Two look away!\n")
    playerChoice = input("Enter you word (if it has a space, use '-', e.g. ice-cream). Type 'F' to cancel: ")

    playerWord = []
    for i in range(len(playerChoice)): # This loop converts Player One's choice of word into a list.
        playerWord.append(playerChoice[i])

    for i in range(100): # The loop is used to clear the screen so that Player Two cannot see Player One's input.
        print("\n")

    return playerWord

# The second function, 'screenSetup', sets up the intial state of the game.

def screenSetup(playerWord, correctGuesses):

    turtle.title("Guess The Word!")
    turtle.setup(700, 800)
    turtle.bgcolor("#66B2FF")
    turtle.penup()
    turtle.goto(-300, 350)
    turtle.pencolor("yellow")
    turtle.write("Guess the word:", font=("MS Sans Serif", 20))
    turtle.goto(-300, -200)
    turtle.write("Wrong guesses:", font=("MS Sans Serif", 20))
    turtle.goto(-90, -300)
    turtle.write("You have", font=("MS Sans Serif", 15))
    tu.pencolor("yellow")
    tu.penup()
    tu.goto(0, -300)
    tu.write("8", font=("MS Sans Serif", 15))
    turtle.forward(110)
    turtle.write("guesses left", font=("MS Sans Serif", 15))
    turtle.goto(-300, 270)

    # This for loop creates a number of turtles equal to the number of characters in Player One's word.
    # I have done this so that each turtle will draw an asterisk to indicate the number of letters required
    # to guess. Then, when the letter is guess, I simply .undo() the turtle to remove the asterisk and replace it
    # with the guessed letter

    for i in range(len(playerWord)):
        t.append(turtle.Turtle())
        t[i].hideturtle()
        t[i].speed(10)

    x = -300
    y = 275
    for i in range(len(playerWord)):
        if playerWord[i] == "-": # This if statement takes into account any spaces.
            t[i].penup()
            t[i].pencolor("yellow")
            t[i].goto(x, y)
            t[i].write(" ", font = ("Arial", 35))
            x = x + 50
            correctGuesses.append(" ") # I have added each space to the correctGuesses list, so Player Two does not
                                       # not need to guess them.
        else:
            t[i].penup()
            t[i].pencolor("yellow")
            t[i].goto(x, y)
            t[i].write("*", font=("Arial", 35))
            x = x + 50

# This function deals with any wrong answers. It will keep track of the number of guesses left and draw the relevant
# section of the ambulance depending on this

def wrongAnswer(guessesLeft, letterChoice):

    print("Incorrect")

    if guessesLeft == 7:
        turtle.goto(-125, 0)
        turtle.pencolor("black")
        turtle.fillcolor("white")
        turtle.pensize(5)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(150)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(150)
        turtle.penup()
        turtle.goto(-300, -250)
        turtle.pencolor("yellow")
        turtle.write(letterChoice, font=("MS Sans Serif", 20))
        tu.undo()
        tu.write(guessesLeft, font=("MS Sans Serif", 15))
    elif guessesLeft == 6:
        turtle.pencolor("black")
        turtle.goto(25, 0)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(75)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(37)
        turtle.right(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(38)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-250, -250)
        turtle.pencolor("yellow")
        turtle.write(letterChoice, font=("MS Sans Serif", 20))
        tu.undo()
        tu.write(guessesLeft, font=("MS Sans Serif", 15))
    elif guessesLeft == 5:
        turtle.pencolor("black")
        turtle.goto(-80, 30)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(30)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-200, -250)
        turtle.pencolor("yellow")
        turtle.write(letterChoice, font=("MS Sans Serif", 20))
        tu.undo()
        tu.write(guessesLeft, font=("MS Sans Serif", 15))
    elif guessesLeft == 4:
        turtle.pencolor("black")
        turtle.goto(20, 30)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(30)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-150, -250)
        turtle.pencolor("yellow")
        turtle.write(letterChoice, font=("MS Sans Serif", 20))
        tu.undo()
        tu.write(guessesLeft, font=("MS Sans Serif", 15))
    elif guessesLeft == 3:
        turtle.pencolor("black")
        turtle.goto(60, 50)
        turtle.fillcolor("#E0E0E0")
        turtle.pensize(2)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(25)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-100, -250)
        turtle.pencolor("yellow")
        turtle.write(letterChoice, font=("MS Sans Serif", 20))
        tu.undo()
        tu.write(guessesLeft, font=("MS Sans Serif", 15))
    elif guessesLeft == 2:
        turtle.pencolor("black")
        turtle.goto(-25, 100)
        turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.pendown()
        for i in range(2):
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(10)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-50, -250)
        turtle.pencolor("yellow")
        turtle.write(letterChoice, font=("MS Sans Serif", 20))
        tu.undo()
        tu.write(guessesLeft, font=("MS Sans Serif", 15))
    elif guessesLeft == 1:
        turtle.goto(-40, 40)
        turtle.pencolor("red")
        turtle.pendown()
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(20)
            turtle.right(90)
            turtle.forward(40)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(0, -250)
        turtle.pencolor("yellow")
        turtle.write(letterChoice, font=("MS Sans Serif", 20))
        tu.undo()
        tu.write(guessesLeft, font=("MS Sans Serif", 15))
    else:
        turtle.goto(-30, 50)
        turtle.pencolor("red")
        turtle.begin_fill()
        turtle.pendown()
        for i in range(2):
            turtle.forward(40)
            turtle.right(90)
            turtle.forward(20)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(50, -250)
        turtle.pencolor("yellow")
        turtle.write(letterChoice, font=("MS Sans Serif", 20))
        tu.undo()
        tu.write(guessesLeft, font=("MS Sans Serif", 15))
        turtle.goto(0, 200)
        turtle.write("PLAYER ONE WINS!", align="center", font=("MS Sans Serif", 30))

    if guessesLeft == 0: # This statement sets playerLost to True in the main function, to indicate the game has ended
        return True
    else:
        return False

# The 'duplicateCheck' function ensure that the same letter cannot be entered twice.

def duplicateCheck(letterChoice, guessedLetters):

    if letterChoice in guessedLetters:
        return True
    else:
        guessedLetters.append(letterChoice)
        return False

# The 'winner' function runs when the guesser has correctly guessed the word.

def winner():
    turtle.goto(0, 200)
    turtle.pencolor("yellow")
    turtle.write("PLAYER TWO WINS!", align="center", font=("MS Sans Serif", 30))

# The 'restart' function asks the user at the end of each game if they wish to play again. If not, it returns False
# to main, which breaks out of the loop to continue playing.

def restart():

    anotherGame = input("\nGame over! Would you like to play again (Y/N): ")
    if (anotherGame == "N") or (anotherGame == "n"):
        return False
    else:
        return True



def main():

    playAgain = True

    while playAgain == True: # The main loop of the game.
        turtle.reset()
        turtle.hideturtle()
        playerLost = False
        guessesLeft = 8 # Sets the initial number of guesses.
        guessedLetters = [] # A list used to keep track of guessed letters, to check for any duplicates.
        correctGuesses = [] # A list used to keep track of correctly guessed letters, to determine when the game is won.
        playerWord = chooseWord() # The chooseWord function is cause to allow Player One to choose their word.
        screenSetup(playerWord, correctGuesses)

        print("************************")
        print("       Player Two")
        print("************************")

        while playerLost == False:
            letterChoice = input("\nGuess a letter: ")
            duplicateLetter = duplicateCheck(letterChoice, guessedLetters) # Checks to make sure the letter is not a duplicate
            if duplicateLetter == False:
                for i in range(len(playerWord)): # This loop compares the entered letter to the chosen word, to check for any matches.
                    if letterChoice == playerWord[i]:
                        print("You have guessed a letter")
                        for j in range(len(playerWord)): # This nested loop is necessary to display letters that appear more than once.
                            if playerWord[j] == letterChoice:
                                t[j].undo()
                                t[j].write(letterChoice, font = ("MS Sans Serif", 35))
                                correctGuesses.append(letterChoice) # Adds the correctly guessed letter to the correctGuesses list
                        break

                else:
                    guessesLeft = guessesLeft - 1 # If the guess is incorrect, the number of guesses left
                                                  # decreases and is passed to the wrongAnswer function
                    playerLost = wrongAnswer(guessesLeft, letterChoice)
            elif duplicateLetter == True:
                 print("Letter already guessed. Try again!")

            if len(correctGuesses) == len(playerWord): # When the length of the correctGuesses and playerWord list are equal, Player Two wins.
                winner()
                playerLost = True

        playAgain = restart() # Checks to see if the user wishes to play another game.
        turtle.clearscreen() # Resets the turtle window for the next game.









main()