import json

ITEM_DATA_PATH = "../data/item_data.json"
SPECIAL_ITEMS = {"Monkey King Bar":["flat",.35,160],
 "Crystalys":["crit",.20, 1.75],
 "Daedalus":["crit",.3,2.20],
 "Skull Basher":["flat", .25, 120],
 "Maelstrom":["flat", .25, 120],
 "Mjollnir":["flat",.2,200],
 "Abyssal Blade":["flat",.25,120]
 }

class Item_Build():
	def __init__(self, items):
		if len(items) > 6:
			print "Too many items"
			raise Exception
		self.items = items
		
	def get_total_cost(self):
		if len(self.items) > 0:
			return sum(map(lambda k: k.cost, items))
		else:
			return 0

	def add_item(self, item):
		self.items.append(item)

class Item():
	def __init__(self, item_name, level = 0):
		self.proc_chance = None
		self.proc_type = None
		self.proc_value = None
		self.cleave_percent = None #for battle_fury, sven cleave, etc
		self.evasion = 0
		item_data = json.load(open(ITEM_DATA_PATH,"r"))
		self.data = item_data[item_name]
		if item_name in SPECIAL_ITEMS.keys():
			self.proc_type = SPECIAL_ITEMS[item_name][0]
			self.proc_chance = SPECIAL_ITEMS[item_name][1]
			self.proc_value = SPECIAL_ITEMS[item_name][2]
		self.agi = self.data["Agi"] + self.data["All"]
		self.int = self.data["Int"] + self.data["All"]
		self.str = self.data["Str"] + self.data["All"]
		self.damage = self.data["Dmg"]
		self.attack_speed = self.data["AS"]
		self.armor = self.data["Armor"]
		self.magic_resist = self.data["Spell Resist %"]
		self.lifesteal = self.data["Life Steal %"]/100.0
		self.hp = self.data["Health"]
		self.costs = self.data["Gold Cost"]
		self.evasion = self.data["Evasion %"]/100.0



