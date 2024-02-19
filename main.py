import random

class Card:
    suits = ["♠", "♣", "♥", "♦"]
    values = {1: "A", 11: "J", 12: "Q", 13: "K"}

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.name = self.values.get(value, str(value))
        self.symbol = self.suits[suit]

    def __str__(self):
        return f"{self.name}{self.symbol}"

class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for suit in range(4) for value in range(1, 14)]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None

class Solitaire:
    def __init__(self):
        self.deck = Deck()
        self.tableau = [[] for _ in range(7)]  # 7 piles for the tableau
        self.foundations = [[] for _ in range(4)]  # 4 foundations for each suit
        self.waste = []

    def deal_cards(self):
        for i in range(7):
            for j in range(i + 1):
                self.tableau[i].append(self.deck.draw())
                if j == i:  # flip the last card in each pile
                    self.tableau[i][-1].flipped = True

    def display(self):
        print("\nFoundations:")
        for pile in self.foundations:
            top_card = pile[-1] if pile else None
            print(top_card or "   ", end=" ")
        print("\n")

        print("Tableau:")
        max_height = max(len(pile) for pile in self.tableau)
        for i in range(max_height):
            for pile in self.tableau:
                if len(pile) > i:
                    card = pile[i]
                    print(card if card.flipped else "  *", end=" ")
                else:
                    print("   ", end=" ")
            print()

    def play(self):
        self.deal_cards()
        while True:
            self.display()
            command = input("Enter your command (help for instructions): ").lower()
            if command == "help":
                self.help()
            elif command == "q":
                print("Thanks for playing Solitaire!")
                break
            elif command == "d":
                if not self.deck.cards:
                    self.deck.cards = self.waste[::-1]
                    self.waste = []
                self.waste.append(self.deck.draw())
            else:
                print("Invalid command. Type 'help' for instructions.")

    def help(self):
        print("\nCommands:")
        print("d: Draw a card from the deck")
        print("q: Quit the game")
        print("help: Show these instructions\n")

if __name__ == "__main__":
    solitaire = Solitaire()
    solitaire.play()
