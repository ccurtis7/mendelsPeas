from random import choice

class Plant:
    def __init__(self, *args):
        if (len(args) == 1) & isinstance(args[0], str):
            # If only on instance, manually define genotype
            self.genotype = list(args[0])
            self.parents = ['', '']
        elif (len(args) == 2) & all(isinstance(arg, Plant) for arg in args):
            # all inputs are Plants
            p1, p2 = args[0], args[1]
            self.genotype = [choice(p1.genotype), choice(p2.genotype)]
            self.parents = [p1, p2]
        else:
            raise ValueError("Invalid input. Please provide either a string or two Plant instances.")

        #sorted(self.parents)
        self.genotype.sort()
        self.phenotype = self.genotype[0]

    def getGenotype(self):
        return ''.join(self.genotype)

    def getPhenotype(self):
        return self.phenotype

class Population:
    def __init__(self, plants=''):
        if plants == '':
            self.plants = []
        elif all(isinstance(arg, Plant) for arg in plants):
                self.plants = plants
        else:
            raise ValueError("Invalid input. Please provide either no inputs or a list of Plants.")

    def tag(self, name, note):
        '''
        Add metadata including the name of the population and
        any notes you would like to add.
        '''
        self.name = name
        self.note = note

    def genRandomPop(self, N=100, pattern=['Gg', 'GG', 'gg']):
        '''
        Generate a random population of size N from the template genotypes pattern.
        '''
        self.plants = [Plant(choice(pattern)) for i in range(N)]

    def breedRandomPairs(self):
        p1, p2 = self.plants.copy(), self.plants.copy()
        shuffle(p1), shuffle(p2)
        newPop = []
        for plant1, plant2 in zip(p1, p2):
            newPop.append(Plant(plant1, plant2))

        return Population(newPop)

    def phenoSummary(self):
        phenos = [plant.phenotype for plant in self.plants]

        item_counts = {}
        # Count occurrences of each item in the list
        for item in phenos:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1

        print('Population summary:')
        # Print the counts of unique items
        for item, count in item_counts.items():
            print(f"{item}: {count}")
