
import os, sys  

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        passwordPolicyList, validCount = list(file.read().strip().split('\n')), 0

        for policy in passwordPolicyList:
            charPositions, character, password = [val.strip(':') for val in policy.split()]

            positionA,positionB = [int(val) - 1 for val in charPositions.split('-')]

            validCount += 1 if (password[positionA] == character) is not (password[positionB] == character) else 0

        print(f'The valid password count is {validCount}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')