from Blackjack import Blackjack
from MonteCarloRL import MonteCarloRL

test = Blackjack()
# test.start_game()
# test.multi_start_game(1000)

mc_rl = MonteCarloRL()
mc_rl.iterate_over_single_episode()