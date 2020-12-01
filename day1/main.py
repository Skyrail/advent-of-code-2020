import os, sys  
from itertools import combinations
from functools import reduce

if len(sys.argv) != 2:
    raise ValueError('Please supply the intcode to be processed')

inputPath = sys.argv[1]

def findExpensesThatEqual(expenses, result, count):
    combos = combinations(expenses, count)

    for combo in combos:
        if sum(combo) == result:
            return combo

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