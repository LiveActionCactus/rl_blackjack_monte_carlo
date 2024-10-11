from Blackjack import Blackjack

class MonteCarloRL:
	blackjack = Blackjack()
	state_value = {} 					# to be populated from returns: (player sum, dealer showing, useable ace) : ave return
	returns = {} 						# to be populated from game:    (player sum, dealer showing, useable ace) : [reward; occurance(s)]
	gamma = 1.0							# discount rate (closer to 1.0 has longer-term memory)


	def generate_state(self):
		player_sum = self.blackjack.scores['player']		
		dealer_showing = self.blackjack.hands['dealer'][1][1]

		if isinstance(dealer_showing, list):
			dealer_showing = min(dealer_showing)
		
		return (player_sum, dealer_showing, self.blackjack.has_useable_ace['player'])


	def iterate_over_single_episode(self):
		episode_states = []

		self.blackjack.initialize_hands()
		state = self.generate_state()
		episode_states.append(state)

		for hand in reversed(self.blackjack.hands):
			while self.blackjack.scores[hand] < self.blackjack.strategy[hand]:
				self.blackjack.hit(hand)
				self.blackjack.check_player_ace(hand)
				self.blackjack.update_score(hand)
		
				if hand == 'player':
					state = self.generate_state()
					episode_states.append(state)

		winner = self.blackjack.determine_winner()
		print(winner, state)
		print(self.blackjack.hands)
	
		print()
		print(episode_states)
		# input()

		G = 0 			# approx reward
		for state in reversed(episode_states):
			pass

	