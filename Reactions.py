import CycloalkeneGeneration as c

endo_exo = input("Endocyclic or Exocyclic? ")
molecule = c.cyclogen(endo_exo)
print(molecule.iupac_name())

# EXO Examples: 1-isobutyl-4-methylene cyclooctane -> 1-isobutyl-4-methyl cyclooctane
#               1-t-butyl-3-vinyl cycloheptane -> 1-ethyl-3-t-butyl cycloheptane
#               1-allyl-1-ethyl cyclooctane -> 1-ethyl-1-propyl cyclooctane


# ENDO Examples: 1-t-butyl cyclobutene
#                3-propyl cyclopentene
#                4-ethyl cyclooctene