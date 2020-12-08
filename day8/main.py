import os, sys, re

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = list(file.read().strip().split('\n'))
        processedInst = []
        idx = accumulator = 0

        while idx < len(batch):
            instruction,value = batch[idx].split(' ')

            if idx in processedInst:
                print(f'This is a repeated instruction. Current accumulator value is {accumulator}')
                break
            else:
                processedInst.append(idx)

            if instruction == 'acc':
                accumulator += int(value)
                idx += 1
            elif instruction == 'jmp':
                idx += int(value)
            else:
                idx += 1

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')