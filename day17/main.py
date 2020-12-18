import os, sys
from copy import copy,deepcopy
from collections import defaultdict

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        currentBatch = file.read().strip().split('\n')
        currentBatch = [list(x) for x in currentBatch]

        dimensions, cycle = defaultdict(list), 0
        dimensions[0] = currentBatch

        searchArea = (-1, 0, 1)

        def printGrid(dimensions):
            print('='*20,f'Layer','='*20)
            for R in dimensions:
                print("".join(R))

        while cycle < 6:

            for Li,L in dimensions.items():
                for Ri,R in enumerate(L):
                    dimensions[Li][Ri] = ['.'] + R + ['.']
                newRow = [['.'] * len(dimensions[0][0])]
                dimensions[Li] = deepcopy(newRow) + dimensions[Li] + deepcopy(newRow)

            newLayerRow = ['.'] * len(dimensions[0][0])
            
            newLayer = []
            for _ in range(len(dimensions[0])):
                newLayer.append(deepcopy(newLayerRow))


            dimensions[(max(dimensions.keys())+1)] = deepcopy(newLayer)
            dimensions[(min(dimensions.keys())-1)] = deepcopy(newLayer)

            prevDimensions = deepcopy(dimensions)

            minZ = min(prevDimensions.keys())
            maxZ = max(prevDimensions.keys())
            maxY = len(prevDimensions[0])
            maxX = len(prevDimensions[0][0])

            for layer in range(minZ,maxZ+1):
                for row in range(maxY):
                    for col in range(maxX):
                        element = prevDimensions[layer][row][col]
                        activeCount = 0

                        for zi in searchArea:
                            for yi in searchArea:
                                for xi in searchArea:
                                    if(xi == 0 and yi == 0 and zi == 0):
                                        continue

                                    xIndex = col + xi
                                    yIndex = row + yi
                                    zIndex = layer + zi

                                    if (0 <= xIndex < maxX) and (0 <= yIndex < maxY) and (minZ <= zIndex <= maxZ) and prevDimensions[zIndex][yIndex][xIndex] == '#':
                                        activeCount += 1

                        if element == '#' and not (2 <= activeCount <= 3):
                            dimensions[layer][row][col] = '.'
                        elif element == '.' and activeCount == 3:
                            dimensions[layer][row][col] = '#'

            cycle += 1

        totalActive = 0

        for L in dimensions.values():
            for R in L:
                for C in R:
                    if C == '#':
                        totalActive += 1

        print(totalActive)

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        if file is not None:
            file.close()
else:
    print(f'Unable to locate file {inputPath}')