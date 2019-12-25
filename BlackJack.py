import time
import random

def drawCard(arr: list) -> str:
    # function to draw a card, input is list of all the cards, returns string
    
    index = randomInt(arr)
    returnString = arr.pop(index)
    return returnString
    
def randomInt(arr: list) -> int:
    # function that uses random module to randomly get a card in the list
    return random.randrange(0,len(arr))

def getValue(arr: list) -> int:
    # function that gets the value of a cards that have been drawn, intput is 
    # list of cards drawn returns int value of cards drawn
    
    aplhaVlaue = {"A" : 11, "Q" : 10, "K" : 10, "J" : 10}
    value = 0
    for card in arr:   #loops through cards that have been drawn
        card = str(card)
        if (card.isdigit()):
            value += int(card)
        else:
            value += aplhaVlaue.get(card)
    
    if (value > 21 and ("A" in arr)):
        # This is for if the value is above a 21 but you have Ace(s) because an
        # Ace can equal 11 or 1
        for i in range(arr.count("A")):
            if value > 21:
                value -= 10
    return value

def nextMove() -> str:
    # function returns whether the user wants to hit or hold
    
    print("\nWhat do you want to do next?")
    move = input("You can Hit or Hold: ")
    
    while(move.lower() != "hit" and move.lower() != "hold"):
        print("Sorry I did not get that. You have 2 options: Hit or Hold ")
        move = input("You can Hit or Hold: ")
        print()
    
    return move

def compareScore(player: list, comp: list) -> int:
    # function to compare the score between User and computer, inputs are drawn
    # hands from user and computer, returns 1 if user won else 0, no ties
    
    playScore = getValue(player)
    compScore = getValue(comp)
    
    if (playScore > compScore and playScore <= 21):
        print ("Congrats you won!!!")
        return 1
    else:
        print("The computer won this round :(")
        return 0

def doContinue() -> bool:
    # function to know if user wants to continue playing, returns boolean true
    # if they want to continue false if not
    
    cont = input("Do you want to continue? [Yes/No] ")
    while( cont.lower() != "yes" and cont.lower() != "no" ):
        print("You have to choose Yes or No.\n")
        cont = input("Do you want to continue? [Yes/No] ")
    
    if(cont.lower() == "yes"):
        return True
    
    return False
    
    
if __name__== "__main__":
    print("="*46)
    print("= Welcome to a simple Blackjack console game =")
    print("=                                            =")
    print("=   First you will be asked how many decks   =") 
    print("=     you want to combine into one deck.     =")
    print("=                                            =")
    print("=  This is to make counting cards easier or  =")
    print("=            harder for yourself.            =")
    print("=                                            =")
    print("=   When the game begins the computer will   =")
    print("=        always draw its cards first.        =")
    print("=                                            =")
    print("=       Then you draw your cards next.       =")
    print("=                                            =")
    print("=  The goal is to have a total higher than   =")
    print("=    the computer but not higher that 21.    =")
    print("=                                            =")
    print("= All ties will count towards the computer.  =")
    print("=                                            =")
    print("=          Good luck and have fun!!          =")
    print("=" * 46)
    print()

    validNumber = False
    while(not validNumber):
        countDeck = input("How many decks will be combined? ")
        while(not countDeck.isdigit()):
            print("\nPlease input a digit")
            countDeck = input("How many decks will be combined? ")
        countDeck = int(countDeck)
        if (1 > countDeck  or countDeck > 10):
            print("\nThe number of decks combined must be between 1-10(inclusive)")
            print("Please re-enter the number of decks that will be combined")
        else:
            validNumber = True

    currentDeck = []
    # this is the list that will have all the cards in it, when a card get
    # drawn it will be pop from this list
    cardTypes = ("A", "Q", "K", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")
    for i in cardTypes:
        # for loop will populate currentDeck 
        for j in range(countDeck * 4):
            currentDeck.append(i)
    
    willContinue = True
    totalScore = 0
    
    while(willContinue and len(currentDeck) >= 4):
        
        print("\nThe computer is drawing 2 cards.")
        time.sleep(1.5)
        comp_firstCard = drawCard(currentDeck)
        comp_secondCard = drawCard(currentDeck)
        compList = [comp_firstCard, comp_secondCard]
        print("\nThe computer got a " + comp_firstCard + " and a " + 
              comp_secondCard)
        if (getValue(compList) <= 11 and len(currentDeck) >= 3):
            # if the value is <= 11 that means the computer can hit without 
            # risking going over 21
                compHit = drawCard(currentDeck)
                print("The computer wanted to take a hit and got a " + 
                      str(compHit))
                compList.append(compHit)
        print("That means you have to beat: " + str(getValue(compList)))
        
        print("\nNow it is your turn!")
        time.sleep(2.5)
        play_firstCard = drawCard(currentDeck)
        play_secondCard = drawCard(currentDeck)
        playList = [play_firstCard, play_secondCard]
        print("\nYou got a " + play_firstCard + " and a " + play_secondCard)
        print("That means you have : " + str(getValue(playList)))
        
        if(len(currentDeck) >= 1):
            # ther has to be at least one card in the deck in order to hit
            playMove = nextMove()
            while (playMove.lower() != "hold" and len(currentDeck) >= 1):
                hit = drawCard(currentDeck)
                print("\nYou wanted to hit and you got a: " + str(hit))
                playList.append(hit)
                print("That means your total is now: " + str(getValue(playList))
                + " because you have " + str(playList))
                
                if(getValue(playList) > 21):
                    print("Oh no you went over 21!")
                    break
                playMove = nextMove()
        
        if(len(currentDeck) == 0):
            print("\nRan out of cards")
        time.sleep(1)
        
        print("\nThe computer had " + str(getValue(compList)) + " while you had " +
              str(getValue(playList)))
        totalScore += compareScore(playList,compList)
        print("\nYour Game Score is: " + str(totalScore))
        print("The number of cards in the deck is now: " + str(len(currentDeck)))
        print()
        willContinue = doContinue()

    if(len(currentDeck) < 4):
        print("\nOh no! There is not enough cards to continue.")
    
    print("\nThank you for playing. You got a score of " + str(totalScore))
    print("This progarm will shutdown soon")
    time.sleep(10)
    exit()
