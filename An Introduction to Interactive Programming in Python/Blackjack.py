# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or Stand?"
res_word = ''
score = 0
count = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_of_cards = list()
        

    def __str__(self):
        ans = "Hand contains"
        for i in range(len(self.hand_of_cards)):
            ans += ' '
            ans += str(self.hand_of_cards[i])
        return ans
        
        # return a string representation of a hand

    def add_card(self, card):
        return self.hand_of_cards.append(card) 
        # add a card object to a hand

    def get_value(self):
        score = 0
        ind_A = 0
        for card in self.hand_of_cards:
            score += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                ind_A += 1
        if score + 10 <= 21 and ind_A > 0:
            score = score + 10
        return score
        
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for card in self.hand_of_cards:
            card.draw(canvas, pos)
            pos[0] += 80
        # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck_of_cards = list()
        for suit in SUITS:
            for rank in RANKS:
                cards = Card(suit, rank)
                self.deck_of_cards.append(cards)
        # create a Deck object

    def shuffle(self):
        return random.shuffle(self.deck_of_cards)
        # shuffle the deck 
        
    def deal_card(self):
        i = random.choice(range(len(self.deck_of_cards)))
        return self.deck_of_cards.pop(i)
        # deal a card object from the deck
    
    def __str__(self):
        ans = 'Deck contains'
        for cards in self.deck_of_cards:
            ans += ' '
            ans += str(cards)
        return ans


#define event handlers for buttons
def deal():
    global outcome, in_play, play_deck, hand_deal, hand_player, score
    
    # your code goes here
    play_deck = Deck()
    hand_deal = Hand()
    hand_player = Hand()
    play_deck.shuffle()
    hand_deal.add_card(play_deck.deal_card())
    hand_player.add_card(play_deck.deal_card())
    hand_deal.add_card(play_deck.deal_card())
    hand_player.add_card(play_deck.deal_card())
    
    outcome = 'Hit or Stand?'
    
    if hand_player.get_value() == 21:
        outcome = 'Player wins'
        score += 1
        in_play = False
    
    if in_play:
        outcome = 'You lose. New deal?'
        score -= 1
        in_play = False
        
    in_play = True


def hit():
    # replace with your code below
    global in_play, play_deck, hand_player, outcome, score
    # if the hand is in play, hit the player
    if in_play == True and hand_player.get_value() < 21:
        hand_player.add_card(play_deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
    if hand_player.get_value() > 21:
        #print "You have busted"
        outcome = 'You have busted. New deal?'
        score -= 1
        in_play = False
    elif hand_player.get_value() == 21:
        outcome = 'Player wins'
        score += 1
        in_play = False
        
def stand():
    global in_play, play_deck, hand_deal, hand_player, outcome, score
    # replace with your code below
    if in_play == True and hand_player.get_value() > 21:
        #print "You have busted"
        outcome = 'You have busted. New deal?'
        in_play = False
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    else:
        while hand_deal.get_value() <= 17:
            hand_deal.add_card(play_deck.deal_card())
            
    # assign a message to outcome, update in_play and score
    
    if hand_deal.get_value() > 21:
        outcome = "Player wins. New Deal?"
        score += 1
        in_play = False
        
    elif hand_deal.get_value() >= hand_player.get_value():
        outcome = 'Dealer wins. New deal?'
        score -= 1
        in_play = False
        
    else:
        outcome = 'Player wins. New deal?'
        score += 1
        in_play = False
        
    
# draw handler    
def draw(canvas):
    global hand_deal, hand_player, outcome, res_word
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('BlackJack', (20, 50), 65, 'Black')
    canvas.draw_text('Score: ' + str(score), (400, 60), 30, 'red')
    canvas.draw_text('Dealer', (20, 150), 50, 'grey')
    canvas.draw_text('Player', (20, 350), 50, 'grey')
    canvas.draw_text(outcome, (210, 150), 30, 'blue')
    
    hand_deal.draw(canvas, [50, 180])
    hand_player.draw(canvas, [50, 380])
    
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50 + CARD_BACK_CENTER[0], 180 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric