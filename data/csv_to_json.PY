import json

tags = ["Name", "All","Str","Agi","Int","Armor","Dmg","AS","HPregen","Manaregen %","Life Steal %","Spell Resist %","Evasion %","Mana","Health","MS","Block","Gold Cost","Gold Value","Stat Efficiency","Value - Cost"]

file_name = "Dota 2 Item Efficiency.csv"

f = open(file_name,"r")

d = {}

line = f.readline()
# some hacky stuff to handle dumb formatting
while line:
	list_of_things = line.split(",")
	item_data = {}
	for i in range(len(list_of_things[1:])):
		thing = list_of_things[i+1]
		if len(thing) > 0 and thing[-1] == "\n":
			thing = thing[:-1]
		if len(thing) > 0 and thing[-1] == "%":
			thing = float(thing[:-1])/100.0
		if thing == "":
			thing = 0
		try:
			thing = int(thing)
		except Exception:
			pass
		item_data[tags[i+1]] = thing

	d[list_of_things[0]] = item_data
	line = f.readline()

json.dump(d, open("item_data2.json","w"))

