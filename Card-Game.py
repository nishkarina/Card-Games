import random

# constants in cards
SUITE_TUPLE = ('Spade','Ace','Diamond','Clubs')
RANK_TUPLE = ('Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King')
NCARDS = 8

# to get a card from a list
def getcard(dekcListIn):
    deckListOut = dekcListIn.pop()
    return deckListOut

def shuffle(dekcListIn):
    deckListOut = dekcListIn.copy()  # making a copy of Original List
    random.shuffle(deckListOut) # shuffle elements in list
    return deckListOut


# Main Code
print("Welcome to Higher or Lower Game")
print('You have to choose whether the next card is higher or lower than current card')
print('Getting it right will give 20 points and wrong will lose 15 points.')
print('At starting you have 50 points to start.')
print()

startingDeckList = []
for suit in SUITE_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank ,'suit': suit,'value' : thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getcard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is:' +currentCardRank+' of '+currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):
        answer = input('Will the next card value will be higher or lower than '+ currentCardRank +' of '+ currentCardSuit +' ? (enter h or l:) and e for exit: ')
        answer = answer.casefold()
        if answer =='e':
            break
        nextCardDict = shuffle(startingDeckList)
        nextCardDict = getcard(startingDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print("You got it right!, it's higher")
                score = score + 20
            else:
                print("You lost it!, it was not lower")
                score = score - 15
        if answer == 'l':
            if nextCardValue < currentCardValue:
                print("You got it right!, it's higher")
                score = score + 20
            else:
                print("You lost it!, it was not lower")
                score = score - 15
        print('your score is: ',score)
        print()
        # to update current card rank and value after final score show
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
    goAgain = input("To play again press ENTER, else q for quit: ")
    if goAgain == 'q':
        break
    print('Bye')
            