from utils import *
from interface import *

def startingPop():
    plants = Population()

    plants.genRandomPop()
    plants.tag('N1', 'Imaginary starting population')
    plants.phenoSummary()
    generations = [plants]

    plants = plants.breedRandomPairs()
    plants.tag('0', 'Starting population')
    plants.phenoSummary()
    generations.append(plants)

    return generations

def main():
    generations = startingPop()
    printIntro()
    trait = getTrait()
    printInstructions()
    command = getCommand(generations)
    print(command.getsimType())


if __name__ == '__main__':
    main()
