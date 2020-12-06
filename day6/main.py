import os, sys  

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = list(file.read().strip().split('\n\n'))

        total = 0

        for group in batch:
            answers = [set(results) for results in group.split()]
            total += len(set.intersection(*answers))

        print(f'The total is {total}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')