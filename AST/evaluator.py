from ast import *
import sys
sys.path.insert(0,"../IR")
sys.path.insert(0,"../data")
from build import Build
from combat import *
from item import *

from copy import deepcopy

# Evaluates the abstract syntax tree result of parsing a program
class Evaluator(object):
	def __init__(self):
		# Stores the vars and their corresponding values,
		# Evaluated to be the actual IR classes
		# Everything other than assignment just prints
		# things for the user
		self.var_dict = {}

	# The main evaluate method, recursively calls other eval methods
	def evaluate(self, program):
		for statement in program.statements:
			self.eval_statement(statement)

	def eval_statement(self, statement):
		t = type(statement).__name__
		if t == "Assignment":
			self.eval_assign(statement)
		elif t == "For_Loop":
			self.eval_for_loop(statement)
		elif t == "Stat_Query":
			self.eval_stat_query(statement)
		elif t == "Combat_Query":
			self.eval_combat_query(statement)

	def eval_assign(self, statement):
		val = self.eval_value(statement.var_value)
		self.var_dict[statement.var_name.name] = val


	'''
	Evaluators that just execute code
	'''
	# slightly gross method that does a bunch of different
	# things based on the stat that's queried
	def eval_stat_query(self, statement):
		stat_name = self.eval_stat_name(statement.stat_name)
		build_value = self.eval_value(statement.var_name)
		if stat_name == "damage":
			base = build_value.get_base_damage()
			plus = build_value.plus_damage
			print str(base) + " + " + str(plus)
		elif stat_name == "hp":
			print build_value.get_hp()
		else:
			print stat_name + "not valid query"
		# TODO: finish this for not demo stuff

	def eval_combat_query(self, statement):
		stat_name = self.eval_stat_name(statement.stat_name)
		att_build = self.eval_value(statement.attack_build)
		def_build = self.eval_value(statement.defend_build)
		if type(att_build).__name__ != "Build":
			print "Attacking build is not a valid build"
			raise Exception
		elif type(def_build).__name__ != "Build":
			print "Defending build is not a valid build"
			raise Exception
		if stat_name == "attacks":
			get_attacks_to_kill(att_build, def_build)

	def eval_for_loop(self, statement):
		for list_elem in self.eval_value(statement.list):
			self.var_dict[statement.var_name.name] = list_elem
			for inner_statement in statement.statements:
				self.eval_statement(inner_statement)

	# don't even have backend for this yet, lol
	def eval_optimize_command(self, statement):
		print "optimizing something, trust me"

	'''
	Evaluators that return things
	'''
	def eval_value(self, value):
		t = type(value).__name__
		if t == "Var_Name":
			return self.eval_var_name(value)
		elif t == "Items_Declaration":
			return self.eval_item_dec(value)
		elif t.startswith("Build_Assignment"):
			return self.eval_build_assignment(value)
		elif t == "List_Of_Builds":
			return list(map(lambda k: self.eval_value(k), value.builds))
		else:
			print "Type not found"

	def eval_var_name(self,value):
		try:
			return self.var_dict[value.name]
		except Exception: #var isn't in var_dict
			print "Variable: " + value.name + " hasn't been defined yet"
			raise Exception

	def eval_item_dec(self,value):
		items = value.items
		actual_items = map(lambda k: self.eval_item_name(k), items)
		item_build = Item_Build([])
		for item in actual_items:
			actual_item = Item(item)
			item_build.add_item(actual_item)
		return item_build


	def eval_build_assignment(self,build_assign):
		t = type(build_assign).__name__
		if t == "Build_Assignment_Value":
			return self.eval_build_value(build_assign)
		elif t == "Build_Assignment_Items":
			return self.eval_build_items(build_assign)
		elif t == "Build_Assignment_NoItems":
			return self.eval_build_none(build_assign)

	def eval_build_value(self,build_assign):
		level = build_assign.level
		hero_name = self.eval_hero_name(build_assign.hero_name)
		item_build = self.eval_var_name(build_assign.items_name)
		if type(item_build).__name__ != "Item_Build":
			print "Variable: " + items_name + "isn't an item build"
			raise Exception
		build = Build(hero_name, level)
		build.give_item_build(item_build)
		return build


	def eval_build_items(self,build_assign):
		level = build_assign.level
		hero_name = self.eval_hero_name(build_assign.hero_name)
		item_build = self.eval_item_dec(build_assign.items_dec)
		build = Build(hero_name, level)
		build.give_item_build(item_build)
		return build

	def eval_build_none(self,build_assign):
		level = build_assign.level
		hero_name = self.eval_hero_name(build_assign.hero_name)
		build = Build(hero_name, level)
		return build


	'''
	TODO: Make these smarter - I.E. have them check for edit 
	distance to names and fix if close enough.
	'''
	def eval_item_name(self,item_name):
		return item_name.name

	def eval_stat_name(self,stat_name):
		return stat_name.name 

	def eval_hero_name(self,hero_name):
		return hero_name.name



