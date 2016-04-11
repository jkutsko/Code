from build import Build
from item import Item
import combat
import matplotlib.pyplot as plt 



antimage = Build("Anti-Mage", 25, [4,4,4,3])
print antimage.get_base_damage()
print antimage.get_total_damage()
antimage.add_item_by_name("Monkey King Bar")
antimage.add_item_by_name("Demon Edge")
antimage.add_item_by_name("Butterfly")
antimage.add_item_by_name("Crystalys")

print antimage.get_base_damage()
print antimage.get_total_damage()


poor_little_lion = Build("Lion", 16, [4,4,4,3,1])
print combat.calculate_damage(antimage, poor_little_lion)
print combat.calculate_damage(antimage, antimage)

#stop hitting yourself
print combat.calculate_average_damage(antimage, antimage)
# should be different from the above version.

print combat.calculate_average_damage(poor_little_lion, antimage)
D =  combat.calculate_hits_to_kill(antimage, poor_little_lion)
print combat.calculate_hits_to_kill(antimage, antimage)

