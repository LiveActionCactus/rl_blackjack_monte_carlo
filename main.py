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
		single_deck = [(card, value) for card, value in self.deck_baseline.items()]

		for i in range(0, self.num_decks):
			deck.extend(single_deck)

		return deck

	# TODO: this could result in a game with more than 4 cards of the same kind; need to include a check 
	def draw_card_with_replacement(self):
		assert self.deck, "Deck is empty, need to initailize a deck first"

		return random.choice(self.deck)


class Blackjack:
	deck = Deck()
	hands = {
		"dealer" : [],
		"player" : []
	}
	scores = {
		"dealer" : 0,
		"player" : 0
	}
	has_ace = {
		"dealer" : False,
		"player" : False
	}
	player_stick_policy = 20
	dealer_stick_policy = 17

	def start_game(self):
		self.initialize_hands()
		self.play_player_hands()

	def initialize_hands(self):
		# draw initial hands for all players and dealer
		for hand in self.hands:
			self.hands[hand].append(self.deck.draw_card_with_replacement())
			self.hands[hand].append(self.deck.draw_card_with_replacement())

			self.check_player_ace(hand)
			self.update_score(hand)

	def play_player_hands(self):
		for hand in self.hands:
			if hand == "dealer":
				break
			else:
				while self.player_strategy(hand):
					self.hit(hand)
					self.check_player_ace(hand)
					self.scores[hand] = self.update_score(hand)

	def player_strategy(self, hand):
		if self.score[hand] >= 20:
			return False
		else:
			return True

	# TODO: handle more than 1 ace in hand
	def update_score(self, hand):
		score_calc = 0
		
		for card in self.hands[hand]:
			if card[0] == "A":
				pass
			else:
				score_calc += card[1]

		if self.has_ace[hand]:
			if score_calc + 11 < 21:
				score_calc += 11
			elif score_calc + 1 < 21:
				score_calc += 1
			else:
				print(hand + " BUST")

		self.scores[hand] = score_calc


	def check_player_ace(self, hand):
		if any("A" == card[0] for card in self.hands[hand]):
			print('hi mom')
			self.has_ace[hand] = True

	def hit(self, hand):
		self.score[hand].append(self.deck.draw_card_with_replacement())

	def stick(self):
		print(hand + " sticks with score " + self.score[hand])


test = Blackjack()
test.start_game()
print(test.hands)
print(test.scores)
# test.hit()
# test.print(player_hand)