import os, sys, re
from functools import reduce
from itertools import product

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        currentBatch = file.read().strip().split('\n')

        mask, masks, memory = "X"*36, list(), dict()

        for line in currentBatch:

            if 'mask' in line:
                mask, masks = line[7:], list()

                maskFloatingBits = list(product('01', repeat=mask.count('X')))

                for combination in maskFloatingBits:

                    maskCopy = mask
                    
                    for bit in combination:
                        maskCopy = maskCopy.replace('X', str(bit), 1)

                    masks.append(maskCopy)
                    
            else:
                regex = r'mem\[([\d]+)\] = ([\d]+)'
                address,value = re.findall(regex, line)[0]
                binary = format(int(address), '036b')

                for combination in masks:

                    memoryAddress = list(binary)

                    for i,bit in enumerate(list(combination)):
                        if mask[i] == 'X' or mask[i] == '1':
                            memoryAddress[i] = bit

                    memoryAddress = "".join(memoryAddress)
                    
                    memory[memoryAddress] = value

        memorySum = reduce(lambda x,y:int(x)+int(y), memory.values())

        print(f'The memory sum is: {memorySum}')


    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')