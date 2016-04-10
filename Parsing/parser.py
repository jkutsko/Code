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


'''
Forward parser declarations
'''
statement = Forward()
program = OneOrMore(statement)
var_name = (Exact(ZeroOrMore(Alphanum() - CharIn('\"," ","="'))))["".join][lambda x: Var_Name(x)]
hero_name = Forward()
item_name = Forward()
stat_name = Forward()

'''
Parser objects for defining values
(builds, item builds, lists, etc)
'''

items_definition = ("(" + item_name + Repeat(("and" + item_name),0,5)  + ")")[parse_item_def]

build_assignment = (
	("level: " + number[int] + hero_name + "with:" + items_definition)[lambda x: Build_Assignment_Items(x[0],x[1],x[2])]\
	| ("level: " + number[int] + hero_name + "with:" + var_name)[lambda x: Build_Assignment_Value(x[0,x[1],x[2]])]\
	| ("level: " + number[int] + hero_name )[lambda x: Build_Assignment_NoItems(x[0],x[1])])


build = (build_assignment | var_name)

value = (build_assignment | items_definition | var_name) # | list_of_builds | optimize_command


'''
Assignment
'''
assignment = (var_name + "=" + value)[lambda x: Assignment(x[0],x[1])]


'''
Commands that actually do things
'''
query = (
	("get" + stat_name + "of" + build)[lambda x: Stat_Query(x[1],x[0])]
	| ("get" + stat_name + "of" + build + "vs" + build)[lambda x: Combat_Query(x[1],x[0],x[2])])

optimize_command = (
	("optimize" + build + "for" +  stat_name)[lambda x: Stat_Query(x[1],x[0])]
	| ("optimize" + build + "for" +  stat_name + "vs" + build)[lambda x: Combat_Query(x[1],x[0],x[2])])


statement << (assignment | query | optimize_command)
hero_name << alpha_word[lambda x: Hero_Name(x)]
stat_name << alpha_word["".join][lambda x: Stat_Name(x)]
item_name << alpha_word["".join][lambda x: Item_Name(x)]


x = statement.parse_string("build1 = level: 22 AntiMage with: (daedalus and mekansm and butterfly)")
print x