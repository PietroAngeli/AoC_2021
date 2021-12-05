f = open('input.txt')
lines = f.readlines()
f.close()
coords = []
mapsize = [0,0]
for line in lines:
    temp = line.strip()
    temp = temp.split(' -> ')
    temp = [i.split(',') for i in temp]
    for i in range(2):
        for j in range(2):
            temp[i][j] = int(temp[i][j])
            if mapsize[j] < temp[i][j]+1:
                 mapsize[j] = temp[i][j]+1
    coords.append(temp)
print(mapsize)
map=[]
for y in range(mapsize[1]):
    map.append([])
    for x in range(mapsize[0]):
        map[-1].append(0)

for coord in coords:
    x1 = coord[0][0]
    x2 = coord[1][0]
    y1 = coord[0][1]
    y2 = coord[1][1]
    xmax = max([x1,x2])
    ymax = max([y1,y2])
    if (x1 == x2):
        for y in range(min(y1, y2), max(y1, y2)+1):
            map[y][x1]+=1
    elif (y1 == y2):
        for x in range(min(x1, x2), max(x1, x2)+1):
            map[y1][x]+=1
    
    else:
        x = x1
        y = y1
        while (x!=x2) and (y!=y2):
            map[y][x]+=1
            if x < x2:             
                x+=1
            else:
                x-=1
            if y < y2:             
                y+=1
            else:
                y-=1
        map[y2][x2]+=1
dangerpoints = 0
for row in map:
    #print(''.join([str(i) for i in row]))
    for point in row:
        if point >= 2:
            dangerpoints+=1
print(dangerpoints)
