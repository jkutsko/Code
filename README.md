# DOTA-Builder
Code repository for DSLs Project

# How to run

Currently, this runs by using the python file "dota.py" in the main directory. To get this to work, you must install the following necessary packages:

```
parcon ("pip install parcon")
matplotlib ("pip install matplotlib")
```
To run, first make a file with your program in the Sample Programs folder. Then, edit the line of dota.py with ```prgm_name``` (line 15) to have the name of your file. Then enter: ```python dota.py``` in your command line in the main project directory. Yes, this is gross. No, its not the final implementation. Working on other parts of this at the moment. 

# Documentation
To write a program, you can write a program by following the examples in the Sample Programs folder

Essentially, you specify a build as:

```
build_name = level: X hero_name with: (item1, item2,...)
```

adding items is optional, and you can give the hero a preset item build by declaring it beforehand as:

```
items = (item1, item2, ...)
```

Then, you can query for stats of a build:

```
get: damage of: build1
```

The available stat queries are:
- "damage"
- "hp"
- "armor"
- "agi"
- "int"
- "str"
- "attack speed"
- "mana"
- "attacks per second"


You can also get some stats in relation to another build, with the syntax:

```
get: STAT of: build1 vs: build2:
```

The available combat stat queries are:

```
attacks
```

Which will bring up a frequency graph of how many attacks it might take for build1 to kill build2,

and
```
damage
```
Which will bring up the average damage build1 does to build2

To make a list of builds, you can write:

```
builds = [BUILD1, BUILD2, BUILD3]
```
where each BUILDX is a valid build specification. You can then loop over these builds with the syntax:

```
for: VARIABLE_NAME in: LIST{
	COMMAND
	COMMAND
	.
	.
	.
}
```

Finally, you can get the optimal item for a build's next item given a list of parameters:

```
optimize: myBuild for:{
	armor: 3
	damage vs: defender: 2
	attack speed: 5
	agi: 2
	hp: 4
}
```
The parameter specifications are any valid stat or combat stat, and the integers that follow are your relative priority values.

#TODO:

- add hero ability data
- add efficiency somehow (probably with faked item data for buildup items)
- beef up combat simulation/add more combat queries


#Maybe TODO:
- include hero abilities to grammar/ast/eval
- include other syntax elements when I think of them
- make specifying hero/item/data names smart


#DONE
- add optimize command to the backend
- add optimize command to the grammar, ast, and eval
- Add for loops and lists to grammar and abstract syntax tree. 
- add the evaluator for for loops and lists 
- include all data queries 


