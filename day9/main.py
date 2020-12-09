import os, sys

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = list(map(int,file.read().strip().split('\n')))

        result = resultIndex = total = 0
        i = chunkSize = 25

        while i < len(batch):

            current, previousChunk, sums = batch[i], set(batch[i-chunkSize:i]), set()

            for previous in previousChunk:
                sums.add(current - previous)
            
            if len(sums & previousChunk) == 0:
                result, resultIndex = current, i
                print(f'The number {result} cannot be summed from the previous chunk {previousChunk}')
                break
            
            i += 1

        print(f'The result was {result}')

        startIndex = currentIndex = 0

        listLength = len(batch[startIndex:resultIndex])
        while currentIndex < listLength:
            total += batch[currentIndex]

            if total == result:
                contiguousRange = batch[startIndex:currentIndex]
                print(f'Sum of the smallest and largest numbers in contiguous range is {min(contiguousRange) + max(contiguousRange)}')
                break
            elif total > result:
                startIndex += 1
                currentIndex, total = startIndex, 0
            else:
                currentIndex += 1

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')