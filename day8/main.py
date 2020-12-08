import os, sys, re

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

def runBatch(batch):

    processedInst = []
    idx = accumulator = 0

    while idx < len(batch):
        instruction,value = batch[idx].split(' ')

        if idx in processedInst:
            return False, accumulator
        else:
            processedInst.append(idx)

        if instruction == 'acc':
            accumulator += int(value)
            idx += 1
        elif instruction == 'jmp':
            idx += int(value)
        else:
            idx += 1

    return True, accumulator


if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = list(file.read().strip().split('\n'))

        for idx,line in enumerate(batch):

            modifiedBatch = batch.copy()
            instruction,value = line.split(' ')

            if instruction == 'nop':
                modifiedBatch[idx] = line.replace('nop', 'jmp')
            elif instruction == 'jmp':
                modifiedBatch[idx] = line.replace('jmp', 'nop')

            result,accumulator = runBatch(modifiedBatch)

            if result:
                print(f'Succesful program termination with accumulator value {accumulator}')
                break


    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')