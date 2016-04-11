from ast import *

# Evaluates the abstract syntax tree result of parsing a program
class evaluator(object):
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
		self.var_dict[statement.var_name] = val


	'''
	Evaluators that just execute code
	'''
	def eval_for_loop(statement):
		pass

	def eval_stat_query(statement):
		pass

	def eval_combat_query(statement):
		pass

	'''
	Evaluators that return things
	'''
	def eval_value(self, value):
		t = type(value).__name__
		if t == "Var_Name":
			return self.eval_var_name(value)
		elif t == "Items_Declaration":
			return self.eval_item_dec(value)
		elif t == "Build_Assignment":
			return self.eval_build_assignment(value)

	def eval_var_name(value):
		return self.var_dict[value.name]

	def eval_item_dec(value):
		pass

	def eval_build_assignment(build_assign):
		t = type(build_assign).__name__
		if t == "Build_Assignment_Value":
			return self.eval(build_assign_value)

	'''
	TODO: Make these smarter - I.E. have them check for edit 
	distance to names and fix if close enough.
	'''
	def eval_item_name(item_name):
		return item_name.name

	def eval_stat_name(stat_name):
		return stat_name.name 

	def eval_hero_name(hero_name):
		return hero_name.name



