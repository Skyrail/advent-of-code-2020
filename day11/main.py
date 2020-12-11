import os, sys
import numpy as np

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

def replaceChars(string):
    """ 0 == empty seat, 1 == occupied seat, 2 == floor """
    stringList = list(string)

    stringList[:]  = [(lambda x: 0 if x == 'L' else 2)(x) for x in stringList]

    return stringList

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = file.read().strip().split('\n')

        previousBatch = np.array([])
        currentBatch = np.array([replaceChars(row) for row in batch])

        while np.array_equal(previousBatch, currentBatch) != True:

            previousBatch = currentBatch.copy()

            iterator = np.nditer(previousBatch, flags=['multi_index'])

            for element in iterator:
                row,col = iterator.multi_index
                startRow,endRow = 0 if row == 0 else row - 1, row + 2
                startCol,endCol = 0 if col == 0 else col - 1, col + 2

                subMatrix = previousBatch[startRow:endRow,startCol:endCol]

                if element == 1 and np.count_nonzero(subMatrix == 1) > 4:
                    currentBatch[row,col] = 0
                elif element == 0 and np.count_nonzero(subMatrix == 1) == 0:
                    currentBatch[row,col] = 1
                else:
                    continue

        print(f'The number of occupied seats is: {np.count_nonzero(currentBatch == 1)}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')