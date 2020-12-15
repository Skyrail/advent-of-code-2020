import os, sys

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        currentBatch = list(file.read().strip().split(','))

        i,numbers = len(currentBatch), [int(n) for n in currentBatch]
        while len(numbers) < 2020:
            previousNo = numbers[-1]

            if previousNo not in numbers[:-1]:
                numbers.append(0)
            else:
                idx = len(numbers) - 2- numbers[:-1][::-1].index(previousNo)
                numbers.append(i - 1 - idx)

            i += 1

        print(numbers[len(numbers) - 1])

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')