import random
import math
from numpy.random import randint

def generate_cycloalkene():
    # Define lists of prefixes for different alkyl groups
    alkyl_groups = ["methyl", "ethyl", "propyl", "isopropyl", "butyl", "t-butyl", "s-butyl", "isobutyl"]
    
    # Define list of cycloalkene prefixes
    cycloalkene_prefixes = ["prop", "but", "pent", "hex", "hept", "oct"]
    
    # Randomly select an alkyl group to attach to the cycloalkene ring
    alkyl_group = random.choice(alkyl_groups)
    
    # Randomly select a cycloalkene prefix
    prefix = random.choice(cycloalkene_prefixes)

    # Determine length of ring
    num_carbons = cycloalkene_prefixes.index(prefix) + 3
    alkyl_location = randint(1, math.ceil(num_carbons/2 + 1))
    if alkyl_location == 2:
        while alkyl_location == 2:
            alkyl_location = randint(1, math.ceil(num_carbons/2 + 1))
        
    
    # Construct the IUPAC name
    iupac_name = f"{alkyl_location}-{alkyl_group} cyclo{prefix}ene"
    
    return iupac_name

if __name__ == "__main__":
    cycloalkene = generate_cycloalkene()
    print("Random Cycloalkene with Correct IUPAC Nomenclature:", cycloalkene)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Method to insert a new node at the end of the linked list
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Method to display the circular linked list
    def display(self):
        if not self.head:
            print("Circular Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

size = int(input("Size of ring "))

if __name__ == "__main__":
    cycloalkene = CircularLinkedList()

    # Inserting elements into the circular linked list to represent cyclobutene
    for n in range(size):
        cycloalkene.insert("C"+str(n+1))  # Represents first carbon atom

    # Displaying the circular linked list representing cyclobutene
    print("Circular Linked List representing cycloalkene", end=" ")
    cycloalkene.display()

