from utils import *
from random import choice

def main():
    print('Example program: ')
    plants = Population()
    plants.genRandomPop()
    plants.phenoSummary()

if __name__ == '__main__':
    main()
