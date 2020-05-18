# Creating a Class for Cards
class Card:
    '''Creating a Class for Cards'''

    def __init__(self, card, colour=0, suit=0, value=0):
        self.card = card
        self.colour = colour
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.card} {self.colour} of {self.suit}"


# Creating the balance account of the Player which contains the betting function.
class Balance:
    '''Creating the balance account of the Player which contains the betting function. the
    collect method used to collect money after a win or a tie'''

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(
            '\n\n#################################\n\nHello %s,\n\nYour starting balance is: '
            '$%s\n\nPlease spend it wisely\n\n#################################\n\n' % (
                self.name, self.balance))

    def __str__(self):
        return f"\nYour remaining balance is: {self.balance}"

    def bet(self):
        while True:
            global bettingamount
            try:
                bettingamount = int(input("Please enter betting amount and press Enter:"))
            except:
                print('Please enter a valid integer')
            else:
                if bettingamount > self.balance or bettingamount <= 0:
                    print(
                        '\nNo Funds; or Amount Entered <= 0\n\nPlease place a positive bet up to '
                        '$%s\n\n' % self.balance)
                else:
                    break
        self.balance -= bettingamount

    def collect(self, amount):
        self.balance = self.balance + amount
        print('You have collected $ %s\nYour Current Balance: $%s' % (amount, self.balance))


# Creating the Deck:

def createdeck():
    '''This function used to to the deck'''
    card_dic = {'Ace': [1, 11], 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
                'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
    cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
             'Queen', 'King']
    Values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    colours = ['Red', 'Black']
    for i, x in enumerate(cards):
        deck.append(
            Card(card=cards[i], colour=colours[0], suit=suits[1], value=card_dic.get(cards[i])))
        deck.append(
            Card(card=cards[i], colour=colours[0], suit=suits[2], value=card_dic.get(cards[i])))
        deck.append(
            Card(card=cards[i], colour=colours[1], suit=suits[0], value=card_dic.get(cards[i])))
        deck.append(
            Card(card=cards[i], colour=colours[0], suit=suits[3], value=card_dic.get(cards[i])))

    # Now deck is a list containing 52 cards with there different attributes


# Shuffles the deck:
def shuffle():
    '''This function shuffles the deck'''
    import random
    random.shuffle(deck)


# Dealing cards
def deal(deck_name, n):
    ''' This function deals to player "name" - "n"  card(s),
    by assigning cards from deck to the applicable list of
    cards; delaer_cards or player_cards
    '''
    count = 0
    while count < n:
        deck_name.append(deck.pop())
        count += 1


# Prints the balance
def pbalance():
    # Prints Balance Table
    from texttable import Texttable
    bal = Texttable()
    bal.add_rows([['Balance', 'Bet Amount', 'Pot']])
    bal.add_row([balance.balance, bettingamount, (2 * bettingamount)])
    print('+-----------Balance----------+')
    print(bal.draw())
    print('\n')


# Prints current values
def printval():
    '''Prints current value'''
    from texttable import Texttable
    val = Texttable()
    val.add_rows([['%s' % playersname, 'Dealer']])
    val.add_row([check_val((player_cards)), check_val(dealer_cards)])
    print('+-----Values-----+')
    print(val.draw())
    print('\n')


# Prints the board
def pboard(Title=''):
    print('\n' * 300)
    from texttable import Texttable
    ##Player's Table
    a = Texttable()
    a.add_rows([['Card', 'Suit', 'Colour', 'Value']])
    for i, x in enumerate(player_cards):
        a.add_row([player_cards[i].card, player_cards[i].suit, player_cards[i].colour,
                   player_cards[i].value])

    # Dealers Table
    b = Texttable()
    b.add_rows([['Card', 'Suit', 'Colour', 'Value']])
    if turn == 'player':
        b.add_row(['Covered', 'Covered', 'Covered', 'Covered'])
        for i, x in enumerate(dealer_cards[1:]):
            b.add_row([dealer_cards[i].card, dealer_cards[i].suit, dealer_cards[i].colour,
                       dealer_cards[i].value])
    else:
        for i, x in enumerate(dealer_cards):
            b.add_row([dealer_cards[i].card, dealer_cards[i].suit, dealer_cards[i].colour,
                       dealer_cards[i].value])

    pbalance()
    print('...............%s................' % playersname)
    print(a.draw())
    print('\n')
    print('................Dealer.................')
    print(b.draw())
    print('\n')


# checks the value of deck
def check_val(player_or_dealer_cards):
    aces = 0
    acesval = 0
    sumc = 0
    for card in player_or_dealer_cards:
        if card.card == 'Ace':
            aces += 1
    if aces == 0:
        for card in player_or_dealer_cards:
            sumc += card.value
    else:
        for card in player_or_dealer_cards:
            if card.card != 'Ace':
                sumc += card.value
        if sumc > 21:
            pass
        else:
            acesval = aces * 11
            while acesval > aces and acesval + sumc > 21:
                acesval -= 10
            sumc += acesval
    return sumc


# Asks the player for his next move
def hitorstand():
    global turn, choose
    choose = 0
    while choose != 1 or choose != 2:
        try:
            choose = int(input('HIT - Enter 1;\nSTAND - Enter 2\nEnter here:'))
        except:
            continue
        finally:
            if choose == 1 or choose == 2:
                break
    if choose == 1:
        turn = 'player'
    else:
        turn = 'dealer'


####  Starting The Game ####

finish_game = False

while finish_game == False:
    print(
        '##################################################\n                    '
        'HELLO!\n\nWELCOME TO THE BEST BlackJack GAME EVER '
        'CREATED!!!\n\n##################################################\n')
    playersname = input('Please enter your name and press enter:')
    print('\n' * 40)
    game_on = True
    # Creating the balance
    balance = Balance(playersname, 1000)

    while game_on == True and finish_game == False:
        bettingamount = 0
        deck = []
        dealer_cards = []
        player_cards = []
        createdeck()
        shuffle()
        pbalance()
        balance.bet()
        turn = 'player'
        # dealing and resenting the "Board":
        deal(player_cards, 2)
        deal(dealer_cards, 2)
        pboard('Here is the starting board:')

        #####Players Turn - Hit or Stand until player chooses to stand, or until he goes bust###

        while turn == 'player' and check_val(player_cards) < 21:
            hitorstand()
            if choose == 1:
                deal(player_cards, 1)
            pboard('Here is the current board:')

        # If players bust, the following code lets him know and ask him if he wishes to play
        # again (if he has the funds)
        if check_val(player_cards) > 21:
            printval()
            print('\n%s, You are BUST :(\n\nThe value of your deck is %s which  is over 21 :(\n' % (
            playersname, check_val(player_cards)))
            if balance.balance > 0:
                print('Your remaining balance is: $%s' % balance.balance)
                while True:
                    keepplaying = input('\nwould you like to keep playing? (enter Yes/No:)')
                    if keepplaying.upper() == 'YES':
                        break
                    elif keepplaying.upper() == 'NO':
                        game_on = False
                        finish_game = True
                        break
                    else:
                        pass
            else:
                while True:
                    keepplaying = input(
                        '%s, you have lost all of your funds and therefore, lost the Game, '
                        'would you like to play again? (Yes/No)' % playersname)
                    if keepplaying.upper() == 'YES':
                        game_on = False
                        break
                    elif keepplaying.upper() == 'NO':
                        game_on = False
                        finish_game = True
                        break
                    else:
                        pass

        else:
            # Notifies the player he reached 21
            if check_val(player_cards) == 21:
                turn = 'dealer'
                input("Nice - you have hit 21!!,\nNow, please press Enter and let  the dealer  do "
                      "his thing")

            # Dealers move (hits until reaches 17)
            while check_val(dealer_cards) < 17:
                print('\n' * 300)
                deal(dealer_cards, 1)
                pboard('The dealer chose to hit, here is the new board:')
                if check_val(dealer_cards) < 17:
                    input("press Enter to watch dealer's next move")

            # Checking the Winner after Dealer's turn
            printval()
            if check_val(player_cards) > check_val(dealer_cards) or check_val(dealer_cards) > 21:
                print('%s, You won this round!' % playersname)
                balance.collect(2 * bettingamount)
                while True:
                    keepplaying = input('would you like to keep playing? (enter Yes/No:)')
                    if keepplaying.upper() == 'YES':
                        break
                    elif keepplaying.upper() == 'NO':
                        game_on = False
                        finish_game = True
                        break
                    else:
                        pass
            elif check_val(player_cards) == check_val(dealer_cards):
                print('This is a Tie!')
                balance.collect(bettingamount)
                print('You have collected $%s back to your balance' % bettingamount)
                print('Your remaining balance is: %Ss' % balance.balance)
                while True:
                    keepplaying = input('would you like to keep playing? (enter Yes/No:)')
                    if keepplaying.upper() == 'YES':
                        break
                    elif keepplaying.upper() == 'NO':
                        game_on = False
                        finish_game = True
                        break
                    else:
                        pass
            elif balance.balance == 0:
                while True:
                    keepplaying = input(
                        '%s, you have lost all of your funds and therefore, lost the Game, '
                        'would you like to play again? (Yes/No)' % playersname)
                    if keepplaying.upper() == 'YES':
                        game_on = False
                        break
                    elif keepplaying.upper() == 'NO':
                        game_on = False
                        finish_game = True
                        break
                    else:
                        pass
            else:
                while True:
                    print('%s, You have lost this round:(\n' % playersname)
                    print('You have lost $ %s\nYou remaining balance: $%s' % (
                    bettingamount, balance.balance))
                    keepplaying = input('would you like to keep playing? (enter Yes/No:)')
                    if keepplaying.upper() == 'YES':
                        break
                    elif keepplaying.upper() == 'NO':
                        game_on = False
                        finish_game = True
                        break
                    else:
                        pass

quit()
