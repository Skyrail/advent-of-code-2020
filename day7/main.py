import os, sys, re

def get_parents(bags, child):

    parents = set()

    for bag in bags[child]:
        parents.add(bag)
        if bag in bags:
            parents = parents.union(get_parents(bags, bag))

    return parents

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = list(file.read().strip().split('\n'))

        bags = {}
        containerRegex = re.compile(r'^([\S]+\s[\S]+)')
        containsRegex = re.compile(r'([0-9]+)\s([\S]+\s[\S]+)')

        for rule in batch:
            containingBag = containerRegex.match(rule).group()
            containedInBag = containsRegex.findall(rule)

            for count,bag in containedInBag:
                if bag in bags:
                    bags[bag].add(containingBag)
                else:
                    bags[bag] = set([containingBag])

        print(f"The shiny gold bag will go into the following bags: {len(get_parents(bags, 'shiny gold'))}")

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')