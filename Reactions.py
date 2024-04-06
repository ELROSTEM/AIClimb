import CycloalkeneGeneration as c

while 2 == 2:
    endo_exo = input("Endocyclic or Exocyclic? ")
    molecule = c.cyclogen(endo_exo)
    print(molecule.iupac_name())

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