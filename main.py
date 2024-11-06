from Blackjack import Blackjack
from MonteCarloRL import MonteCarloRL
from Plotting import Plotting

test = Blackjack()
# test.start_game()
# test.multi_start_game(1000)

mc_rl = MonteCarloRL()
# mc_rl.iterate_over_single_episode()
mc_rl.first_visit_mc_state_value_estimation(10000)

plt = Plotting(mc_rl.state_value)