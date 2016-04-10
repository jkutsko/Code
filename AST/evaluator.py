from ast import *

class evaluator():
	def __init__(self):
		self.var_dict = {}


	def evaluate(program):
		for statement in program.statements:
			self.eval_statement(statement)

	def eval_statement(statement):
		t = type(statement).__name__
		if t == "ast.Assignment":
			self.eval_assign(statement)
		elif t == "ast.For_Loop":
			self.eval_for_loop(statement)
		elif t == "ast.Stat_Query":
			self.eval_stat_query(statement)
		elif t == "ast.Combat_Query":
			self.eval_combat_query(statement)
		


