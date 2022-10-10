from random import randint

cardNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
bal = [500]

def main():

    '''Prompts the user to enter a wager and then intializes the program'''

    if bal[0] == 0:
        print("You're out of money! You should work on your skills. L.")
        exit()
    print("Your current balance is: $" + str(bal[0]))
    print("How much would you like to wager? Enter 0 if you'd like to quit.")
    global wager
    global hand
    global dealerHand
    dealerHand = [0,0]
    hand = [0, 0]
    wager = int(input())
    if wager > bal[0]:
        print("Wager is greater than balance! You can't do that!")
        print("----------------------------------------------------------------------")
        main()
    elif wager == 0:
        print("----------------------------------------------------------------------")
        exit()
    elif wager == bal[0]:
        print("----------------------------------------------------------------------")
        print("FULL SEND ALERT!")
        print("----------------------------------------------------------------------")
        getHand()
    else:
        print("----------------------------------------------------------------------")
        getHand()

    
def getCard(): 

    '''Gets a unique card'''

    card = (cardNumbers[randint(0, 11)], suits[randint(0,3)])
    for i in hand:
        while i == card:
            card = (cardNumbers[randint(0, 11)], suits[randint(0,3)])
    for j in dealerHand:
        while j == card:
            card = (cardNumbers[randint(0, 11)], suits[randint(0,3)])
    return card

def getHand():

    '''Initializes the user's hand.'''

    hand[0] = getCard()
    hand[1] = getCard()
    dealerHand[0] = getCard()
    print("The Dealer's first card is the " + str(dealerHand[0][0]) + " of " + str(dealerHand[0][1]) + '.')
    print("Your first card is the " + str(hand[0][0]) + " of " + str(hand[0][1]) + '.')
    print("Your second card is the " + str(hand[1][0]) + " of " + str(hand[1][1]) + '.')
    if getValue(hand)[0] == getValue(hand)[-1]:
        print("Your current value is: " + str(getValue(hand)[0]))
    else:
        print("Your current possible values are: " + str(getValue(hand)))
    task()

def task():

    '''Task's the user with either hitting or standing'''

    print("----------------------------------------------------------------------")
    print("Please enter 'hit' to draw another card, or 'stand' to stay where you are at.")
    choice = input()
    print("----------------------------------------------------------------------")
    if choice == 'hit':
        hit()
    elif choice == 'stand':
        checkDealer()
        over()
    else:
        print("Invalid selection, please try again.")
        task()

def getValue(hand):
    
    '''Gets the value of the given hand'''

    values = [0,0]
    for i in hand:
        if i[0] == 'J' or i[0] == 'Q' or i[0] == 'K':
            values[0] += 10
            values[1] += 10
        elif i[0] == 'A':
            values[0] += 1
            values.insert(1, values[0] + 10)
        else:
            values[0] += int(i[0])
            values[1] += int(i[0])
    end = [values[0], values[1]]

    if values[1] > 21:
        end.remove(values[1])
    return(end)

def hit():

    '''Draws a new card and adds it to the current hand'''

    newCard = getCard()
    hand.append(newCard)
    print("You chose to hit! Your new card is the " + str(newCard[0]) + " of " + str(newCard[1]) + '.')
    if getValue(hand)[0] == getValue(hand)[-1]:
        print("Your current value is: " + str(getValue(hand)[0]))
    else:
        print("Your current possible values are: " + str(getValue(hand)))
    if getValue(hand)[0] > 21:
        over()
    task()

def checkDealer():

    '''Initializes the dealer, as well as makes all of the dealer's moves'''
    
    dealerHand[1] = getCard()
    for i, j in dealerHand:
        while i == j:
            j = getCard()
    print("The Dealer's second card is the " + str(dealerHand[1][0]) + " of " + str(dealerHand[1][1]) + '.')

    if getValue(dealerHand)[0] == getValue(dealerHand)[-1]:
        print("The Dealer's current value is: " + str(getValue(dealerHand)[0]))
    else:
        print("The Dealer's possible values are: " + str(getValue(dealerHand)))
    print("----------------------------------------------------------------------")
    while getValue(hand)[-1] >= getValue(dealerHand)[-1]:
        if getValue(hand)[-1] == getValue(dealerHand)[-1] and getValue(dealerHand)[-1] >= 17:
            break
        newCard = getCard()
        dealerHand.append(newCard)
        print("The Dealer chose to hit! Their new card is the " + str(newCard[0]) + " of " + str(newCard[1]) + '.')
        if getValue(dealerHand)[0] == getValue(dealerHand)[-1]:
            print("The Dealer's current value is: " + str(getValue(dealerHand)[0]))
        else:
            print("The Dealer's possible values are: " + str(getValue(dealerHand)))
        if getValue(dealerHand)[-1] == 21:
            break
        print("----------------------------------------------------------------------")
    while getValue(dealerHand)[-1] <= 16:
        newCard = getCard()
        dealerHand.append(newCard)
        print("The Dealer has to hit! Their new card is the " + str(newCard[0]) + " of " + str(newCard[1]) + '.')
        if getValue(dealerHand)[0] == getValue(dealerHand)[-1]:
            print("The Dealer's current value is: " + str(getValue(dealerHand)[0]))
        else:
            print("The Dealer's possible values are: " + str(getValue(dealerHand)))
    over()

def over():
    if getValue(hand)[-1] > 21:
        bal[0] = bal[0] - wager
        print("You busted! You lose!")
    elif getValue(dealerHand)[-1] > 21:
        bal[0] = bal[0] + wager
        print("The Dealer busted! You win!")
    elif getValue(dealerHand)[-1] > getValue(hand)[-1]:
        bal[0] = bal[0] - wager
        print("You lose!")
    elif getValue(dealerHand)[-1] == getValue(hand)[-1]:
        print("Draw!")
    print("----------------------------------------------------------------------")
    main()

if __name__ == "__main__":
    main()