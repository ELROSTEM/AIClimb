import random
import math
from numpy.random import randint

# Useful for whole program:

alphabet = [*"abcdefghijklmnopqrstuvwxyz"]

alkyl_groups = ["methyl", "ethyl", "propyl", "isopropyl", "butyl", "t-butyl", "s-butyl", "isobutyl"]

alkyl_groups_dict = { "methyl": "m", "ethyl": "e", "propyl": "p", "isopropyl": "i", "butyl": "b", "t-butyl": "b", "s-butyl": "b", "isobutyl": "i" }

exo_groups = ["methylene", "vinyl", "allyl"]

exo_groups_dict = { "methylene": "m", "vinyl": "v", "allyl": "a" }

alkene_prefixes = ["prop", "but", "pent", "hex", "hept", "oct"]

class cycloalkene:

    def __init__(self, prefix, group, length, endex, locale, nulocale):

        self.prefix = prefix
        #print(self.prefix)
        self.group = group
        #print(self.group)
        self.length = length
        #print(self.length)
        self.endex = endex
        #print(self.endex)
        self.locale = locale
        #print(self.locale)
        self.nulocale = nulocale

    def iupac_name(self):

        if self.endex == "exo":
                
            return f"{self.locale[0]}-{self.group[0]}-{self.locale[1]}-{self.group[1]} cyclo{self.prefix}ane"

        if self.endex == "end":
        
            return f"{self.locale[0]}-{self.group[0]} cyclo{self.prefix}ene"

def cyclogen(end_exo):

    prfx = random.choice(alkene_prefixes)
    leng = alkene_prefixes.index(prfx) + 3

    if end_exo == "end":
        grp = [random.choice(alkyl_groups)]
        alkyl_location = randint(1, math.ceil(float(leng)/2)+2)
        while alkyl_location == 2:
            alkyl_location = randint(1, math.ceil(float(leng)/2)+2)

        locale = [alkyl_location]
        nulocale = [alkyl_location]

    if end_exo == "exo":
        grp = [random.choice(exo_groups), random.choice(alkyl_groups)]
        if grp[0] == "methylene":
            alkyl_location = randint(2, math.ceil(float(leng)/2)+2)
        else:
            alkyl_location = randint(1, math.ceil(float(leng)/2)+2)

        if alphabet.index(alkyl_groups_dict[grp[1]]) > alphabet.index(exo_groups_dict[grp[0]]):
                
            locale = [1, alkyl_location]
            nulocale = alkyl_location

        if alphabet.index(exo_groups_dict[grp[0]]) >= alphabet.index(alkyl_groups_dict[grp[1]]):

            grp = [grp[1], grp[0]]
            locale = [alkyl_location, 1]
            nulocale = alkyl_location

    return cycloalkene(prfx, grp, leng, end_exo, locale, nulocale)


if __name__ == "__main__":

    #for i in range(100):
    #    cyclo1 = cyclogen("end")
    #    print("#", cyclo1.iupac_name())
    for i in range(10):
        cyclo1 = cyclogen("exo")
        print("#", cyclo1.iupac_name()) 
