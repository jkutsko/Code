from parcon import * 
import sys
sys.path.insert(0,"../AST")
from ast import *


'''
Parsing helper functions:
'''
# x is [item1, [items]]
def parse_item_def(x):
	items = Items_Declaration([x[0]])
	for item in x[1]:
		items.add_item(item)
	return items

def parse_program(x):
	p = Program([x[0]])
	for i in x[1:]:
		p.add_statement(i)
	return p

# x is [build1,[builds]]
def parse_list(x):
	return List_Of_Builds([x[0]] + x[1])


'''
Forward parser declarations
'''
statement = Forward()
program = OneOrMore(statement)[lambda x: parse_program(x)]
var_name = (Exact(ZeroOrMore(Alphanum() - CharIn('\"," ","="'))))["".join][lambda x: Var_Name(x)]
hero_name = Forward()
item_name = Forward()
stat_name = Forward()
combat_stat_name = Forward()
optimize_command = Forward()

'''
Parser objects for defining values
(builds, item builds, lists, etc)
'''

items_definition = ("(" + item_name + Repeat(("," + item_name),0,5)  + ")")[parse_item_def]

build_assignment = (
	("level: " + number[int] + hero_name + "with:" + items_definition)[lambda x: Build_Assignment_Items(x[0],x[1],x[2])]\
	| ("level: " + number[int] + hero_name + "with:" + var_name)[lambda x: Build_Assignment_Value(x[0],x[1],x[2])]\
	| ("level: " + number[int] + hero_name )[lambda x: Build_Assignment_NoItems(x[0],x[1])])


build = (build_assignment | var_name)

list_of_builds = (("[" + build + OneOrMore("," + build) +  "]")[parse_list]
				| var_name)

value = (build_assignment | items_definition | list_of_builds | var_name ) #| optimize_command

stat_dec = (
	(combat_stat_name + "vs:" + build)[lambda x: Combat_Stat_Declaration(x[0],x[1])]
	| (stat_name)[lambda x: Base_Stat_Declaration(x)])

'''
Assignment
'''
assignment = (var_name + "=" + value)[lambda x: Assignment(x[0],x[1])]


'''
Commands that actually do things
'''
query = (
	 ("get:" + combat_stat_name + "of:" + build + "vs:" + build)[lambda x: Combat_Query(x[0],x[1],x[2])]
	 | ("get:" + stat_name + "of:" + build)[lambda x: Stat_Query(x[0],x[1])])

optimize_command << ("optimize:" + build + "for:" + "{" + OneOrMore((stat_dec + ":" + number[int])) + "}")[lambda x: Optimize_Command(x[0],x[1])]

for_loop = ("for:" + var_name + "in:" + list_of_builds + "{"+ OneOrMore(statement) + "}")[lambda x: For_Loop(x[0], x[1], x[2])]

'''
basic definitions
'''
thing_word = Word('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-') - "with:" - "get:" - "of:" - "," - "and:" - "vs:"
thing_name =  OneOrMore(thing_word)[lambda k: reduce(lambda x,y: x + " " + y, k)]
statement << (query | for_loop | optimize_command | assignment )
hero_name << thing_name[lambda x: Hero_Name(x)]
stat_name << thing_name["".join][lambda x: Stat_Name(x)]
combat_stat_name << thing_name["".join][lambda x: Combat_Stat_Name(x)]
item_name << thing_name["".join][lambda x: Item_Name(x)]



def parse(string):
	return program.parse_string(string)

if __name__ == '__main__':
	print stat_dec.parse_string("damage vs: build3:")

