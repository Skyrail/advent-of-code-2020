import os, sys
from copy import deepcopy
import time

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        currentBatch = file.read().strip().split('\n')
        currentBatch = [list(x) for x in currentBatch]

        maxRow = len(currentBatch)
        maxCol = len(currentBatch[0])

        while True:

            hasChanged = False
            previousBatch = deepcopy(currentBatch)

            for row in range(maxRow):
                for col in range(maxCol): 
                    element = previousBatch[row][col]

                    occupiedCount = 0

                    for ri in (-1, 0, 1):
                        for ci in (-1, 0, 1):

                            if (ri == 0 and ci == 0):
                                continue

                            rowIndex = row + ri
                            colIndex = col + ci
                                
                            while (0 <= rowIndex < maxRow) and (0 <= colIndex < maxCol) and (previousBatch[rowIndex][colIndex] == '.'):
                                rowIndex += ri
                                colIndex += ci

                            if (0 <= rowIndex < maxRow) and (0 <= colIndex < maxCol) and previousBatch[rowIndex][colIndex] == '#':
                                occupiedCount += 1
                                
                    if element == '#' and occupiedCount >= 5:
                        currentBatch[row][col] = 'L'
                        hasChanged = True
                    elif element == 'L' and occupiedCount == 0:
                        currentBatch[row][col] = '#'
                        hasChanged = True

            if hasChanged == False:
                break

        finalString = ("".join(["".join(x) for x in currentBatch])).count('#')

        print(f'The number of occupied seats is: {finalString}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')