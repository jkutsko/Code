# DOTA-Builder
Code repository for DSLs Project

# How to run

Currently, this runs by using the python file "dota.py" in the main directory. To get this to work, you must install the following necessary packages:

```
parcon ("pip install parcon")
matplotlib ("pip install matplotlib")
```
To run, edit the line of dota.py with ```prgm_name``` to have the name of your file. Then enter: ```python dota.py``` in your command line in the main project directory. Yes, this is gross. No, its not the final implementation. 

Then, you can write a program by following the examples in Sample Programs/sample1.dota

Essentially, you specify a build as:

```
build_name = level: X hero_name with: (item1 and item2 and...)
```

adding items is optional, and you can give the hero a preset item build by declaring it beforehand as:

```
items = (item1 and item2 and ...)
```

Then, you can query for stats of a build. Currently, the only available stats are:
"damage", and "hp", like:

```
get: damage of: build1
```

You can also get the number of attacks it takes for one build to kill another, like:

```
get: attacks of: build1 vs: build2:
```

Thats about it at the moment, soon lists, loops, and more stat queries will be available, followed by the ```optimize``` keyword.




#TODO:

- Add for loops and lists to grammar and abstract syntax tree. 
- add the evaluator for for loops and lists
- include all data queries
- add hero ability data
- beef up combat simulation
- add optimize command to the backend
- add optimize command to the grammar, ast, and eval
- make specifying hero/item/data names smart
- add efficiency somehow (probably with faked item data for buildup items)
- include hero abilities to grammar/ast/eval
- include other syntax elements when I think of them


