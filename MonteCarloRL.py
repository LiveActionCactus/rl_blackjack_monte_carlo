from Blackjack import Blackjack
from collections import defaultdict

class MonteCarloRL:
	blackjack = Blackjack()
	state_value = defaultdict(list) 		# to be populated from returns: (player sum, dealer showing, useable ace) : ave return
	returns = defaultdict(list) 			# to be populated from game:    (player sum, dealer showing, useable ace) : [reward; occurance(s)]
	gamma = 1.0								# discount rate (closer to 1.0 has longer-term memory)


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

		# play the game for all players
		for hand in reversed(self.blackjack.hands):
			while self.blackjack.scores[hand] < self.blackjack.strategy[hand]:
				self.blackjack.hit(hand)
				self.blackjack.check_player_ace(hand)
				self.blackjack.update_score(hand)
		
				if hand == 'player':
					state = self.generate_state()
					episode_states.append(state)

		winner = self.blackjack.determine_winner()

		self.first_visit_mc_generate_returns(winner, episode_states) 		# assign returns


	def first_visit_mc_generate_returns(self, winner, episode_states):
		reward = None

		if winner == 'player':
			reward = 1
		elif winner == 'dealer':
			reward = -1
		else:
			reward = 0

		episode_states_reversed = list(reversed(episode_states))
		
		for i,state in enumerate(episode_states_reversed):
			if state in episode_states_reversed[i+1:]:
				pass 
			else:
				self.returns[state].append(reward) 			# every state in a win will become a 1 (and vice-versa); thus don't need to keep track of 0


	def first_visit_mc_state_value_estimation(self, num_episodes):
		for i in range(0,num_episodes):
			self.iterate_over_single_episode()
			self.blackjack.reset_game()

		self.calc_state_value_estimates()

		# for state, value in self.state_value.items():
		# 	print(state, value, "\n")

		# print(self.state_value)


	def calc_state_value_estimates(self):
		for key, value in self.returns.items():
			assert key not in self.state_value.keys(), "Key already exists in state_value dictionary!"

			self.state_value[key] = sum(self.returns[key]) / len(self.returns[key])