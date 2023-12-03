from utils import *
from random import choice

def main():
    print('Example program: ')
    plants = Population()

    plants.genRandomPop()
    plants.tag('0', 'Starting population')
    plants.phenoSummary()
    generations = [plants]

    plants = plants.breedRandomPairs()
    plants.tag('1', '2nd gen, to get parents info')
    plants.phenoSummary()
    generations.append(plants)

    for i in range(10):
        plants = plants.breedFilter('aaa')
        plants.tag('{}'.format(i), '{}th generation'.format(i))
        print()
        plants.phenoSummary()
        generations.append(plants)

if __name__ == '__main__':
    main()
