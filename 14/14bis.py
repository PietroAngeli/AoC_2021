from collections import Counter

f = open('test.txt')
lines = f.readlines()
f.close()

poly = lines[0].strip()
rules = {}

for line in lines[2:]:
    rule = line.strip().split(' -> ')
    rules[rule[0]]=rule[1]

def polyeval(poly):
    elements = [element for element in poly]
    counter = Counter(elements)
    return(max(counter.values())-min(counter.values()))

steps = 10
newpoly = poly[0]
for i in range(1, len(poly)):
    newpoly+=poly[i]
    for j in range(steps):
        if newpoly[]
    #if i == 10: print(polyeval(newpoly))
    newpoly