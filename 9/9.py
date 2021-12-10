f = open('input.txt')
lines = f.readlines()
f.close()

hmap = {}
proc_line = None
xsize = len(lines[0].strip())
ysize = len(lines)
y = 0
for line in lines:
    proc_line = line.strip()
    x = 0
    for num in proc_line:
        hmap[x,y] = (int(num))
        x+=1
    y+=1

mins = []
minscoords = []
for i in range(xsize):
    for j in range(ysize):
        if i+j == 0: #Check top left corner
            if hmap[i,j] < hmap[i,j+1] and hmap[i,j] < hmap[i+1,j]:
                mins.append(hmap[i,j])
                minscoords.append([i,j])
        elif i == xsize-1 and j == 0: #Check top right corner
            if hmap[i,j] < hmap[i-1,j] and hmap[i,j] < hmap[i,j+1]:
                mins.append(hmap[i,j])
                minscoords.append([i,j])
        elif i == 0 and j == ysize-1: #Check bottom left corner
            if hmap[i,j] < hmap[i+1,j] and hmap[i,j] < hmap[i,j-1]:
                mins.append(hmap[i,j])
                minscoords.append([i,j])
        elif i == xsize-1 and j == ysize-1: #Check bottom right corner
            if hmap[i,j] < hmap[i-1,j] and hmap[i,j] < hmap[i,j-1]:
                mins.append(hmap[i,j])
                minscoords.append([i,j])
        elif i == 0 and j not in [0, ysize-1]: #Check left border
            if hmap[i,j] < hmap[i,j+1] and hmap[i,j] < hmap[i,j-1] and hmap[i,j] < hmap[i+1,j]:
                mins.append(hmap[i,j])
                minscoords.append([i,j])
        elif i not in [0, xsize-1] and j == 0: #Check top border
            if hmap[i,j] < hmap[i,j+1] and hmap[i,j] < hmap[i-1,j] and hmap[i,j] < hmap[i+1,j]:
                mins.append(hmap[i,j])
                minscoords.append([i,j])
        elif i == xsize-1 and j not in [0, ysize-1]: #Check right border
            if hmap[i,j] < hmap[i,j+1] and hmap[i,j] < hmap[i,j-1] and hmap[i,j] < hmap[i-1,j]:
                mins.append(hmap[i,j])
                minscoords.append([i,j])
        elif i not in [0, xsize-1] and j == ysize-1: #Check bottom border
            if hmap[i,j] < hmap[i,j-1] and hmap[i,j] < hmap[i-1,j] and hmap[i,j] < hmap[i+1,j]:
                mins.append(hmap[i,j])
                minscoords.append([i,j])
        else:
            if hmap[i,j] < hmap[i,j-1] and hmap[i,j] < hmap[i-1,j] and hmap[i,j] < hmap[i+1,j] and hmap[i,j] < hmap[i,j+1]:
                mins.append(hmap[i,j])
                minscoords.append([i,j])
score = 0
for val in mins:
    score+=val+1

print('Part 1:', score)

basins = {}
def checkright(i,j,hmap):
    if 9 > hmap[i+1,j] > hmap[i,j]:
        return([i+1,j])
    else:
        return(None)
def checkleft(i,j,hmap):
    if 9 > hmap[i-1,j] > hmap[i,j]:
        return([i-1,j])
    else:
        return(None)
def checkup(i,j,hmap):
    if 9 > hmap[i,j-1] > hmap[i,j]:
        return([i,j-1])
    else:
        return(None)
def checkdown(i,j,hmap):
    if 9 > hmap[i,j+1] > hmap[i,j]:
        return([i,j+1])
    else:
        return(None)
for index in range(len(minscoords)):
    minspot = minscoords[index]
    check = False
    basins[index] = {
        'L0': [minspot]
    } 
    level = 0
    inbasin = []
    while check == False:
        basins[index]['L'+str(level+1)] = []
        for point in basins[index]['L'+str(level)]:
            i = point[0]
            j = point[1]
            if i+j == 0: #Check top left corner
                out = checkright(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)                 
                out = checkdown(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)

            elif i == xsize-1 and j == 0: #Check top right corner
                out = checkleft(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkdown(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)

            elif i == 0 and j == ysize-1: #Check bottom left corner
                out = checkright(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkup(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)

            elif i == xsize-1 and j == ysize-1: #Check bottom right corner
                out = checkleft(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkup(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)

            elif i == 0 and j not in [0, ysize-1]: #Check left border
                out = checkright(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkup(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkdown(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)

            elif i not in [0, xsize-1] and j == 0: #Check top border
                out = checkdown(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkright(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkleft(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)

            elif i == xsize-1 and j not in [0, ysize-1]: #Check right border
                out = checkdown(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkleft(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkup(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)

            elif i not in [0, xsize-1] and j == ysize-1: #Check bottom border
                out = checkup(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkright(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkleft(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
            
            else:
                out = checkup(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkright(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkleft(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
                out = checkdown(i,j,hmap)
                if out and out not in inbasin:
                    basins[index]['L'+str(level+1)].append(out)
                    inbasin.append(out)
            levelcheck = 'L'+str(level+1)
        if len(basins[index][levelcheck]) == 0:
            check = True
        level+=1

sizes = []
for basin in basins:
    sizes.append(0)
    for key in basins[basin]:
        sizes[-1] += len(basins[basin][key])

score = 1
for i in range(3):
    score *= max(sizes)
    sizes.remove(max(sizes))

print('Part 2:', score)