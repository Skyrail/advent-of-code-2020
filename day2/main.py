
import os, sys  

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        passwordPolicyList, validCount = list(file.read().strip().split('\n')), 0

        for policy in passwordPolicyList:
            charCount, character, password = [val.strip(':') for val in policy.split()]

            minCount,maxCount = [int(val) for val in charCount.split('-')]

            actualCount = password.count(character)

            validCount += 1 if minCount <= actualCount <= maxCount else 0

        print(f'The valid password count is {validCount}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')