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

            for rowNo,row in enumerate(previousBatch):
                for colNo,column in enumerate(row):
                    if column == 2:
                        continue
                    else:
                        startRow = (rowNo - 1) if (rowNo - 1) >= 0 else 0
                        endRow = rowNo + 2

                        startCol = (colNo - 1) if (colNo - 1) >= 0 else 0
                        endCol = colNo + 2

                        subMatrix = previousBatch[startRow:endRow, startCol:endCol]
                        previousValue = previousBatch[rowNo,colNo]
                        
                        if previousValue == 1 and np.count_nonzero(subMatrix == 1) > 4:
                            currentBatch[rowNo,colNo] = 0
                        elif previousValue == 0 and np.count_nonzero(subMatrix == 1) == 0:
                            currentBatch[rowNo,colNo] = 1
                        else:
                            continue

        print(f'The number of occupied seats is: {np.count_nonzero(currentBatch == 1)}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')