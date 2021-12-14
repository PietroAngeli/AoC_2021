f = open('input.txt')
lines = f.readlines()
f.close()

sheetend = False
folds = []
points = []
maxx = 0
maxy = 0
for line in lines:
    if sheetend:
        fold = line.strip()[11:].split('=')
        fold[1] = int(fold[1])
        folds.append(fold)     
    if line.strip() == '':
        sheetend = True
    if not sheetend:
        point = line.strip().split(',')
        point = [int(point[0]), int(point[1])]
        if point[0]>maxx: maxx = point[0]
        if point[1]>maxy: maxy = point[1]
        points.append(point)

def foldleft(xfold, points):
    newpoints = []
    maxx = 0
    for point in points:
        x = point[0]
        y = point[1]
        if x > xfold:
            x = xfold*2-x
            if x > maxx: maxx = x
            if [x,y] not in points:      
                newpoints.append([x,y])
        else:
            newpoints.append([x,y])
    return(newpoints,maxx)

def foldup(yfold, points):
    newpoints = []
    maxy = 0
    for point in points:
        x = point[0]
        y = point[1]
        if y > yfold:
            y = yfold*2-y
            if y > maxy: maxy = y
            if [x,y] not in points:      
                newpoints.append([x,y])
        else:
            newpoints.append([x,y])
    return(newpoints,maxy)

def printsheet(points, maxx, maxy):
    for j in range(maxy+1):
        for i in range(maxx+1):
            if [i,j] in points: print('#', end='')
            else: print('.', end='')
        print('')

#print('Start sheet:')
#printsheet(points, maxx, maxy)

for fold in folds:
    print('Folding along', fold)
    if fold[0] == 'x':
        (points,maxx) = foldleft(fold[1],points)
    if fold[0] == 'y':
        (points,maxy) = foldup(fold[1],points)
    #print('Result:')
    #printsheet(points, maxx, maxy)
    print('Number of points:', len(points))
    #input('press any key to continue')
printsheet(points, maxx, maxy)