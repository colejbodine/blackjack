import random

# Classes
class Player():
    """Initialize player class"""
    def __init__(self):
        self.hand = []

    def deal(self):
        card = deck.pop()
        if card == 11:
            card = 'J'
        if card == 12:
            card = 'Q'
        if card == 13:
            card = 'K'
        if card == 14:
            card = 'A'
        self.hand.append(card)
        return card


# Functions
def play_game():
    # Set up our local variables
    d_playing = True
    p_playing = True
    p_score = 0
    d_score = 0
    random.shuffle(deck)

    while d_playing or p_playing:
        # The dealer should keep hitting so long as their
        # running total is less than 18, based on conventional strategy.
        if d_score < 18:
            card = dealer.deal()
            if card == 'J': card = 10
            if card == 'Q': card = 10
            if card == 'K': card = 10
            if card == 'A' and d_score < 11: card = 11
            if card == 'A' and d_score >= 11: card = 1
            d_score += int(card)
            print(f"\nDealer hand: {dealer.hand}")
            print(f"The dealer's current score is: {d_score}")
            if d_score > 21:
                print("The dealer busted!")
                p_playing = False
                d_playing = False
        else:
            if d_score == 21 and len(dealer.hand) <= len(player.hand):
                print("The dealer got a blackjack! Dealer wins.")
                p_playing = False
            d_playing = False
        
        # The player's turn:
        if p_playing == True:
            choice = input("\nWould you like to (h)it, (p)ass, or (q)uit? ")
            if choice.lower() == 'p':
                p_playing = False
            elif choice.lower() == 'h':
                card = player.deal()
                if card == 'J': card = 10
                if card == 'Q': card = 10
                if card == 'K': card = 10
                if card == 'A' and p_score < 11: card = 11
                if card == 'A' and p_score >= 11: card = 1
                p_score += int(card)
                print(f"\nYour hand: {player.hand}")
                print(f"Your current score is: {p_score}")
                if p_score > 21:
                    p_playing = False
                    d_playing = False
                    print("You busted!")
            elif choice.lower() == 'q':
                break

    # If player has less than 21 and more than the dealer, they win.
    if p_score > d_score and p_score <= 21:
        print("Congratulations, you win!")
    elif p_score < 21 and d_score > 21:
        print("Congratulations, you win!")
    else:
        print("Sorry, you lost.")


# Variables
player = Player()
dealer = Player()

# Main program
playAgain = True
while playAgain:
    # Empty out the players' hands before the game starts.
    deck = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
        ]
    dealer.hand = []
    player.hand = []
    play_game()
    choice = input("Do you want to play again? (y/n): ")
    if choice.lower() == 'y':
        playAgain = True
    elif choice.lower() == 'n':
        playAgain = False