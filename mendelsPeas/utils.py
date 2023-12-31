from random import choice, shuffle

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
            if p1.phenotype.isupper():
                self.parents = [p1, p2]
            else:
                self.parents = [p2, p1]
        else:
            raise ValueError("Invalid input. Please provide either a string or two Plant instances.")

        #sorted(self.parents)
        self.genotype.sort()
        self.phenotype = self.genotype[0]

    def getGenotype(self):
        return ''.join(self.genotype)

    def getPhenotype(self):
        return self.phenotype

    def breed(self, plant, trait='1', N=100):
        newPop = []
        for i in range(N):
            newPop.append(Plant(self, plant))

        return Population(newPop, trait) # This is awkward, because I made trait a population-level attribute

class Population:
    def __init__(self, plants='', trait='1'):
        if plants == '':
            self.plants = []
        elif all(isinstance(arg, Plant) for arg in plants):
                self.plants = plants
        else:
            raise ValueError("Invalid input. Please provide either no inputs or a list of Plants.")

        traitDict = {'1': ['yellow', 'green'],
                     '2': ['round', 'wrinkled'],
                     '3': ['purple', 'white'],
                     '4': ['yellow', 'green'],
                     '5': ['inflated', 'constricted'],
                     '6': ['axial', 'terminal']}
        self.traits = trait

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

    def breedRandomPairs(self, N=100):
        p1, p2 = self.plants.copy(), self.plants.copy()
        newPop = []
        for i in range(N):
            newPop.append(Plant(choice(p1), choice(p2)))

        return Population(newPop, self.traits)

    def breedWithPop(self, population, N=100):
        p1, p2 = self.plants.copy(), population.plants.copy()
        newPop = []
        for i in range(N):
            newPop.append(Plant(choice(p1), choice(p2)))

        return Population(newPop, self.traits)

    def breedWithOne(self, plant, N=100):
        p1 = self.plants.copy()
        newPop = []
        for i in range(N):
            newPop.append(Plant(choice(p1), plant))

        return Population(newPop, self.traits)

    def breedFilter(self, filterType='A', N=100):
        plants = [self.plants[i] for i in self.filter(filterType)]
        newPop = []
        for i in range(N):
            newPop.append(Plant(choice(plants), choice(plants)))
        return Population(newPop, self.traits)

    def filter(self, filterType='A'):
        phenos = [plant.phenotype for plant in self.plants]
        if len(filterType) > 1:
            p1Phenos = [plant.parents[0].phenotype for plant in self.plants]
            p2Phenos = [plant.parents[1].phenotype for plant in self.plants]
            fullPhenos = [p + p1 + p2 for p, p1, p2 in zip(phenos, p1Phenos, p2Phenos)]
        if filterType == 'A':
            return [index for index, letter in enumerate(phenos) if letter.isupper()]
        elif filterType == 'a':
            return [index for index, letter in enumerate(phenos) if letter.islower()]
        elif filterType == 'AAA':
            return [index for index, letter in enumerate(fullPhenos) if letter.isupper()]
        elif filterType == 'aaa':
            return [index for index, letter in enumerate(fullPhenos) if letter.islower()]

    def phenoSummary(self):
        phenos = [plant.phenotype for plant in self.plants]

        item_counts = {}
        # Count occurrences of each item in the list
        for item in phenos:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1
        item_counts = dict(sorted(item_counts.items()))

        print('Pop. {} summary:'.format(self.name))
        # Print the counts of unique items
        for item, count in item_counts.items():
            print(f"{item}: {count}")

    def fullSummary(self):
        phenos = [plant.phenotype for plant in self.plants]
        p1Phenos = [plant.parents[0].phenotype for plant in self.plants]
        p2Phenos = [plant.parents[1].phenotype for plant in self.plants]
        i = 0
        for p1, p2 in zip(p1Phenos, p2Phenos):
            if p1 > p2:
                p1Phenos[i], p2Phenos[i] = p2Phenos[i], p1Phenos[i]
            i += 1
        fullPhenos = [p + p1 + p2 for p, p1, p2 in zip(phenos, p1Phenos, p2Phenos)]

        item_counts = {}
        # Count occurrences of each item in the list
        for item in fullPhenos:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1
        item_counts = dict(sorted(item_counts.items()))

        print('Pop. {} summary:'.format(self.name))
        # Print the counts of unique items
        for item, count in item_counts.items():
            print(f"{item}: {count}")

    def list(self):
        name = self.name
        for i, plant in enumerate(self.plants):
            print('{}.{}: {} ({}/{})'.format(name, i, plant.phenotype, plant.parents[0].phenotype, plant.parents[1].phenotype))
