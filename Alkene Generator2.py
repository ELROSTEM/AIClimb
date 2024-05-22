import random
from numpy.random import randint
import turtle

#Definitions 

alphabet = [*"abcdefghijklmnopqrstuvwxyz"]

alkyl_groups = ["methyl", "ethyl", "propyl", "isopropyl", "butyl", "tert-butyl", "sec-butyl", "isobutyl"]

alkyl_groups_dict = {"methyl": "m", "ethyl": "e", "propyl": "p", "isopropyl": "ip", "butyl": "b", "tert-butyl": "bt", "sec-butyl": "bs", "isobutyl": "ib" }

alkyl_groups_min_dict = {"methyl":2, "ethyl":3, "propyl":4, "isopropyl":4, "butyl":5, "tert-butyl":5, "sec-butyl":5, "isobutyl":5}

exo_groups = ["methylene", "vinyl", "allyl"]

exo_groups_dict = { "methylene": "m", "vinyl": "v", "allyl": "a" }

alkene_prefixes = ["prop", "but", "pent", "hex", "hept", "oct"]

substituent_prefixes = ["di", "tri", "tetra"]

#Function

def alkenegen():

    #setup
    length = random.randint(3,8)
    prefix = alkene_prefixes[length - 3]
    double_bond_loc = random.randint(1, int((length) / 2))

    #substituent assignment
    subs = {}
    num_sub = random.randint(0,3)#   <-- change later
    for i in range(num_sub):
        sub = random.choice(alkyl_groups)
        min_sub_loc = alkyl_groups_min_dict[sub]
        max_sub_loc = length - min_sub_loc + 1
        if max_sub_loc < min_sub_loc:
            while max_sub_loc < min_sub_loc:
                sub = random.choice(alkyl_groups)#          <-- keep picking until it works
                min_sub_loc = alkyl_groups_min_dict[sub]
                max_sub_loc = length - min_sub_loc + 1
        if sub not in subs:
            subs[sub] = [(random.randint(min_sub_loc, max_sub_loc))] #       <-- make it so that it can take in multiple of the same substituents
        if sub in subs:
            if len(subs[sub]) < 2:
                subs[sub].append((random.randint(min_sub_loc, max_sub_loc)))
                subs[sub].sort()

    #double bond check
    sp2_carbon_1 = double_bond_loc
    sp2_carbon_2 = sp2_carbon_1 + 1

    count = 0
    for sub in subs: #    <-- list of all the substituent location numbers; check for sp2 carbon 1
        for index in range(len(subs[sub])):
            if subs[sub][index] == sp2_carbon_1 and count >= 1:
                count += 1
                subs[sub][index] = -1
            elif subs[sub][index] == sp2_carbon_1:
                count += 1

    count = 0
    for sub in subs: #    <-- list of all the substituent location numbers; check for sp2 carbon 1
        for index in range(len(subs[sub])):
            if subs[sub][index] == sp2_carbon_2 and count >= 1:
                count += 1
                subs[sub][index] = -1
            elif subs[sub][index] == sp2_carbon_2:
                count += 1

    #check for more than 2 per carbon
    for number in range(length):
        number += 1
        num_instances = 0
        for sub in subs:
            for item in range(len(subs[sub])):
                if subs[sub][item] == number:
                    num_instances += 1
                if num_instances > 1:
                    subs[sub][item] = -1

    #alphabatization
    keys = list(subs.keys())#   <-- list of names of groups
    keys2 = []
    for key in keys:
        keys2.append(alkyl_groups_dict[key])
    keys2.sort()#   <-- sorted, incomplete names
    alkyl_groups_dict_a = {alkyl_groups_dict[i]:i for i in alkyl_groups_dict}
    keys = []
    for key in keys2:
        keys.append(alkyl_groups_dict_a[key])
    subs2 = {i: subs[i] for i in keys}
    subs = subs2#       <-- sorted dictionary of all the substituents

    #removal of -1 list items
    for i in range(num_sub):
        for sub in subs:
            if -1 in subs[sub]:
                subs[sub].remove(-1)

    #prefix addition
    subs2 = {}
    for sub in subs:
        if len(subs[sub]) >= 2:
            subs2[str(substituent_prefixes[len(subs[sub]) - 2]) + str(sub)] = subs[sub]
        else:
            subs2[sub] = subs[sub]

    #naming
    iupac_name = "" 
    for sub in subs2:
        if not (subs2[sub] == []):
            for i in range(len(subs2[sub])):
                iupac_name += f"{subs2[sub][i]}"
                if (i + 1) != len(subs2[sub]):
                    iupac_name  += "," 
                else:
                    iupac_name += "-"
            iupac_name += f"{sub}-"
    iupac_name += f"{double_bond_loc}-{prefix}ene"

    #return
    return [iupac_name, subs, length]

def draw(alkene):
    turt = turtle.Turtle()
    length = alkene[2]
    subs = alkene[1]
    for i in range(length):
        if i == 0:
            turt.left(30)
        elif i % 2 == 0:
            turt.left(60)
        else:
            turt.right(60)
        turt.forward(30)
    


if __name__ == "__main__":
    myAlkene = alkenegen()
    print(myAlkene)
    draw(myAlkene)