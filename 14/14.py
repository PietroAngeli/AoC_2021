from collections import Counter

f = open('test.txt')
lines = f.readlines()
f.close()

poly = lines[0].strip()
rules = {}

for line in lines[2:]:
    rule = line.strip().split(' -> ')
    rules[rule[0]]=rule[1]

def findpairs(poly):
    pairs = []
    for index in range(len(poly)-1):
        pairs.append()
    return(pairs)

def splicepoly(poly, rules):
    index = 0
    newpoly = ''
    while index < len(poly):
        newpoly += poly[index]
        pair = poly[index:index+2]
        if pair in rules:
            newpoly += rules[pair]
        index += 1
    return(newpoly)

def polyeval(poly):
    elements = [element for element in poly]
    counter = Counter(elements)
    return(max(counter.values())-min(counter.values()))

#print('Start:',poly)
for step in range(10):
    poly = splicepoly(poly,rules)
    print('Step:', step)
    print(poly)

print('Part 1:', polyeval(poly))

for step in range(11,30):
    print('Step:', step)
    poly = splicepoly(poly,rules)

print('Part 2:', polyeval(poly))