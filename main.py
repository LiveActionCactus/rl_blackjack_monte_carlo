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
	win_count = {
		"dealer" : 0,
		"player" : 0
	}


	def start_game(self):
		self.initialize_hands()
		# TODO: bet table minimum
		self.play_player_hands()   		# includes betting between rounds
		self.determine_winner()

	def multi_start_game(self, starts):
		for i in range(0, starts):
			self.start_game()

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
		possible_winners = [(player, score) for player, score in self.scores.items() if score <= 21]

		if not possible_winners:
			print("No winner!")
		else:
			winner = max(possible_winners, key=lambda item: item[1])

			if len(winner) > 2:
				print("Tie!")
			else:
				print(winner[0] + " wins!")
				self.win_count[winner[0]] += 1


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
				break
			elif new_best_score <= 21:
				best_score = new_best_score


		assert best_score >= (score_calc + num_aces), "Ace(s) score calculation error -- best: " + str(best_score) + " min: " + str(score_calc+num_aces)

		return best_score


	def hit(self, hand):
		self.hands[hand].append(self.deck.draw_card_with_replacement())


	def stick(self):
		print(hand + " sticks with score " + self.score[hand])


test = Blackjack()
# test.start_game()
test.multi_start_game(25)
# print(test.hands)
# print(test.scores)
# test.hit()
# test.print(player_hand)