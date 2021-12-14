f = open('smalltest.txt')
lines = f.readlines()
f.close()

class Cave:
    def __init__(self, name):
        self.name = name
        self.islarge = name.isupper()
        self.connections = []

class Path:
    def __init__(self, firstmove):
        self.smalltwice = False
        self.route = firstmove
        
caves = {}

for line in lines:
    tunnel = line.strip().split('-')
    end0 = tunnel[0]
    end1 = tunnel[1]
    if end0 in caves:
        if end1 not in caves[end0].connections:
            caves[end0].connections.append(end1)
    else:
        caves[end0] = Cave(end0)
        caves[end0].connections.append(end1)

    if end1 in caves:
        if end0 not in caves[end1].connections:
            caves[end1].connections.append(end0)
    else:
        caves[end1] = Cave(end1)
        caves[end1].connections.append(end0)

paths = []
stop = False
pathlen = 2

for cave in caves:
    if 'start' in caves[cave].connections:
        paths.append(Path(['start',cave]))

while not stop:
    index = 0
    while index < len(paths):
        current = paths[index].route[-1]
        if current != 'end':
            wasupdated = False
            connectedcaves = caves[current].connections
            pathchek = paths[index].route.copy()
            for cave in connectedcaves:
                if cave != 'start':
                    if caves[cave].islarge or cave not in paths[index].route:
                        if wasupdated:
                            newpath = paths[index].route[:-1]
                            newpath.append(cave)
                            paths.append(Path(newpath))
                        else:
                            paths[index].route.append(cave)
                            wasupdated = True
                    elif caves[cave].islarge == False and paths[index].route.count(cave) == 1 and paths[index].smalltwice == False and cave != 'end':
                        paths[index].smalltwice = True
                        if wasupdated:
                            newpath = paths[index]
                            newpath.route.append(cave)
                            paths.append(newpath)
                        else:
                            paths[index].route.append(cave)
                            wasupdated = True
            if paths[index] == pathchek: # We hit a dead end!
                paths.pop(index)
                index -= 1
        index += 1
    stop = True
    for path in paths:
        if path.route[-1] != 'end':
            stop = False

count = 0
for path in paths:
    if path.route[-1] == 'end':
        count += 1

    '''
    for cave in caves:
        for path in paths:
            connectedcaves = caves[path[-1]].connections
            if path[-1] != cave:
                if (caves[cave].islarge) or (caves[cave].name not in path):
                    if path[:-1] not in paths:
                        path.append(cave)
                    else:
                        newpath = path
                        newpath.append(cave)
                        paths.append(newpath)                  
    stop = True
    for path in paths:
        if path[-1] != 'end':
            stop = False
    '''
print('Part 1:', count)