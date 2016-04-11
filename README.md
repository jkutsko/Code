# Code
Code for DSLs Project

# How to run

Currently, this runs by using the python file "dota.py" in the main directory. To get this to work, you must install the following necessary packages:

'''
parcon ("pip install parcon")
matplotlib ("pip install matplotlib")
'''

Then, you can run the program by following the examples in Sample Programs/sample1.dota

Essentially, you specify a build as:

'''
build_name = level: X hero_name with: (item1 and item2 and...)
'''

adding items is optional, and you can give the hero a preset item build by declaring it beforehand as:

'''
items = (item1 and item2 and ...)
'''

Then, you can query for stats of a build. Currently, the only available stats are:
"damage", and "hp", like:

'''
get: damage of: build1
'''

You can also get the number of attacks it takes for one build to kill another, like:

'''
get: attacks of: build1 vs: build2:
'''

Thats about it at the moment, soon lists, loops, and more stat queries will be available, followed by the '''optimize''' keyword!


