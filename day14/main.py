import os, sys, re
from functools import reduce

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        currentBatch = file.read().strip().split('\n')

        mask = "X"*36
        memory = dict()

        for line in currentBatch:
            # If mask field - update mask
            if 'mask' in line:
                mask = line[7:]
            else:
                regex = r'mem\[([\d]+)\] = ([\d]+)'
                address,value = re.findall(regex, line)[0]
                binary = format(int(value), '036b')

                binaryList = list(binary)

                for i,m in enumerate(mask):
                    if m == 'X':
                        continue

                    binaryList[i] = m

                memory[address] = int("".join(binaryList), 2)

        memorySum = reduce(lambda x,y:x+y, memory.values())

        print(f'The memory sum is: {memorySum}')


    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')