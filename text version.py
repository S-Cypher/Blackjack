#Blackjack text version
import random

'''
Player and dealer are dealt two cards each
Dealer has one card face-up and the other one faced down
Hit: draw an additional card to increase the hand value
Stand: keep the current hand and end the turn

After all players have completed their turns, the dealer reveals the hole card
The dealer must hit until their hand totals 17 or higher
If the dealer busts (exceeds 21), players who haven't busted win

Compare the two hand values
Players win if their hand is closer to 21 than the dealer's hand without busting
Players lose if their hand exceeds 21 (busts) or if the dealer's hand is closer to 21
If the player and dealer have the same hand value, it's a push (tie), and the player's bet is returned

I probably won't do any money bets yet. That would be cool to implement, but that'll have to wait

'''

dealerCards = []
playerCards = []

def inititalDeal():
    for x in range(2):
        card = random.randint(1,10)
        if card == 1:
            card = 11
        dealerCards.append(card)
    for x in range(2):
        card = random.randint(1,10)
        if card == 1:
            card = 11
        playerCards.append(card)
    print(playerCards)
    print(dealerCards[0]);

inititalDeal()

