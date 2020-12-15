import os, sys

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        currentBatch = list(file.read().strip().split(','))

        numbers = [int(n) for n in currentBatch]
        spoken = dict()

        for i,num in enumerate(numbers):
            if i == len(numbers)-1:
                break
            else:
                spoken[num] = i

        while len(numbers) < 2020:

            lastSpokenNum = numbers[-1]
            lastSpokenIdx = len(numbers) - 1
            prevSpokenIdx = spoken.get(lastSpokenNum, False)
            spoken[lastSpokenNum] = lastSpokenIdx

            if prevSpokenIdx is False:
                speak = 0
            else:
                speak = lastSpokenIdx - prevSpokenIdx
            
            numbers.append(speak)

        print(f'The {len(numbers)} number is {numbers[-1]}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')