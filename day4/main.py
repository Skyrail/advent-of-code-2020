import os, sys  

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = list(file.read().strip().split('\n\n'))

        validCount, validFields = 0, ['byr','iyr','eyr','hgt','hcl','ecl','pid']

        for passport in batch:
            validCount += 1 if all(passport.__contains__(field) for field in validFields) else 0

        print(f'Number of valid passports is: {validCount}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')