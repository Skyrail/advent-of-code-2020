import os, sys
from functools import reduce

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        currentBatch = file.read().strip().split('\n')

        busIds = currentBatch[1].split(',')

        N = reduce(lambda a,b: a*b, [int(id) for id in busIds if id != 'x'])
        sum = 0

        for i,n in enumerate(busIds):
            if n == 'x':
                continue

            n = int(n)
            a = n - i
            y = N // n
            z = pow(y, -1, n)

            sum += a * y * z
            sum %= N 

        print(f'The timestamp is: {sum}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')