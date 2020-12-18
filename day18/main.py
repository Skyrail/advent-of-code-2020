import os, sys, re

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

def evaluate(eq,i=0):
    parenCount,total,op = 0,None,None

    eq = eq.replace(' ', '')

    while i < len(eq):
        c = eq[i]
        if c == '(':
            if op == '+':
                result,i = evaluate(eq, i+1)
                total += result
            elif op == '*':
                result,i = evaluate(eq, i+1)
                total *= result
            else:
                total,i = evaluate(eq, i+1)
        elif c == ')':
            return total,i
        elif c in ('+', '*'):
            op = c
        else:
            if total == None:
                total = int(c)
            elif op == '+':
                total += int(c)
            elif op == '*':
                total *= int(c)
        i += 1

    return (total,i)


if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        currentBatch = file.read().strip().split('\n')

        results = list()

        for eq in currentBatch:
            results.append(evaluate(eq)[0])

        print(sum(results))

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        if file is not None:
            file.close()
else:
    print(f'Unable to locate file {inputPath}')