from Deck import Deck

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
	strategy = {
		"dealer" : 17,
		"player" : 20
	}
	has_ace = {
		"dealer" : False,
		"player" : False
	}
	has_useable_ace = {
		"dealer" : False,
		"player" : False
	}
	win_count = {
		"dealer" : 0,
		"player" : 0
	}


	def reset_game(self):
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
		has_useable_ace = {
			"dealer" : False,
			"player" : False
		}


	def start_game(self, verbose=True):
		self.initialize_hands()
		# TODO: bet table minimum
		self.play_player_hands()   		# includes betting between rounds
		self.determine_winner()

		if verbose:
			print(self.hands)
			print(self.has_useable_ace)
			print(self.scores)
			print(self.win_count)


	def multi_start_game(self, starts):
		for i in range(0, starts):
			self.start_game(verbose=False)
			self.reset_game()
			# print(self.hands)
			# print(self.scores)

		print(self.win_count)


	def initialize_hands(self):
		# draw initial hands for all players and dealer
		for hand in self.hands: 												# for each player/dealer
			self.hands[hand] = []
			self.hands[hand].append(self.deck.draw_card_with_replacement()) 	# draw card 1
			self.hands[hand].append(self.deck.draw_card_with_replacement()) 	# draw card 2

			self.check_player_ace(hand)
			self.update_score(hand)


	def play_player_hands(self):
		for hand in reversed(self.hands):
			while self.scores[hand] < self.strategy[hand]:
				self.hit(hand)
				self.check_player_ace(hand)
				self.update_score(hand)


	def determine_winner(self):
		possible_winners = [player for player, score in self.scores.items() if score <= 21]
		ties = []
		high_score = 0

		if not possible_winners:
			return "None"
			# print("No winner!") 									# print no winner -- TODO: verbose mode
		else:
			for player in possible_winners:
				if self.scores[player] > high_score:
					ties = [player]
					high_score = self.scores[player]
				elif self.scores[player] == high_score:
					ties.append(player)

			if len(ties) == 1:
				self.win_count[ties[0]] += 1
				return ties[0]
			else:
				for player in ties:
					self.win_count[player] += 0.5
					return "Draw"

			# print(', '.join(ties).upper() + " won!") 				# print winner of game -- TODO: verbose mode


	def update_score(self, hand):
		score_calc = 0
		aces = [] 						# handle 2 or more aces in hand

		for card in self.hands[hand]:
			if card[0] == "A":
				pass
			else:
				score_calc += card[1]

		if self.has_ace[hand]:
			score_calc = self.score_ace(hand, score_calc)

		self.scores[hand] = score_calc


	def check_player_ace(self, hand):
		if any("A" == card[0] for card in self.hands[hand]):
			self.has_ace[hand] = True


	def score_ace(self, hand, score_calc):
		num_aces = sum(1 for card in self.hands[hand] if card[0] == 'A')
		best_score = score_calc + num_aces										# all aces value of 1; lowest possible score

		for i in range(0, num_aces):
			new_best_score = score_calc + (num_aces-(i+1)) + (11*(i+1)) 		# sliding window Aces 1 or 11 calc
			
			if new_best_score > 21:
				if i == 0:
					self.has_useable_ace[hand] = False
				
				break

			elif new_best_score <= 21:
				self.has_useable_ace[hand] = True
				best_score = new_best_score

		assert best_score >= (score_calc + num_aces), "Ace(s) score calculation error -- best: " + str(best_score) + " min: " + str(score_calc+num_aces)

		return best_score


	def hit(self, hand):
		self.hands[hand].append(self.deck.draw_card_with_replacement())


	def stick(self):
		print(hand + " sticks with score " + self.score[hand])