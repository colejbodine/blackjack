import random


# Classes
class Player:
    """A class representing a player."""

    def __init__(self, name):
        """Initialize the player class."""
        self.hand = []
        self.score = 0
        self.name = name
        self.playing = True

    def deal(self):
        """Deal a card."""
        card = deck.pop()

        # Assign the face value to the card (What you see in hand)
        if card == 11:
            card = 'J'
        if card == 12:
            card = 'Q'
        if card == 13:
            card = 'K'
        if card == 14:
            card = 'A'
        self.hand.append(card)

        # Assign numerical value to the card (What you see in score)
        if card == 'J':
            card = 10
        if card == 'Q':
            card = 10
        if card == 'K':
            card = 10
        if card == 'A' and self.score < 11:
            card = 11
        if card == 'A' and self.score >= 11:
            card = 1

        # Add the numerical value of the player's card to their score.
        self.score += card

        # Print information about player's hand:
        print(f"\n{self.name.title()}'s hand: {self.hand}")
        print(f"{self.name.title()}'s' current score is: {self.score}")

        # If the player busts, let them know!
        if self.score > 21:
            print(f"\n{self.name.title()} busted!")
            self.playing = False


# Functions
def play_game():
    # Set up our local variables
    random.shuffle(deck)
    dealer.deal()
    player.deal()

    while dealer.playing or player.playing:
        # The dealer should keep hitting so long as their
        # running total is less than 17, based on conventional strategy.
        if dealer.score < 17:
            dealer.deal()
        else:
            dealer.playing = False
            if dealer.score == 21 and len(dealer.hand) <= len(player.hand):
                print(f"{dealer.name.title()} got a blackjack! \
                    {dealer.name.title()} wins.")
                player.playing = False
            elif dealer.score > 21 and player.score <= 21:
                player.playing = False

        # The player's turn:
        if player.playing:
            choice = input("\nWould you like to (h)it, (p)ass, or (q)uit? ")
            if choice.lower() == 'p':
                player.playing = False
            elif choice.lower() == 'h':
                player.deal()
                if player.score > 21:
                    dealer.playing = False
            elif choice.lower() == 'q':
                break

    # If player has less than 21 and more than the dealer, they win.
    if (dealer.score < player.score <= 21) or \
            (player.score < 21 and dealer.score > 21):
        print(f"\nCongratulations, {player.name.title()} won!")
    else:
        print(f"\n{player.name.title()} lost.")


# Main program
playAgain = True
while playAgain:
    # Reset deck before the game starts.
    deck = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
        ]

    # Gather the player's name and initialize them..
    name = input("What is your name? Enter here: ")
    player = Player(name)
    player.hand = []
    player.score = 0
    # Initialize the dealer.
    dealer = Player("Dealer")
    dealer.hand = []
    dealer.score = 0
    play_game()
    choice = input("\nDo you want to play again? (y/n): ")
    if choice.lower() == 'y':
        playAgain = True
    elif choice.lower() == 'n':
        playAgain = False
