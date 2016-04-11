import build
import item
import math
import random
from collections import Counter
import matplotlib.pyplot as plt 

N_SIMULATIONS = 1000

#Calculates one instance of a build attacking another build using the game engine's formula
def calculate_damage(attack_build, defend_build):
	base_damage = (attack_build.get_base_damage() + attack_build.plus_damage)
	armor_multiplier = (1-(.06*(defend_build.get_armor())/(1+.06*abs(defend_build.get_armor()))))
	crit_multiplier = 1
	bonus_damage = 0
	for item in attack_build.item_build.items:
		if item.proc_chance != None:
			#Pick the strongest crit
			if random.uniform(0,1) < item.proc_chance and item.proc_type == "crit":
				crit_multiplier = max(crit_multiplier, item.proc_value)
			# Other procs stack, so add them
			if random.uniform(0,1) < item.proc_chance and item.proc_type == "flat":
				bonus_damage += item.proc_value
	total_damage = (base_damage + bonus_damage)*armor_multiplier*crit_multiplier
	return total_damage

# calculates the average damage done per attack
def calculate_average_damage(attack_build, defend_build):
	sum_all_attacks = 0
	for i in range(N_SIMULATIONS):
		sum_all_attacks += calculate_damage(attack_build, defend_build)
	average_damage = sum_all_attacks/N_SIMULATIONS
	return average_damage

# Calculates the DPS of a build based on several trials of attacking,
# and the attack speed of the build.
def calculate_dps(attack_build, defend_build):
	average_damage = calculate_average_damage(attack_build, defend_build)
	return attack_build.get_aps()*average_damage

# Gets the frequency counter of hits it takes a build to
# kill another. Currently, hp regen is not taken into account
# Which shouldn't matter too much since hero skills and
# regen items aren't handled yet because of lack of data...
# TODO: Incorporate HP regen since I have data now
def calculate_hits_to_kill(attack_build, defend_build):
	frequency_counter = Counter()
	for i in range(N_SIMULATIONS):
		defending_hp = defend_build.get_hp()
		hit_count = 0
		while defending_hp > 0:
			defending_hp -= calculate_damage(attack_build, defend_build)
			hit_count += 1
		frequency_counter[hit_count] += 1
	return frequency_counter 

def get_attacks_to_kill(attack_build, defend_build):
	freq = calculate_hits_to_kill(attack_build, defend_build)
	dictionary = plt.figure()
	plt.bar(range(len(freq)), map(lambda k: k/float(N_SIMULATIONS),freq.values()), align='center')
	plt.xticks(range(len(freq)), freq.keys())
	plt.ylabel("Frequency")
	plt.xlabel("Number of Attacks")
	# TODO: Don't hard code this shit:
	plt.title("Attacks it takes for " + attack_build.name + " to kill " +defend_build.name)
	plt.show()

def calculate_time_to_kill(attack_build, defend_build):
	pass