import random
playing = False
stand1=True

chip_pool = 100
bet = 1
restart_phrase = "Press 'd' to deal the cards again, or press 'q' to quit"

su = ('H', 'D', 'C', 'S')

r = ('A', '2', '3', '4','5', '6', '7', '8', '9', '10', 'J', 'K')

card_val = { 'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10 }

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def draw(self):
        print(self.suit + self.rank)


#Hand Class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        hand_comp = ""

        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name

        return 'The hand has %s' %hand_comp

    def card_add(self, card):

        self.cards.append(card)


        if card.rank == 'A':
            self.ace = True
        self.value = self.value+card_val[card.rank]

    def calc_val(self):

        if (self.ace == True and self.value < 12):
            return self.value + 10
        return self.value

    def draw(self, hidden):
        if hidden == True and playing == True:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()

class Deck:
    def __init__(self):

        self.deck = []
        for suit in su:
            for rank in r:
                self.deck.append(Card(suit, rank))

    def shuffle(self):

        random.shuffle(self.deck)

    def deal(self):

        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ""
        for card in self.cards:
            deck_comp += " " + deck_comp.__str__()

        return "The deck has" + deck_comp


class BlackJack:
    def make_bet(self):


        global bet
        bet = 0

        print( ' What amount of chips would you like to bet? (Enter whole integer please) ')
        while bet == 0:
            bet_comp = input()
            bet_comp = int(bet_comp)
            if bet_comp >= 1 and bet_comp <= chip_pool:
                bet = bet_comp
            else:
                print("Invalid bet, you only have " + str(chip_pool) + " remaining")

    def deal_cards(self):

        global result,playing,deck,player_hand,dealer_hand,chip_pool,bet
        deck = Deck()
        deck.shuffle()
        self.make_bet()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.card_add(deck.deal())
        player_hand.card_add(deck.deal())

        dealer_hand.card_add(deck.deal())
        dealer_hand.card_add(deck.deal())

        result = "Hit or Stand? Press either h or s: "

        if playing == True:
            print('Fold, Sorry')
            chip_pool -= bet
        playing = True
        self.game_step()

    def hit(self):

        global playing,chip_pool,deck,player_hand,dealer_hand,result,bet
        if playing:
            if player_hand.calc_val() <= 21:
                player_hand.card_add(deck.deal())

            print("Player hand is %s" %player_hand)

            if player_hand.calc_val() > 21:
                result = "Busted! " + restart_phrase

                chip_pool -= bet
                playing = False

            self.game_step()

    def stand(self):
        global playing,chip_pool,deck,player_hand,dealer_hand,result,bet,stand1
        '''This function will now play the dealers hand, since stand was chosen'''

        if playing == False:
            if player_hand.calc_val() > 0:
                result = "Sorry, you can't stand!"


        else:

            stand1=False
            if (dealer_hand.calc_val() < 17):
                dealer_hand.card_add(deck.deal())
                result = "dealer takes a card"
                print("17 rule dealer takes the card")
                self.stand()

            else:

                if dealer_hand.calc_val() > 21:
                    result = 'Dealer busts! You win!' + restart_phrase
                    chip_pool += bet
                    playing = False

                elif dealer_hand.calc_val() < player_hand.calc_val():
                    result = 'You beat the dealer, you win!' + restart_phrase
                    chip_pool += bet
                    playing = False

                elif dealer_hand.calc_val() == player_hand.calc_val():
                    result = 'Tied up, push!' + restart_phrase
                    playing = False

                else:
                    result = 'Dealer Wins!' + restart_phrase
                    chip_pool -= bet
                    playing = False
        self.game_step()


    def game_step(self):

        print ('')
        print('Player Hand is: '),
        player_hand.draw(hidden = False)

        print('Player hand total is: ' + str(player_hand.calc_val()))
        print('The Dealer Hand is: '), dealer_hand.draw(hidden = stand1)


        if playing == False:
            print("--- for a total of " + str(dealer_hand.calc_val()))
            print ("Chip Total: " + str(chip_pool))

        else:
            print ("with another card hidden upside dowm")

        print (result)

        self.player_input()


    def game_exit(self):
        print( "Thanks for playing!")
        exit()

    def player_input(self):

        plin = input().lower()

        if plin == 'h':
            self.hit()
        elif plin == 's':
            self.stand()
        elif plin == 'd':
            stand1=True
            self.deal_cards()
        elif plin == 'q':
            self.game_exit()
        else:
            print( "Invalid Input...Enter h,s,d, or q: ")
            self.player_input()




blackJack=BlackJack()

deck = Deck()
deck.shuffle()

player_hand = Hand()
dealer_hand = Hand()
blackJack.deal_cards()
