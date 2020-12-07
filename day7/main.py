import os, sys, re

def get_parents(bags, child):

    parents = set()

    for bag in bags[child]:
        parents.add(bag)
        if bag in bags:
            parents = parents.union(get_parents(bags, bag))

    return parents

def get_children_count(bags, parent):

    childrenCount = 0

    for count,bag in bags[parent]:
        childrenCount += int(count)
        if bag in bags:
            childrenCount += get_children_count(bags, bag) * int(count)

    return childrenCount

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = list(file.read().strip().split('\n'))

        containedBags, containerBags, total= {}, {}, 0
        containerRegex = re.compile(r'^([\S]+\s[\S]+)')
        containsRegex = re.compile(r'([0-9]+)\s([\S]+\s[\S]+)')

        for rule in batch:
            containingBag = containerRegex.match(rule).group()
            containedInBag = containsRegex.findall(rule)

            containerBags[containingBag] = containedInBag

            for count,bag in containedInBag:
                if bag in containedBags:
                    containedBags[bag].add(containingBag)
                else:
                    containedBags[bag] = set([containingBag])

        print(f"The shiny gold bag will go into the following bags: {len(get_parents(containedBags, 'shiny gold'))}")
        print(f"The shiny gold bag will contain a total of {get_children_count(containerBags, 'shiny gold')} bags")

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')