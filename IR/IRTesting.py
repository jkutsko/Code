from build import Build
from item import Item
import combat
import matplotlib.pyplot as plt 



antimage = Build("Anti-Mage", 16, [4,4,4,3,1])
print antimage.get_base_damage()
print antimage.get_total_damage()
antimage.add_item_by_name("Monkey King Bar")
antimage.add_item_by_name("Demon Edge")

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

dictionary = plt.figure()
plt.bar(range(len(D)), map(lambda k: k/1000.0,D.values()), align='center')
plt.xticks(range(len(D)), D.keys())
plt.ylabel("Frequency")
plt.xlabel("Number of Attacks")
plt.title("Attacks it takes for Antimage to kill Lion")
plt.show()

