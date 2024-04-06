import random
import math
from numpy.random import randint

# Useful for whole program:

alphabet = [*"abcdefghijklmnopqrstuvwxyz"]

alkyl_groups = ["methyl", "ethyl", "propyl", "isopropyl", "butyl", "t-butyl", "s-butyl", "isobutyl"]

exo_groups = ["methylene", "vinyl", "allyl"]

alkene_prefixes = ["prop", "but", "pent", "hex", "hept", "oct"]

class cycloalkene:

    def __init__(self, prefix, group, length):

        self.prefix = prefix
        self.group = group
        self.length = length

    def iupac_name(self):

        if type(self.group) is list:

            if alphabet.index([*self.group[0]][0]) > alphabet.index([*self.group[1]][0]):

                exo_location = randint(1, math.ceil(self.length/2 + 1))
                alkyl_location = 1
                
                name = f"{alkyl_location}-{self.group[1]}-{exo_location}-{self.group[0]} cyclo{self.prefix}ane"

            if alphabet.index([*self.group[1]][0]) > alphabet.index([*self.group[0]][0]):

                exo_location = 1
                alkyl_location = randint(1, math.ceil(self.length/2 + 1))
                
                name = f"{exo_location}-{self.group[0]}-{alkyl_location}-{self.group[1]} cyclo{self.prefix}ane"

        if self.group in alkyl_groups:

            alkyl_location = randint(1, math.ceil(self.length/2 + 1))
            while alkyl_location == 2:
                alkyl_location = randint(1, math.ceil(self.length/2 + 1))
        
            name = f"{alkyl_location}-{self.group} cyclo{self.prefix}ene"

        return name

def cyclogen(endo_exo):

    prfx = random.choice(alkene_prefixes)
    if endo_exo == "endo":
        grp = random.choice(alkyl_groups)
    if endo_exo == "exo":
        grp = [random.choice(exo_groups), random.choice(alkyl_groups)]
    leng = alkene_prefixes.index(prfx) + 3

    return cycloalkene(prfx, grp, leng)

# EXOCYCLIC CYCLOALKENE
cyclo1 = cyclogen("exo")
print(cyclo1.prefix)
print(cyclo1.group)
print(cyclo1.length)
print("Random Cycloalkene with Correct IUPAC Nomenclature:", cyclo1.iupac_name())

# ENDOCYCLIC CYCLOALKENE
cyclo2 = cyclogen("endo")
print(cyclo2.prefix)
print(cyclo2.group)
print(cyclo2.length)
print("Random Cycloalkene with Correct IUPAC Nomenclature:", cyclo2.iupac_name())

