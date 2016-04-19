import os
from item import Item, Item_Build
import combat
import json

DATA_FOLDER_PATH = "data/hero_data.json"

PRIMARY_STATS = {0:"str",1:"agi",2:"int"}
HERO_NUMS = {u'Razor': u'48', u'Night Stalker': u'23', u'Naga Siren': u'45', u'Undying': u'28', u'Dragon Knight': u'6', u'Juggernaut': u'32', u'Ursa': u'42', u'Jakiro': u'71', u'Pugna': u'87', u'Tinker': u'68', u'Ancient Apparition': u'92', u'Omniknight': u'8', u'Chaos Knight': u'27', u'Outworld Devourer': u'94', u'Abaddon': u'102', u'Faceless Void': u'50', u'Mirana': u'33', u'Bristleback': u'99', u'Elder Titan': u'101', u'Windrunner': u'64', u'Slardar': u'19', u'Shadow Fiend': u'47', u'Templar Assassin': u'39', u'Shadow Demon': u'95', u'Anti-Mage': u'30', u'Keeper of the Light': u'77', u'Necrophos': u'83', u'Lina': u'66', u'Medusa': u'60', u'Lone Druid': u'44', u'Phantom Lancer': u'35', u'Witch Doctor': u'81', u'Riki': u'37', u'Invoker': u'93', u'Sniper': u'38', u'Meepo': u'57', u'Leshrac': u'89', u'Zeus': u'65', u'Silencer': u'73', u'Broodmother': u'54', u'Enigma': u'82', u'Doom': u'24', u'Techies': u'108', u'Bane': u'78', u'Alchemist': u'10', u'Batrider': u'91', u'Brewmaster': u'11', u'Axe': u'16', u'Skywrath Mage': u'100', u'Clinkz': u'53', u'Venomancer': u'49', u'Morphling': u'34', u'Death Prophet': u'86', u'Lion': u'80', u'Ogre Magi': u'74', u'Dazzle': u'88', u'Magnus': u'29', u'Earth Spirit': u'103', u'Pudge': u'17', u'Storm Spirit': u'63', u"Nature's Prophet": u'69', u'Warlock': u'84', u'Spirit Breaker': u'25', u'Crystal Maiden': u'61', u'Sven': u'2', u'Huskar': u'9', u'Shadow Shaman': u'67', u'Lich': u'79', u'Sand King': u'18', u'Dark Seer': u'90', u'Lifestealer': u'22', u'Clockwerk': u'7', u'Tiny': u'3', u'Oracle': u'109', u'Enchantress': u'70', u'Earthshaker': u'1', u'Puck': u'62', u'Nyx Assassin': u'58', u'Bounty Hunter': u'41', u'Luna': u'40', u'Centaur Warrunner': u'14', u'Disruptor': u'76', u'Timbersaw': u'15', u'Queen of Pain': u'85', u'Viper': u'52', u'Tusk': u'98', u'Lycan': u'26', u'Winter Wyvern': u'110', u'Phoenix': u'107', u'Beastmaster': u'5', u'Bloodseeker': u'46', u'Gyrocopter': u'43', u'Drow Ranger': u'31', u'Vengeful Spirit': u'36', u'Phantom Assassin': u'51', u'Terrorblade': u'106', u'Spectre': u'56', u'Kunkka': u'4', u'Slark': u'59', u'Weaver': u'55', u'Troll Warlord': u'97', u'Treant Protector': u'12', u'Visage': u'96', u'Ember Spirit': u'104', u'Arc Warden': u'111', u'Legion Commander': u'105', u'Wraith King': u'21', u'Tidehunter': u'20', u'Io': u'13', u'Chen': u'72', u'Rubick': u'75'}

class Build(object):
    #skills_list e.g. [4,4,4,3,6] @ level 21
    def __init__(self, hero_name, level, skills_list = []):
        self.name = hero_name
        self.plus_mana = 0
        self.plus_hp = 0
        self.plus_armor = 0
        self.plus_attack_speed = 0
        self.plus_damage = 0
        self.item_build = None
        self.evasion = 0

        self.item_build = Item_Build([])

        self.level = level

        all_hero_data = json.load(open(DATA_FOLDER_PATH, "rb"))
        self.hero_data = all_hero_data[HERO_NUMS[hero_name]]

        self.int = self.hero_data["BaseInt"] + self.hero_data["IntGain"]*(level-1)
        self.str = self.hero_data["BaseStr"] + self.hero_data["StrGain"]*(level-1)
        self.agi = self.hero_data["BaseAgi"] + self.hero_data["AgiGain"]*(level-1)

        self.base_damage = self.get_base_damage() 
        self.hp = self.get_hp()
        self.attack_speed = self.get_attack_speed()
        self.attacks_per_second = self.get_aps()
        self.armor = self.get_armor()
        self.mana = self.get_mana()


        self.skills_list = skills_list
        if sum(skills_list) > level:
            raise exception
        for i in range(len(skills_list)):
            if i < 3 and 2*(skills_list[i]-1)+1 > level:
                print "Invalid skill distribution"
                raise Exception
            if i == 3:
                ult = skills_list[i]
                if ult*5+1 > level or ult > 3:
                    print "Invalid level for ultimate"
                    raise Exception
            if len(skills_list) < 4: 
                print "Not enough skills"
                raise Exception
            if len(skills_list) > 5:
                print "Too many skills"
                raise Exception
            if len(skills_list) == 4:
                skills_list.append(level-sum(skills_list))
    '''
    Stat Calculation Methods:
    These get basic stats on heroes based on the hero's items and base stats,
    using the in-game formulas
    '''
    def get_base_damage(self):
        if self.hero_data["PrimaryStat"] == 0:
            return (self.hero_data["MaxDmg"] + self.hero_data["MinDmg"])/2 + self.str
        if self.hero_data["PrimaryStat"] == 1:
            return (self.hero_data["MaxDmg"] + self.hero_data["MinDmg"])/2 + self.agi
        if self.hero_data["PrimaryStat"] == 2:
            return (self.hero_data["MaxDmg"] + self.hero_data["MinDmg"])/2 + self.int
    
    #each point of str gives 19 hp, and there's a flat base of 180
    def get_hp(self):
        return int(self.str)*19+180 + self.plus_hp
    
    # each point of agi gives 1 AS, and there's a cap of 500
    def get_attack_speed(self):
        return min(500, self.agi + self.plus_attack_speed)

    # attacks per second based on the in-game formula
    def get_aps(self):
        return (100 + self.get_attack_speed())*.01/self.hero_data["BaseAttackTime"]

    # each point of agi gives .14 armor
    def get_armor(self):
        return self.agi*.14+ self.plus_armor + self.hero_data["Armor"]

    # Each point of int gives 13 mana
    def get_mana(self):
        return 13 * self.int + self.plus_mana

    def get_total_damage(self):
        return self.get_base_damage() + self.plus_damage
    '''
    Item Methods.
    These allow you to give one item, or an entire
    pre-set item build to the hero.
    '''
    # Adds an entire set of items to the current build
    # Useful for giving the same pre-set item build multiple times
    def give_item_build(self, item_build):
        for item in item_build.items:
            self.add_item(item)


    # adds an item to the hero's build by the item name
    def add_item_by_name(self, item_name):
        item = Item(item_name)
        self.add_item(item)

    # Adds an item object to the current build 
    def add_item(self, item):
        self.item_build.add_item(item)
        self.agi += item.agi
        self.int += item.int
        self.str += item.str
        self.plus_damage += item.damage
        self.plus_armor += item.armor
        self.plus_attack_speed += item.attack_speed
        self.plus_hp += item.hp

    '''
    Catch-all access method for getting the original json data
    '''
    #gets the stat of the hero by the name of the stat e.g. "damage"
    def get_stats(self, stat_name):
        return self.hero_data[stat_name]
    



