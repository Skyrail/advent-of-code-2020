import os, sys, re

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = list(map(int,file.read().strip().split('\n')))

        i = chunkSize = 25

        while i < len(batch):

            current, previousChunk, sums = batch[i], set(batch[i-chunkSize:i]), set()

            for previous in previousChunk:
                sums.add(current - previous)
            
            if len(sums & previousChunk) == 0:
                print(f'The number {current} cannot be summed from the previous chunk {previousChunk}')
                break
            
            i += 1

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')