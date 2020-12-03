
import os, sys  

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        hillMap = list(file.read().strip().split('\n'))
        position, right = 1, 3
        mapWidth, treeCount = len(hillMap[0]), 0

        for line in hillMap[1:]:
            position += right if position < (mapWidth - (right - 1)) else -(mapWidth - right)
            treeCount += 1 if line[position - 1] == '#' else 0

        print(f'Tree count: {treeCount}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')