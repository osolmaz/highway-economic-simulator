import simpy
from highway_economic_simulator import *
import progressbar


INITIAL_SUPPLY = 1000000000000

env = simpy.Environment()

# A simple setup of 2 fast 1 slow validators with equal weight

v1 = SimpleValidator(100000000000, "A")
v1.set_constant_round_exponent(15)

v2 = SimpleValidator(100000000000, "B")
v2.set_constant_round_exponent(14)

v3 = SimpleValidator(100000000000, "C")
v3.set_constant_round_exponent(14)


state = EraState(env, INITIAL_SUPPLY)

state.add_validators([v1, v2, v3])
state.initialize_simulation()

env.run(until=TICKS_PER_ERA)

# bar = progressbar.ProgressBar(max_value=TICKS_PER_ERA)
# for tick in range(TICKS_PER_ERA):
#     state.next_tick()
#     bar.update(tick)

# state.distribute_rewards()
# print(state.output_result())
