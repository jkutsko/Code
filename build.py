import os
from Item.py import Item
import combat.py
import json

DATA_FOLDER_PATH = "../data/hero_data.json"

PRIMARY_STATS = {0:"str",1:"agi",2:"int"}
HERO_NUMS = {u'Razor': u'48', u'Night Stalker': u'23', u'Naga Siren': u'45', u'Undying': u'28', u'Dragon Knight': u'6', u'Juggernaut': u'32', u'Ursa': u'42', u'Jakiro': u'71', u'Pugna': u'87', u'Tinker': u'68', u'Ancient Apparition': u'92', u'Omniknight': u'8', u'Chaos Knight': u'27', u'Outworld Devourer': u'94', u'Abaddon': u'102', u'Faceless Void': u'50', u'Mirana': u'33', u'Bristleback': u'99', u'Elder Titan': u'101', u'Windrunner': u'64', u'Slardar': u'19', u'Shadow Fiend': u'47', u'Templar Assassin': u'39', u'Shadow Demon': u'95', u'Anti-Mage': u'30', u'Keeper of the Light': u'77', u'Necrophos': u'83', u'Lina': u'66', u'Medusa': u'60', u'Lone Druid': u'44', u'Phantom Lancer': u'35', u'Witch Doctor': u'81', u'Riki': u'37', u'Invoker': u'93', u'Sniper': u'38', u'Meepo': u'57', u'Leshrac': u'89', u'Zeus': u'65', u'Silencer': u'73', u'Broodmother': u'54', u'Enigma': u'82', u'Doom': u'24', u'Techies': u'108', u'Bane': u'78', u'Alchemist': u'10', u'Batrider': u'91', u'Brewmaster': u'11', u'Axe': u'16', u'Skywrath Mage': u'100', u'Clinkz': u'53', u'Venomancer': u'49', u'Morphling': u'34', u'Death Prophet': u'86', u'Lion': u'80', u'Ogre Magi': u'74', u'Dazzle': u'88', u'Magnus': u'29', u'Earth Spirit': u'103', u'Pudge': u'17', u'Storm Spirit': u'63', u"Nature's Prophet": u'69', u'Warlock': u'84', u'Spirit Breaker': u'25', u'Crystal Maiden': u'61', u'Sven': u'2', u'Huskar': u'9', u'Shadow Shaman': u'67', u'Lich': u'79', u'Sand King': u'18', u'Dark Seer': u'90', u'Lifestealer': u'22', u'Clockwerk': u'7', u'Tiny': u'3', u'Oracle': u'109', u'Enchantress': u'70', u'Earthshaker': u'1', u'Puck': u'62', u'Nyx Assassin': u'58', u'Bounty Hunter': u'41', u'Luna': u'40', u'Centaur Warrunner': u'14', u'Disruptor': u'76', u'Timbersaw': u'15', u'Queen of Pain': u'85', u'Viper': u'52', u'Tusk': u'98', u'Lycan': u'26', u'Winter Wyvern': u'110', u'Phoenix': u'107', u'Beastmaster': u'5', u'Bloodseeker': u'46', u'Gyrocopter': u'43', u'Drow Ranger': u'31', u'Vengeful Spirit': u'36', u'Phantom Assassin': u'51', u'Terrorblade': u'106', u'Spectre': u'56', u'Kunkka': u'4', u'Slark': u'59', u'Weaver': u'55', u'Troll Warlord': u'97', u'Treant Protector': u'12', u'Visage': u'96', u'Ember Spirit': u'104', u'Arc Warden': u'111', u'Legion Commander': u'105', u'Wraith King': u'21', u'Tidehunter': u'20', u'Io': u'13', u'Chen': u'72', u'Rubick': u'75'}

class Build():
	#skills_list e.g. [4,4,4,4,5] @ level 21
	def __init__(self, hero_name, level, skills_list):
		self.int 
		self.str
		self.agi
		self.base_damage
		self.raw_damage
		self.armor
		self.attack_speed
		self.magic_resistance

		self.level = level

		all_hero_data = json.load(open(DATA_FOLDER_PATH, "rb"))
		self.hero_data = all_hero_data[HERO_NUMS[hero_name]]

		self.int = self.hero_data["BaseInt"] + self.hero_data["IntGain"]*(level-1)
		self.str = self.hero_data["BaseStr"] + self.hero_data["StrGain"]*(level-1)
		self.agi = self.hero_data["BaseAgi"] + self.hero_data["AgiGain"]*(level-1)

		self.hp = self.get_hp()
		self.attack_speed = self.get_attack_speed()
		self.attacks_per_second = self.get aps()
		self.armor = self.get_armor()
		self.mana = self.get_mana()


		self.skills_list = skills_list
		if sum(skills_list) > level:
			raise exception
		for i in range(len(skills_list)):
			if i < 3 and 2*(skills_list[i]-1)+1 > level:
				print "Invalid skill distribution"
				raise Exception
			if len(skills_list) < 4: 
				print "Not enough skills"
				raise Exception
			if len(skills_list) > 5:
				print "Too many skills"
				raise Exception
			if len(skills_list) == 4:
				skills_list.append(level-sum(skills_list))


	def get_hp(self):
		pass
	def get_attack_speed(self):
		pass
	def get_aps(self):
		pass
	def get_armor(self):
		pass
	def get_mana(self):
		pass

	# adds an item to the hero's build
	def add_item(self, item_name):
		pass
	#gets the stat of the hero by the name of the stat e.g. "damage"
	def get_stats(self, stat_name):
		return self.hero_data[stat_name]
	#other_hero is another Build
	def fights(self, other_hero):



