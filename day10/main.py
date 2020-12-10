import os, sys

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = sorted(list(map(int,file.read().strip().split('\n'))))

        differences, index = [], 0
        # The source supplies 0 jolts, the sink uses +3 the max adapter joltage
        batch.insert(0, 0)
        batch.append(max(batch)+3)

        while index < (len(batch) - 1):                
            differences.append(batch[index+1] - batch[index])
            index += 1
        

        print(f'The differences that count: {differences.count(1)*differences.count(3)}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')