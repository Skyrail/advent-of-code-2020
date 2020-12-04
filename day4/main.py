import os, sys  

def validateField(field):
    type,value = field.split(':')

    if type == 'byr':
        return len(value) == 4 and 1920 <= int(value) <= 2002

    if type == 'iyr':
        return len(value) == 4 and 2010 <= int(value) <= 2020

    if type == 'eyr':
        return len(value) == 4 and 2020 <= int(value) <= 2030

    if type == 'hgt':
        if value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193:
            return True
        if value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76:
            return True

    if type == 'hcl':
        return value[0] == '#' and all([char in 'abcdef0123456789' for char in value[1:]])

    if type == 'ecl':
        return value in ['amb','blu','brn','gry','grn','hzl','oth']

    if type == 'pid':
        return len(value) == 9

    if type == 'cid':
        return True

    return False

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = list(file.read().strip().split('\n\n'))

        validCount, validFields = 0, ['byr','iyr','eyr','hgt','hcl','ecl','pid']

        for passport in batch:
            if all(passport.__contains__(f) for f in validFields):
                validCount += 1 if all([validateField(field) for field in passport.split()]) else 0

        print(f'Number of valid passports is: {validCount}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')