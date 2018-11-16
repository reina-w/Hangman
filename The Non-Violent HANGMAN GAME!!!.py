from turtle import *
from random import randint
import time

wordList = ['advocate', 'alleviate', 'allege', 'alienate', 'awestruck', \
            'belie', 'bolster', 'callous', 'capricious', 'caricature', \
            'censure', 'circumscribe', 'conciliate', 'condescend', \
            'convoluted', 'corroborate', 'cunning', 'dearth', 'debunk', \
            'deliberate', 'demeanor', 'digress', 'diplomatic', 'discreet', \
            'descrepancy', 'disgruntled', 'disillusioned', 'disingenuous', \
            'disparate', 'dogmatic', 'eccentric', 'elucidate', 'embellish', \
            'emphatic', 'epitome', 'equivocal', 'esteemed', 'estrangement', \
            'extravagant', 'fallible', 'flagrant', 'frugal', 'gullible',\
            'illusory', 'impetuous', 'implausible', 'inconsequencial', \
            'incontrovertible', 'incredulous', 'indignant', 'inquisitive', \
            'interrogate', 'intuitive', 'invigorate', 'lament', \
            'legitimate', 'meticulous', 'negligent', 'orthodox', \
            'partisan', 'precedent', 'pusillanimous', 'reiterate', \
            'reminiscene', 'reprehensible', 'resilient', \
            'rhetoric', 'scrupulous', 'spontaneous', 'susceptible', \
            'thwart', 'venerate', 'vigilant', 'vindicate', 'weary', \
            'whimsical', 'zealous']

sw = 1000
sl = 1000
s = getscreen()
s.setup(sw, sl)
s.bgcolor('#3e0059')

t = getturtle()
t.hideturtle()
t.color('white')
t.speed(0)

#variables to play the game
alpha = "abcdefghijklmnopqrstuvwxyz"
letterWrong = "" # starting as empty strings
letterCorrect = ""
secretWord = ""
displayWord = ""
fails = 9 # how many wrong guesses you have
fontSize = int(sl * 0.04)
gameDone = False

# Another Turtle
tWriter = Turtle() # ask for another turtle -- initializer
tWriter.hideturtle()
tWriter.color('white')

# Turtle for Wrong Letters
tWrong = Turtle()
tWrong.hideturtle()
tWrong.color('white')

def chooseSecretWord():
    global secretWord
    secretWord = wordList[randint(0, len(wordList)-1)]
    print('The secret word is ' + secretWord)

def displayText(newText):
    tWriter.clear()
    tWriter.penup()
    tWriter.goto(-int(3 * sw/8), -int(sl/4))
    tWriter.write(newText, font = ("Comic Sans MS", fontSize, "bold"))

def displayWrongLetters(newText):
    tWrong.clear()
    tWrong.penup()
    tWrong.goto(int(sw/128), int(3 * sl/16))
    tWrong.write(newText, font = ("Comic Sans MS", fontSize, "bold"))

def makeWordString():
    global displayWord, alpha
    displayWord = ""
    # assume we have a secret word
    for i in secretWord:
        if str(i).lower() in alpha:
            if str(i).lower() in letterCorrect.lower():
                displayWord += str(i) + " "
            else:
                displayWord += "_" + "  "
        else:
            displayWord += str(i) + "  "

def updateHangman():
    global fails, gameDone
    if fails == 8:
        drawCircle()
    if fails == 7:
        drawBody()
    if fails == 6:
        drawLeftArm()
    if fails == 5:
        drawRightArm()
    if fails == 4:
        drawLeftLeg()
    if fails == 3:
        drawRightLeg()
    if fails == 2:
        drawLeftEye()
    if fails == 1:
        drawRightEye()
    if fails == 0:
        drawMouth()
        time.sleep(1)
        displayWord = "Sorry..."
        tWriter.color('yellow')
        displayText("The secretword should be " + secretWord)
        time.sleep(2)
        tWriter.clear()
        tWriter.penup()
        tWriter.goto(-int(5 * sw/16), -int(sl/4))
        tWriter.write("GAME OVER ---", font = ("Comic Sans MS", 80, "bold"))
        time.sleep(2)
        gameDone = True
                    
def getGuess():
    boxTitle = "Letters Used: " + letterWrong
    guess = s.textinput(boxTitle, "Enter a LETTER to take a guess!!\
 Enter $$ to guess a word ~")
    return guess

def checkWordGuess():
    global fails, gamedone
    boxTitle = "Word Guess"
    guess = s.textinput(boxTitle, "Ready to guess the WORD!? \
[P.S. A wrong word guess loses two chances...]")
    if guess == secretWord:
        tWriter.clear()
        tWriter.color('yellow')
        tWriter.penup()
        tWriter.goto(-int(7 * sw/16), -int(sl/4))
        tWriter.write("OMG YOU DID IT !!! Congrats!!", \
                      font = ("Comic Sans MS", 60, "bold"))
    else:
        displayText("Nope... It is not " + guess)
        time.sleep(10)
        displayText(displayWord)
        fails -= 1
        updateHangman()
        fails -= 1
        updateHangman()

def restartGame():
    global fails, letterCorrect, letterWrong, displayWord, gameDone
    boxTitle = "Want to play again?"
    guess = s.textinput(boxTitle, "Type 'Y' or 'Yes' to play again!")
    if guess.lower() == 'y' or guess.lower() == 'yes':
        letterCorrect = ""
        letterWrong = ""
        displayWord = ""
        tWriter.color("white")
        time.sleep(1) # wait for 1 seconds
        t.clear()
        drawGallows()
        chooseSecretWord()
        time.sleep(1)
        displayText("Guess a Letter ~")
        time.sleep(1)
        makeWordString()
        displayText(displayWord)
        time.sleep(1)
        displayWrongLetters("Ooops: " + letterWrong)
        fails = 9
        gameDone = False
    else:
        displayWrongLetters("Thanks for playing! Cya ~")
        

def playGame():
    global gameDone, fails, alpha, letterCorrect, letterWrong
    while gameDone == False and fails > 0:
        # get input
        theGuess = str(getGuess())
        # to get out of the loop
        #gameDone = True
        if theGuess == '$$':
            checkWordGuess()
        elif len(theGuess) > 1 or theGuess == "":
            displayText("Sorry, one letter only please ~")
            time.sleep(2)
            displayText(displayWord)
        elif theGuess not in alpha:
            displayText(theGuess + "is not a letter. Give another try ~")
            time.sleep(2)
            displayText(displayWord)
        elif theGuess.lower() in secretWord.lower():
            #see if the letter is in the word
            letterCorrect += theGuess.lower()
            makeWordString()
            displayText(displayWord)
        else: 
            if theGuess.lower() not in letterWrong:
                letterWrong += theGuess.lower() + ", "
                fails -= 1
                displayText(theGuess + " is not in the word")
                time.sleep(1)
                updateHangman()
                displayText(displayWord)
                displayWrongLetters("Ooops: " + letterWrong)
            else:
                displayText(theGuess + " has been guessed already")
                time.sleep(1)
                displayText(displayWord)
        if str("_") not in displayWord:
            time.sleep(2)
            tWriter.clear()
            tWriter.color('yellow')
            tWriter.penup()
            tWriter.goto(-int(7 * sw/16), -int(sl/4))
            tWriter.write("OMG YOU DID IT !!! Congrats!!", \
                    font = ("Comic Sans MS", 60, "bold"))
            gameDone = True
        if gameDone == True:
            restartGame()
        
                
def drawGallows():
    # draw base
    t.width(5)
    t.penup()
    t.setheading(0)
    t.goto(-int(3 * sw/8), -int(sl/8))
    t.pendown()
    t.forward(int(3 * sw/8))

    # draw main pole
    t.penup()
    t.goto(-int(sw/4), -int(sl/8))
    t.pendown()
    t.left(90)
    t.forward(int(3 * sl/8))

    # draw top pole
    t.right(90)
    t.forward(int(sw/8))

    # draw short pole
    t.right(90)
    t.forward(int(sl/32))

def drawCircle():
    t.penup()
    t.goto(-int(21 * sw/128), int(23 * sl/128))
    t.pendown()
    t.circle(5 * sw/128)

def drawBody():
    t.penup()
    t.goto(-int(sw/8), int(9 * sl/64))
    t.pendown()
    t.forward(7 * sl/64)

def drawLeftArm():
    t.penup()
    t.goto(-int(sw/8), int(11 * sl/128))
    t.pendown()
    t.right(120)
    t.forward(int(sw/16))

def drawRightArm():
    t.penup()
    t.goto(-int(sw/8), int(11 * sl/128))
    t.pendown()
    t.right(120)
    t.forward(int(sw/16))

def drawLeftLeg():
    t.penup()
    t.goto(-int(sw/8), int(sl/32))
    t.pendown()
    t.right(170)
    t.forward(int(3 * sw/32))

def drawRightLeg():
    t.penup()
    t.goto(-int(sw/8), int(sl/32))
    t.pendown()
    t.left(100)
    t.forward(int(3 * sw/32))

def drawLeftEye():
    t.penup()
    t,setheading(90)
    t.goto(-int(9 * sw/64), int(3 * sl/16))
    t.pendown()
    t.forward(int(5 * sw/512))

def drawRightEye():
    t.penup()
    t.setheading(90)
    t.goto(-int(7 * sw/64), int(3 * sl/16))
    t.pendown()
    t.forward(int(5 * sw/512))

def drawMouth():
    t.penup()
    t.setheading(0)
    t.goto(-int(35 * sw/256), int(5 * sl/32))
    t.pendown()
    t.forward(int(7 *sw/256))
    
#game starts here
makeWordString()
drawGallows()
drawCircle()
drawBody()
drawLeftArm()
drawRightArm()
drawLeftLeg()
drawRightLeg()
drawLeftEye()
drawRightEye()
drawMouth()

#actual game setup
time.sleep(1) # wait for 1 seconds
t.clear()
drawGallows()
chooseSecretWord()
time.sleep(1)
displayText("Guess a Letter ~")
time.sleep(1)
makeWordString()
displayText(displayWord)
time.sleep(1)
displayWrongLetters("Ooops: " + letterWrong)
playGame()


