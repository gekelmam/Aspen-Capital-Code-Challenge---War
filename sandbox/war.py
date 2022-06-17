import random

############################## Variables #############################

deck = []
player_1_deck = []
player_2_deck = []

center_stack = []

player_1_card = 0
player_2_card = 0

game_in_progress = True

######################### Code #################################

# Playing the game
def play():
    player_1_card = draw_card(player_1_deck)
    player_2_card = draw_card(player_2_deck)

    if(player_1_card - player_2_card != 0): # Its a battle 
        if(player_1_card > player_2_card): # Player 1 wins
            player_1_deck.append(player_1_card)
            player_1_deck.append(player_2_card)
            player_1_card = 0
            player_2_card = 0
            return 1
        else: # Player 2 wins
            player_2_deck.append(player_1_card)
            player_2_deck.append(player_2_card)
            player_1_card = 0
            player_2_card = 0
            return 2
    else: # Its a War   
        win = False
        p1_idx = 1
        p2_idx = 3
        # Into the center stack goes:
        # The originally drawn 2 cards
        center_stack.append(player_1_card)
        center_stack.append(player_2_card)

        # While both player's decks have enough to draw from
        while(len(player_1_deck) >= 2 and len(player_2_deck) >= 2): 
            # Plus two more cards from each player:
            # Player 1
            center_stack.append(draw_card(player_1_deck))
            center_stack.append(draw_card(player_1_deck))
            p1_idx += 2

            # Player 2
            center_stack.append(draw_card(player_2_deck))
            center_stack.append(draw_card(player_2_deck))
            p2_idx += 2

            # The center stack looks something like this:
            # [1, 2, 1, 1, 2, 2]

            if(center_stack[p1_idx] - center_stack[p2_idx] != 0): # Its a battle 
                if(player_1_card > player_2_card): # Player 1 wins
                    for x in center_stack:
                        player_1_deck.append(x)
                    center_stack.clear()
                    return 1
                else: # Player 2 wins
                    for x in center_stack:
                        player_2_deck.append(x)
                    center_stack.clear()
                    return 2
        if(len(player_1_deck) < 2):
            return 2
        else:
            return 1

def draw_card(list):
    return list.pop(0)

############################### Driver Code ######################################

for x in range(4):
    for y in range(2, 15):
        deck.append(y)
random.shuffle(deck)

player_1_deck = deck[0 : int(len(deck)/2)]
player_2_deck = deck[int(len(deck)/2) : len(deck)]

# print(play())