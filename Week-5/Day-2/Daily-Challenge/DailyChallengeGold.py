# Instructions :
# This challenge is about Biology that will put emphasis on your knowledge of classes, inheritance and polymorphism.

# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
# A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.

# Implement these classes as you see fit.

# Create a new class called Organism that accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.

# Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s. Then stop and record the number of generations (iterations) it took.

import random
from typing import Optional

Zero_One = [0,1]

class Gene:
    def __init__(self):
        self.val = random.choice(Zero_One)

    def __flip(self):
        self.val = 1 - self.val
    
    def mutate(self):
        self.__flip()

    def __str__(self) -> str:
        return str(self.val)

class Chromosome:
    def __init__(self):
        self.genes = [Gene() for i in range(10)]

    def mutate(self, threshold: int):
        for gene in self.genes:
            random_int = random.randint(0, 101)
            if threshold <= random_int:
                gene.mutate()

    def __str__(self) -> str:
        output ="|".join(list(map(str, self.genes)))
        # for gene in self.genes:
        #     output += str(gene) + '\n'
        return(output)

chromo = Chromosome()
print(chromo)



class DNA:
    def __init__(self) -> object:
        self.chromosomes = [Chromosome() for i in range(10)]

    def mutate(self, threshold: int):
        for gene in self.genes:
            random_int = random.randint(0, 101)
            if threshold <= random_int:
                gene.mutate()

    def __str__(self) -> str:
        output ="|".join(list(map(str, self.genes)))
        # for gene in self.genes:
        #     output += str(gene) + '\n'
        return(output)

class Organism:

    def __init__(self, DNA) -> None:
        pass