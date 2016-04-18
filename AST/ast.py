'''
A Program in this language is a list of statements
'''

class Program(object):
	def __init__(self, statements = []):
		self.statements = statements
		self.variable_dict = {}
	def add_statement(self, statement):
		self.statements.append(statement)
	def eval(self):
		pass
		#go through and eval every statement
'''
"Abstract" classes go here. Actual abstract classes are 
needlessly complicated in python, so we'll just do it 
by giving each a blank constructor and eval method and
having each subclass implement both of those
'''

class Statement(object):
	def __init__(self):
		pass
	def eval(self):
		pass

class Query(Statement):
	def __init__(self):
		pass 
	def eval(self):
		pass

class Value(object):
	def __init__(self):
		pass
	def eval(self):
		pass


class Build_Assignment(Value):
	def __init__(self):
		pass
	def eval(self):
		pass


'''
The implementation classes go here
'''

class Assignment(Statement):
	def __init__(self, var_name, var_value):
		self.var_value = var_value
		self.var_name = var_name

class For_Loop(Statement):
	def __init__(self, var_name, iter_list, statements):
		self.var_name = var_name
		self.list = iter_list
		self.statements = statements

class List_Of_Builds(Value):
	def __init__(self, builds):
		self.builds = builds

class Build_Assignment_Items(Build_Assignment):
	def __init__(self, level, hero_name, items_dec):
		self.level = level
		self.hero_name = hero_name
		self.items_dec = items_dec

class Build_Assignment_Value(Build_Assignment):
	def __init__(self, level, hero_name, items_name):
		self.level = level
		self.hero_name = hero_name
		self.items_name = items_name

class Build_Assignment_NoItems(Build_Assignment):
	def __init__(self, level, hero_name):
		self.level = level
		self.hero_name = hero_name
		self.items = []

class Items_Declaration(Value):
	def __init__(self, items = []):
		self.items = items
	def add_item(self, item_name):
		self.items.append(item_name)

class Stat_Query(Query):
	def __init__(self, stat_name, var_name):
		self.stat_name = stat_name
		self.var_name = var_name

class Combat_Query(Query):
	def __init__(self, stat_name, attack_build, defend_build):
		self.stat_name = stat_name
		self.attack_build = attack_build
		self.defend_build = defend_build

class Var_Name(Value):
	def __init__(self, name):
		self.name = name

class Stat_Name(object):
	def __init__(self, name):
		self.name = name

class Hero_Name(object):
	def __init__(self, name):
		self.name = name

class Item_Name(object):
	def __init__(self, name):
		self.name = name


