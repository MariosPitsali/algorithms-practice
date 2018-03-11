import random

cards = { 0: "A",
          1: "K",
          2: "Q",
          3: "J",
          4: 10,
          5: 9,
          6: 8,
          7: 7,
          8: 6,
          9: 5,
          10: 4,
          11: 3,
         12 : 2}
         
worth = {10: ['A', 'K', 'Q', 10]}

suits = { 0: "HEARTS",
        1: "CLUBS",
        2: "DIAMONDS",
        3: "SPADES"}
dealer_score = 0
player_score = 0
chosen = []
while True:
    suit = random.randint(0,3)
    card = random.randint(0,12)
    ch = str(suit) + str(card)
    chosen.append(ch)
    w = card
    score += 
    