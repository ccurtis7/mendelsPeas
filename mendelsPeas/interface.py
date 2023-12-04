def printIntro():
    print('Welcome to the Multivariate Experimental Network for Developmental Exploration in Legumes (M.E.N.D.E.L.)\n')
    print('You may simulate a series of pea plant breeding experiments focusing on a desired trait.')

def getTrait():
    print('Which trait would you like to simulate?')
    print('[1]: Seed color (yellow/green)')
    print('[2]: Seed shape (round/wrinkled)')
    print('[3]: Flower color (purple/white)')
    print('[4] Pod color (yellow/green)')
    print('[5]: Pod shape (inflated/constricted)')
    print('[6]: Flower position (axial/terminal)\n')

    while True:
        try:
            trait = int(input('Selection: '))
            if trait in range(1,7):
                print()
                return trait
            else:
                print('Not a valid input. Please enter an integer between 1 and 6.')
        except:
            print('Not a valid input. Please enter an integer between 1 and 6.')

def printInstructions():
    print('You may simulate one generation of pea plants from the starting population (Gen0) of 100 pea plants by using the following options: ')
    print('P1onP1: randomly pair pea plants in given population')
    print('   You may also apply one of the filters to only breed specific types of plants:')
    print('   1: only breed plants of the first kind e.g. round')
    print('   2: only breed plants of the second kind e.g. wrinkled')
    print('   111: only breed plants of the first kind that also have parents of the first kind')
    print('   222: only breed plants of the second kind that also have parents of the second kind')
    print('P1onP2: randomly pair pea plants from two populations')
    print('x1onP1: pollinate all plants in a given population with a single plant')
    print('x1onx2: create a new population from the offspring of two plants\n')
    print('A valid command would like like\n')
    print('P1onP1 Gen0 -N 100 -F 1\n')
    print('This command would breed random pairs in the Gen0 population creating a new population of size N=100 and only breeding plants of the first kind (e.g. round)')
    print('Filters only work for P1onP1 experiments. Flags (-N and -F) are optional. Default population size is 100.')

class Command:
    def __init__(self, simType=None, names=None, N=100, filter=None):
        self.simType = simType
        self.P1, self.P2, self.x1, self.x2 = names
        self.N = N
        self.filter = filter

    def getsimType(self):
        return self.simType

    def getName(self):
        if self.simType == 'P1onP1':
            return self.P1
        elif self.simType == 'P1onP2':
            return [self.P1, self.P2]
        elif self.simType == 'x1onP1':
            return [self.x1, self.P1]
        elif self.simType == 'x1onx2':
            return [self.x1, self.x2]

    def getN(self):
        return self.N

    def getFilter(self):
        return self.filter

def getCommand(generations):
    filter, N = None, 100
    P1, P2, x1, x2 = None, None, None, None
    while True:
        print('Please enter a command: ')
        comm = input('> ')
        parts = comm.strip().split(' ')
        if len(parts) < 2:
            print('Not enough arguments. Please enter sim type, pop name, (pop. size), (filter)')
            continue

        # Make sure the simType is correct
        simType = parts[0]
        types = ['P1onP1', 'P1onP2', 'x1onP1', 'x1onx2']
        if simType not in types:
            print('Please use a valid simulation type: {}'.format(', '.join(types)))
            continue

        # Make sure any names are correct
        names = [pop.name for pop in generations]
        names.append(None)
        if simType == 'P1onP1':
            P1 = parts[1]
        elif simType == 'P1onP2':
            P1, P2 = parts[1], parts[2]
        elif simType == 'x1onP1':
            x1, P1 = parts[1], parts[2]
            P2 = x1.split('.')[-1].strip()
        elif simType == 'x1onx2':
            x1, x2 = parts[1], parts[2]
            P1 = x1.split('.')[-1].strip()
            P2 = x2.split('.')[-1].strip()

        if (P1 not in names) | (P2 not in names):
            print('Please enter a valid population name.')
            continue

        # Make sure the sample size is correct
        if '-N' in parts:
            N = parts[parts.index('-N') + 1]
            try:
                N = int(N)
            except:
                print('N must be an integer.')
                continue

        # Make sure the filter is correct
        if '-F' in parts:
            filter = parts[parts.index('-F')+1]
            if (simType != 'P1onP1') & filter:
                print('Filter has not been applied, only valid for P1onP1 experiments')

            if filter not in ['1', '2', '111', '222']:
                print('Please enter a valid value for the filter')
                continue

        return Command(simType, [P1, P2, x1, x2], N, filter)
