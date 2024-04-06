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

    def __init__(self, prefix, group, length):

        self.prefix = prefix
        self.group = group
        self.length = length

    def iupac_name(self):

        if type(self.group) is list:

            exo_location = 1
            if self.group[0] == "methylene":
                alkyl_location = randint(2, math.ceil(self.length/2 + 1))
            else:
                alkyl_location = randint(1, math.ceil(self.length/2 + 1))

            if alphabet.index(exo_groups_dict[self.group[0]]) >= alphabet.index(alkyl_groups_dict[self.group[1]]):

                return f"{alkyl_location}-{self.group[1]}-{exo_location}-{self.group[0]} cyclo{self.prefix}ane"

            if alphabet.index(alkyl_groups_dict[self.group[1]]) > alphabet.index(exo_groups_dict[self.group[0]]):
                
                return f"{exo_location}-{self.group[0]}-{alkyl_location}-{self.group[1]} cyclo{self.prefix}ane"

        else:

            alkyl_location = randint(1, math.ceil(self.length/2 + 1))
            while alkyl_location == 2:
                alkyl_location = randint(1, math.ceil(self.length/2 + 1))
        
            return f"{alkyl_location}-{self.group} cyclo{self.prefix}ene"

def cyclogen(endo_exo):

    prfx = random.choice(alkene_prefixes)
    if endo_exo == "endo":
        grp = random.choice(alkyl_groups)
    if endo_exo == "exo":
        grp = [random.choice(exo_groups), random.choice(alkyl_groups)]
    leng = alkene_prefixes.index(prfx) + 3

    return cycloalkene(prfx, grp, leng)


if __name__ == "__main__":

    # EXOCYCLIC CYCLOALKENE
    for i in range(50):
        cyclo1 = cyclogen("endo")
        print("Random Cycloalkene with Correct IUPAC Nomenclature:", cyclo1.iupac_name())

    # ENDOCYCLIC CYCLOALKENE
    cyclo2 = cyclogen("endo")
    print(cyclo2.prefix)
    print(cyclo2.group)
    print(cyclo2.length)
    print("Random Cycloalkene with Correct IUPAC Nomenclature:", cyclo2.iupac_name())

