import json

ITEM_DATA_PATH = "../data/item_data.json"
# Just these three for now, since limited item data
SPECIAL_ITEMS = {"Monkey King Bar":["flat",.35,160], "Crystalys":["crit",.20, 1.75], "Daedalus":["crit",.3,2.20]}#,"Skull Basher"}

class Item_Build():
	def __init__(self, items):
		if len(items) > 6:
			print "Too many items"
			raise Exception
		self.items = items
		self.total_cost = sum(map(lambda k: k.cost, items))

	def add_item(self, item):
		self.items.append(item)

class Item():
	def __init__(self, item_name, level = 0):
		self.proc_chance = None
		self.proc_type = None
		self.proc_value = None
		self.cleave_percent = None #for battle_fury
		item_data = json.load(open(ITEM_DATA_PATH,"r"))
		self.data = item_data[item_name]
		if item_name in SPECIAL_ITEMS.keys():
			self.proc_type = SPECIAL_ITEMS[item_name][0]
			self.proc_chance = SPECIAL_ITEMS[item_name][1]
			self.proc_value = SPECIAL_ITEMS[item_name][2]
		self.agi = self.data["Agi"]
		self.int = self.data["Int"]
		self.str = self.data["Str"]
		self.damage = self.data["Damage"]
		self.attack_speed = self.data["attack_speed"]
		self.armor = self.data["Armor"]
		self.magic_resist = self.data["Magic Resistance"]
		self.lifesteal = self.data["lifesteal"]
		self.hp = self.data["HP"]
		self.costs = self.data["Cost"]
		self.cost = sum(self.costs)



