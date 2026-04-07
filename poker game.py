import random


# Deck class from Section 11.5, with cards-in-play tracking

class Deck():

    def __init__(self, size):
        # Create a list of card numbers 0..size-1
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []   # Cards currently on the table
        self.discards_list = []        # Cards from previous hands
        random.shuffle(self.card_list) # Shuffle at start

    def deal(self):
        """
        Deals one card. If the deck is empty, reshuffle the discards.
        """
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print("Reshuffling...!!!")

        # Remove card from top of deck
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    def new_hand(self):
        """
        Moves all cards currently in play into the discard pile.
        Called when a hand is finished.
        """
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()



# Convert card number (0–51) into rank + suit

def card_to_string(card_num):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
             '10', 'J', 'Q', 'K', 'A']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']

    r = card_num % 13
    s = card_num // 13
    return f"{ranks[r]} of {suits[s]}"



# Deal a 5‑card Poker hand

def deal_hand(deck):
    hand = []
    for _ in range(5):
        hand.append(deck.deal())
    return hand



# Replace selected cards in the hand

def replace_cards(deck, hand, positions):
    """
    positions = list of card positions (1–5) to replace
    """
    for pos in positions:
        index = pos - 1  # Convert 1–5 to 0–4
        hand[index] = deck.deal()
    return hand



# Main Program

def main():
    print("=== Poker Hand Program ===")

    deck = Deck(52)

    # Deal initial hand
    hand = deal_hand(deck)
    print("\nYour initial hand:")
    for i, card in enumerate(hand, start=1):
        print(i, "-", card_to_string(card))

    # Ask user which cards to replace
    user_input = input("\nEnter card numbers to replace (e.g., 1 3 5), or press Enter to keep all: ")

    if user_input.strip() != "":
        positions = [int(x) for x in user_input.split()]
        hand = replace_cards(deck, hand, positions)

    # Show final hand
    print("\nYour final hand:")
    for i, card in enumerate(hand, start=1):
        print(i, "-", card_to_string(card))

    # Move cards to discard pile
    deck.new_hand()


# Run the program
main()
