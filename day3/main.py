
import os, sys  

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        hillMap = list(file.read().strip().split('\n'))
        mapWidth, treeMultiplyValue = len(hillMap[0]), 1

        testMovements = [[1,1],[3,1],[5,1],[7,1],[1,2]]

        for movements in testMovements:
            x, y, right, down, treeCount = 1, 0, movements[0], movements[1], 0

            while y < len(hillMap[1:]):
                x += right if x < (mapWidth - (right - 1)) else -(mapWidth - right)
                y += down
                treeCount += 1 if hillMap[y][x - 1] == '#' else 0

            treeMultiplyValue *= treeCount

        print(f'Tree multiply value: {treeMultiplyValue}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')