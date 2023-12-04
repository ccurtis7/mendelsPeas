from utils import *
from interface import *

def startingPop():
    plants = Population()

    plants.genRandomPop()
    plants.tag('N1', 'Imaginary starting population')
    plants.phenoSummary()
    generations = {'N1': plants}

    plants = plants.breedRandomPairs()
    plants.tag('0', 'Starting population')
    plants.phenoSummary()
    generations['0'] = plants

    return generations

def main():
    generations = startingPop()
    printIntro()
    trait = getTrait()
    printInstructions()
    while True:
        command = getCommand(generations)
        simType = command.getsimType()

        if simType == 'quit':
            break
        elif simType == 'list':
            print('Existing populations include: ')
            for key, gen in generations.items():
                print('   {}: {}'.format(key, gen.note))
            continue # skip to next round, don't do anything else
        elif simType == 'P1list':
            print('tbd')
            continue
        elif simType == 'P1sum':
            p1 = generations[command.P1]
            p1.phenoSummary()
            continue
        elif simType == 'P1full':
            p1 = generations[command.P1]
            p1.fullSummary()
            continue
        elif simType == 'P1onP1':
            p1 = generations[command.P1]
            newP = p1.breedRandomPairs(N=command.N)
        elif simType == 'P1onP2':
            p1, p2 = generations[command.P1], generations[command.P2]
            newP = p1.breedWithPop(p2, N=command.N)
        elif simType == 'x1onP1':
            x1, p1 = generations[command.x1], generations[command.P1]
            px, idx = x1.split('.')
            idx = int(idx)
            newP = p1.breedWithOne(px.plants[idx], N=command.N)
        elif simType == 'x1onx2':
            x1name, x2name = generations[command.x1], generations[command.x2]
            px1, idx1 = x1name.split('.')
            px2, idx2 = x2name.split('.')
            x1, x2 = px1[idx1], px2[idx2]
            newP = x1.breed(x2, N=command.N)
        elif filter != None:
            p1 = generations[command.P1]
            # Right now 1/2 are assumed to correspond to dom/rec, which isn't necessarily the case. Need to fix this in the future. Look up which is which
            fTypes = {'1': 'A', '2': 'a', '111': 'AAA', '222': 'aaa'}
            filter = fTypes[command.getFilter()]
            newP = p1.breedFilter(filterType=filter, N=command.N)

        print('Please enter the name of the new population and any notes you would like to add: ')
        name = input('    name: ')
        note = input('    notes: ')
        newP.tag(name, note)
        generations[name] = newP
        print()


    print('Thank you for playing.')


if __name__ == '__main__':
    main()
