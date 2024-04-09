import CycloalkeneGeneration as c

end_exo = input("Endocyclic or Exocyclic? ")[0:3].lower()

conversion = { "allyl": "propyl", "methylene": "methyl", "vinyl": "ethyl" }

def Hydrogenation(molecule):

    if type(molecule) is c.cycloalkene:

        if molecule.endex == "exo":

            group = [conversion[x] if x in conversion.keys() else x for x in molecule.group]

            if c.alphabet.index(c.alkyl_groups_dict[group[1]]) > c.alphabet.index(c.alkyl_groups_dict[group[0]]):
                return f"1-{group[0]}-{molecule.nulocale}-{group[1]} cyclo{molecule.prefix}ane"
            
            if c.alphabet.index(c.alkyl_groups_dict[group[0]]) > c.alphabet.index(c.alkyl_groups_dict[group[1]]):
                return f"1-{group[1]}-{molecule.nulocale}-{group[0]} cyclo{molecule.prefix}ane"
            
            if c.alphabet.index(c.alkyl_groups_dict[group[0]]) == c.alphabet.index(c.alkyl_groups_dict[group[1]]):

                if group[0] == group [1]:
                    return f"1,{molecule.nulocale}-di{group[1]} cyclo{molecule.prefix}ane"

                else: 
                    return f"1-{group[0]}-{molecule.nulocale}-{group[1]} cyclo{molecule.prefix}ane"
                
        if molecule.endex == "end":

            return f"1-{molecule.group[0]} cyclo{molecule.prefix}ane"



for i in range(50):
    cycl = c.cyclogen(end_exo)
    print(cycl.iupac_name())
    print(Hydrogenation(cycl))
    print("..\n..\n..")


# EXO Hydrogenation Examples: 
# 1-allyl-1-isopropyl cyclopropane -> 1-isopropyl-1-propyl cyclopropane
# 1-ethyl-1-vinyl cycloheptane -> 1,1-diethyl cycloheptane
# 1-allyl-2-propyl cycloheptane -> 1,2-dipropyl cycloheptane
# 2-isobutyl-1-methylene cyclopentane -> 1-isobutyl-2-methyl cyclopentane
# 2-isobutyl-1-methylene cyclopropane -> 1-isobutyl-2-methyl cyclopropane
# 2-methyl-1-methylene cyclopropane -> 1,2-dimethyl cyclopropane
# 1-allyl-2-butyl cyclohexane
# 2-propyl-1-vinyl cyclohexane
# 4-isopropyl-1-methylene cycloheptane
# 1-allyl-2-ethyl cyclopropane

# ENDO Hydrogenation Examples:
# 3-methyl cyclopentene
# 1-methyl cyclohexene
# 1-t-butyl cyclooctene
# 1-butyl cyclobutene
# 1-s-butyl cyclopropene
# 3-propyl cyclopentene
# 1-methyl cyclobutene
# 3-propyl cyclohexene
# 3-propyl cyclopentene
# 1-butyl cyclooctene