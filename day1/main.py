import os, sys

if len(sys.argv) != 2:
    raise ValueError('Please supply the intcode to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        expenses = list(map(int, file.read().split()))
        values = expenses.copy()

        for expense in expenses:
            for valueToAdd in expenses.copy():
                for secondValueToAdd in expenses.copy():
                    if (expense + valueToAdd + secondValueToAdd) == 2020:
                        print(f'Expense values are {expense} and {valueToAdd} and {secondValueToAdd} giving {expense * valueToAdd * secondValueToAdd}')
                        break


    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')