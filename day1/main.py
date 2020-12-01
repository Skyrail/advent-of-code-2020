import os, sys  
from itertools import combinations
from functools import reduce

def findExpensesThatEqual(expenses, result, count):
    """ Takes a list of expenses, figures out which number of expenses (denoted by count) add up to equal result """
    combos = combinations(expenses, count)

    for combo in combos:
        if sum(combo) == result:
            return combo

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        expenses = list(map(int, file.read().split()))

        part1Combination = findExpensesThatEqual(expenses, 2020, 2)
        part2Combination = findExpensesThatEqual(expenses, 2020, 3)

        print(f'Part 1: {part1Combination} multiplied equals {reduce(lambda x,y: x*y, part1Combination)}')
        print(f'Part 2: {part2Combination} multiplied equals {reduce(lambda x,y: x*y, part2Combination)}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')