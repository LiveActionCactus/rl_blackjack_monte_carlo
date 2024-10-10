
import random

class Deck:
	num_decks = 1
	deck_baseline = {}
	deck = []

	def __init__(self, num_decks=1):
		self.num_decks = num_decks
		self.deck_baseline = self.create_deck_baseline()
		self.deck = self.initialize_deck()


	def create_deck_baseline(self, deck_baseline={}):
		if deck_baseline:
			pass
		else:
			deck_baseline = {
				"2" : 2, "3" : 3,
				"4" : 4, "5" : 5,
				"6" : 6, "7" : 7,
				"8" : 8, "9" : 9,
				"10" : 10, "J" : 10,
				"Q" : 10,  "K" : 10,
				"A" : [1, 11]
			}

		return deck_baseline


	def initialize_deck(self):
		deck = []
		suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
		single_deck = []

		for suit in suits:
			single_deck.extend([(card, value, suit) for card, value in self.deck_baseline.items()])

		for i in range(0, self.num_decks):
			deck.extend(single_deck)

		deck = self.shuffle_deck(deck)

		return deck


	def shuffle_deck(self, deck):
		shuffled = []

		random.seed()
		while(len(deck) > 0):
			if (1 == len(deck)):
				pick = 0
			else:
				pick = random.randrange(0, len(deck))
				
			shuffled.append(deck[pick])
			del deck[pick]		

		return shuffled


	def draw_card_with_replacement(self):
		assert self.deck, "Deck is empty, need to initailize a deck first"

		return random.choice(self.deck)
