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

        gridWidth = len(dimensions[0][0])
        gridHeight = len(dimensions[0])

        cMin,cMax = -gridWidth-1,gridWidth+1
        rMin,rMax = -gridHeight-1,gridHeight+1
        lMin,lMax = -2,2
        tMin,tMax = -2,2

        prevActive = set()

        for ri,row in enumerate(dimensions[0]):
            for ci,col in enumerate(row):
                if col == '#':
                    prevActive.add((0,0,ri,ci)) 

        while cycle < 6:

            active = set()

            for w in (range(tMin,tMax)):
                for z in range(lMin,lMax):
                    for y in range(rMin,rMax):
                        for x in range(cMin,cMax):
                            activeCount = 0
                            for wi in searchArea:
                                for zi in searchArea:
                                    for yi in searchArea:
                                        for xi in searchArea:
                                            if zi == 0 and yi == 0 and xi == 0 and wi == 0:
                                                continue

                                            checkX = x + xi
                                            checkY = y + yi
                                            checkZ = z + zi
                                            checkW = w + wi

                                            if (checkW,checkZ,checkY,checkX) in prevActive:
                                                activeCount += 1
                                
                            if (w,z,y,x) in prevActive and (2 <= activeCount <= 3):
                                active.add((w,z,y,x))
                            elif (w,z,y,x) not in prevActive and activeCount == 3:
                                active.add((w,z,y,x))

            lMin,lMax = lMin-1,lMax+1
            rMin,rMax = rMin-1,rMax+1
            cMin,cMax = cMin-1,cMax+1
            tMin,tMax = tMin-1,tMax+1

            prevActive = deepcopy(active)

            cycle += 1

        print(len(active))

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        if file is not None:
            file.close()
else:
    print(f'Unable to locate file {inputPath}')